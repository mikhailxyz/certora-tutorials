methods{
    totalSupply() returns (uint256) envfree
    balanceOf(address) returns (uint256) envfree
    transfer(address, uint256) returns (bool)
    allowance(address, address) returns (uint256) envfree
    increaseAllowance(address, uint256) returns (bool)
    decreaseAllowance(address, uint256) returns (bool)
    approve(address, uint256) returns (bool)
    transferFrom(address, address, uint256) returns (bool)
    mint(address, uint256)
    burn(address, uint256)
}    



/* 
 * Try to think about how we can check if this rule is a tautology.
 * It is not as simple as copying the assert to a rule.
 * These problems are being addressed by the Certora team as we try to automate checks for vacuity.
 */
// checks the integrity of increaseAllowance
rule increaseAllowanceIntegrity(address spender, uint256 amount){
    env e;
    address owner;
    require owner == e.msg.sender;
    uint256 _allowance = allowance(owner, spender);
    increaseAllowance(e, spender, amount);
    uint256 allowance_ = allowance(owner, spender);
    assert _allowance <= allowance_;
    assert false, "increaseAllowanceIntegrity has non reverting path";
}

// checks that each function changes balance of at most one user
rule balanceOfChange(method f, address user1, address user2) {
    uint256 balanceOf1Before = balanceOf(user1);
    uint256 balanceOf2Before = balanceOf(user2);
    require !((!(balanceOf1Before < balanceOf2Before)) && (!(balanceOf2Before < balanceOf1Before)));
    env e;
    calldataarg args;
    f(e, args);
    uint256 balanceOf1After = balanceOf(user1);
    uint256 balanceOf2After = balanceOf(user2);
    assert ((balanceOf1After != balanceOf1Before) && 
            (balanceOf2After != balanceOf1Before)) 
               => user1 != user2; 
}

// checks that mint and burn are inverse operations
rule mintBurnInverse(address user, uint256 amount) {
    uint256 balanceBefore = balanceOf(user);
    env e;
    mint(e, user, amount);
    burn(e, user, amount);
    uint256 balanceAfter = balanceOf(user);
    assert balanceBefore == balanceAfter;
}


