// #contract Array.sol:Array
methods {
    get(uint) returns (address) envfree
    getWithDefaultValue(uint) returns (address) envfree
}


invariant uniqueArrayUsingRevert(uint256 i, uint256 j)
(
    (get@withrevert(i) == get@withrevert(j)) => (i == j)
)


invariant uniqueArray(uint256 i, uint256 j)
    i != j => (
        (getWithDefaultValue(i) != getWithDefaultValue(j)) ||
        ((getWithDefaultValue(i)  == 0) && (getWithDefaultValue(j) == 0))
    )
