methods {
    // getFunds implementation does not require any context to get successfully executed
    getFunds(address) returns (uint256) envfree
    // deposit's implementation uses msg.sender, info that's encapsulated in the environment
    // so does withdraw and transfer
    deposit(uint256)
    widthdraw() returns (bool)
    transfer(address, uint256)
    // getTotalFunds implementation does not require any context to get successfully executed
    getTotalFunds() returns (uint256) envfree
    // getEthBalance implementation does not require any context to get successfully executed
    getEthBalance(address) returns (uint256) envfree
}

function preFunctionCall(env e) returns bool {
    uint256 userFunds = getFunds(e, e.msg.sender);
	uint256 total = getTotalFunds(e);
    return total >= userFunds;
}

function callDeposit(env e, uint256 amount){
    deposit(e, amount);
}

function assetTotalGreaterThanSingle(uint256 total, uint256 userFunds){
    assert ( total >=  userFunds, "Total funds are less than a user's funds " );
}

rule totalFundsAfterDeposit(uint256 amount) {
	env e; 
	
    bool preCall = preFunctionCall(e);
	
    callDeposit(e, amount);

	uint256 userFundsAfter = getFunds(e, e.msg.sender);
	uint256 totalAfter = getTotalFunds(e);
	
    assetTotalGreaterThanSingle(totalAfter, userFundsAfter);
    // This assert is here since the syntax checker expects an assert as the last line of a rule.
    // assert (true) will always pass.
    assert (true); // Comment this line out and look at the running error you get.
}


rule totalFundsAfterDepositWithPrecondition(uint256 amount) {
	env e; 
	
    bool preCall = preFunctionCall(e);
    
    require preCall;
	callDeposit(e, amount);

	uint256 userFundsAfter = getFunds(e, e.msg.sender);
	uint256 totalAfter = getTotalFunds(e);
	
    assetTotalGreaterThanSingle(totalAfter, userFundsAfter);
    // This assert is here since the syntax checker expects an assert as the last line of a rule.
    // assert (true) will always pass.
    assert (true); // Comment this line out and look at the running error you get.
}

