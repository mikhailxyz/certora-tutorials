certoraRun Array.sol \
--verify Array:Array.spec \
--solc solc8.19 \
--send_only \
--optimistic_loop \
--loop_iter 4 \
--rule_sanity \
--msg "Array.sol with sanity check"