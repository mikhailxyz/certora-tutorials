certoraRun ArrayUniqueBug.sol \
--verify ArrayUniqueBug:ArrayUniqueBug.spec \
--solc solc8.19 \
--send_only \
--optimistic_loop \
--loop_iter 4 \
--rule_sanity \
--msg "ArrayUniqueBug.sol with sanity check"
