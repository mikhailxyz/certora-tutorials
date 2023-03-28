certoraRun ERC20Bug1.sol:ERC20 --verify ERC20:ERCVacuity.spec \
--solc solc8.19 \
--send_only \
--optimistic_loop \
--rule_sanity \
--msg "$1"