definition UNINITIALIZED() returns uint256 = 0;
definition PENDING() returns uint256 = 1;
definition STARTED() returns uint256 = 2;
definition ENDED() returns uint256 = 3;
definition CANCELLED() returns uint256 = 4;


// check that the meeting can be joined only when it is started
// and the number of participants is increased by 1
rule canBeJoinedOnlyWhenStarted(method f, uint256 meetingId) {
  env e;

  uint256 numOfParticipantsBefore = getnumOfParticipants(e, meetingId);
  uint8 state = getStateById(e, meetingId);

  joinMeeting(e, meetingId);

  uint256 numOfParticipantsAfter = getnumOfParticipants(e, meetingId);

  assert state == 2 => numOfParticipantsAfter - numOfParticipantsBefore == 1; 
}

rule monotonicityOfNumberOfParticipants(method f, uint256 meetingId) {
  env e; calldataarg args;

  uint256 numOfParticipantsBefore = getnumOfParticipants(e, meetingId);
  uint8 state = getStateById(e, meetingId);
  require state != 0;

  f(e, args);

  uint256 numOfParticipantsAfter = getnumOfParticipants(e, meetingId);

  assert numOfParticipantsAfter >= numOfParticipantsBefore;
}

rule validStateTransitions(method f, uint256 meetingId) {
  env e; calldataarg args;
  
    uint8 state = getStateById(e, meetingId);

    f(e, args);

    uint8 newState = getStateById(e, meetingId);

    assert (state == UNINITIALIZED() => newState == PENDING()) ||
      (state == PENDING() => newState == STARTED() || newState == CANCELLED()) ||
      (state == STARTED() => newState == ENDED()) ||
      (state == CANCELLED() <=> newState == CANCELLED());
}