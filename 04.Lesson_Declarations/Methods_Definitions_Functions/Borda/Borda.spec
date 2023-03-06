methods {
    getPointsOfContender(address) returns (uint256) envfree;
    hasVoted(address) returns (bool) envfree;
    getWinner() returns (address, uint256) envfree;
    getFullVoterDetails(address) returns (uint8, bool, bool, uint256, bool) envfree;
    getFullContenderDetails(address) returns (uint8, bool, uint256) envfree;

    registerVoter(uint8) returns (bool);
    registerContender(uint8) returns (bool);
    vote(address, address, address) returns (bool);
}

function getBlockedFlag(address voter) returns bool {
    uint8 age; bool voterRegBefore; bool voted; uint256 vote_attempts; bool blocked;
    age, voterRegBefore, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return blocked;
}

function getRegisteredFlag(address voter) returns bool {
    uint8 age; bool voterRegBefore; bool voted; uint256 vote_attempts; bool blocked;
    age, voterRegBefore, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return voterRegBefore;
}

function getVoterVoteAttempts(address voter) returns uint256{
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool black_listed;
    age, voterReg, voted, vote_attempts, black_listed = getFullVoterDetails(voter);
    return vote_attempts;
}

function getVoterAge(address voter) returns uint8{
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool black_listed;
    age, voterReg, voted, vote_attempts, black_listed = getFullVoterDetails(voter);
    return age;
}

function getVoterHasVoted(address voter) returns bool{
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool black_listed;
    age, voterReg, voted, vote_attempts, black_listed = getFullVoterDetails(voter);
    return voted;
}

definition REGISTER_VOTER_SELECTOR() returns uint32 = registerVoter(uint8).selector;

// If a voter isn't registered every detail should return default value
definition unRegisterVoter(address voter) returns bool = 
        getVoterAge(voter) == 0 && !getRegisteredFlag(voter) &&
        !getVoterHasVoted(voter) && getVoterVoteAttempts(voter) == 0 && 
        !getBlockedFlag(voter);

// A registered voter that hasn't voted cannot be black listed, nor have any voting attempts.
// Note that the age is undetermained because we never demanded anything on the age in the implementation
definition registeredYetVotedVoter(address voter) returns bool = 
        getRegisteredFlag(voter) && !getVoterHasVoted(voter) && 
        getVoterVoteAttempts(voter) == 0 && !getBlockedFlag(voter);

// A registered voter that has already voted, but yet to be black listed
definition legitRegisteredVotedVoter(address voter) returns bool = 
        getRegisteredFlag(voter) && getVoterHasVoted(voter) && 
        (getVoterVoteAttempts(voter) >= 1 && getVoterVoteAttempts(voter) <= 2) && 
        !getBlockedFlag(voter);

// A registered voter that has already voted, and is black listed
definition blockedVoter(address voter) returns bool = 
        getRegisteredFlag(voter) && getVoterHasVoted(voter) &&
        getVoterVoteAttempts(voter) >= 3 && getBlockedFlag(voter);

// Checks that a voter's "registered" mark is changed correctly - 
// If it's false after a function call, it was false before
// If it's true after a function call, it either started as true or changed from false to true via registerVoter()
rule registeredCannotChangeOnceSet(method f, address voter){
    env e; calldataarg args;
    uint256 age; bool voterRegBefore; bool voted; uint256 vote_attempts; bool blocked;
    age, voterRegBefore, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    f(e, args);
    bool voterRegAfter;
    age, voterRegAfter, voted, vote_attempts, blocked = getFullVoterDetails(voter);

    assert (!voterRegAfter => !voterRegBefore, "voter changed state from registered to not registered after a function call");
    assert (voterRegAfter => 
        ((!voterRegBefore && f.selector == REGISTER_VOTER_SELECTOR()) || voterRegBefore), 
            "voter was registered from an unregistered state, by other function then registerVoter()");
}

// Checks that each voted contender receieves the correct amount of points after each vote
rule correctPointsIncreaseToContenders(address first, address second, address third){
    env e;
    uint256 firstPointsBefore = getPointsOfContender(first);
    uint256 secondPointsBefore = getPointsOfContender(second);
    uint256 thirdPointsBefore = getPointsOfContender(third);

    vote(e, first, second, third);
    uint256 firstPointsAfter = getPointsOfContender(first);
    uint256 secondPointsAfter = getPointsOfContender(second);
    uint256 thirdPointsAfter = getPointsOfContender(third);
    
    assert (firstPointsAfter - firstPointsBefore == 3, "first choice receieved other amount than 3 points");
    assert (secondPointsAfter - secondPointsBefore == 2, "second choice receieved other amount than 2 points");
    assert (thirdPointsAfter - thirdPointsBefore == 1, "third choice receieved other amount than 1 points");

}

// Checks that a blocked voter cannot get unlisted
rule onceBlockedNotOut(method f, address voter){
    env e; calldataarg args;

    bool blocked_before; bool registered_before;
    registered_before = getRegisteredFlag(voter);
    blocked_before = getBlockedFlag(voter);
    require blocked_before => registered_before;
    f(e, args);
    bool blocked_after;
    blocked_after = getBlockedFlag(voter);
    
    assert blocked_before => blocked_after, "the specified user got out of the blocked users' list";
}

// Checks that a contender's point count is non-decreasing
rule contendersPointsNondecreasing(method f, address contender){
    env e; calldataarg args;
    uint8 age; bool registeredBefore; uint256 pointsBefore;
    age, registeredBefore, pointsBefore = getFullContenderDetails(contender);
    require pointsBefore > 0 => registeredBefore; 
    f(e,args);
    bool registeredAfter; uint256 pointsAfter;
    age, registeredAfter, pointsAfter = getFullContenderDetails(contender);

    assert (pointsAfter >= pointsBefore);
}

