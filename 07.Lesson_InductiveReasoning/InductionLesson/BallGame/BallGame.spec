
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	ballAt() != 4 && ballAt() != 3

rule neverReachPlayer4Rule(method f){
    env e; calldataarg args;

    uint256 positionBefore = ballAt();
    require positionBefore != 3 && positionBefore != 4;

    f(e, args);

    uint256 positionAfter = ballAt();
    assert positionAfter != 3 && positionAfter != 4, "The ball is at the hands of player 4 or 3";
}
