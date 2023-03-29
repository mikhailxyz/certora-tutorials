certoraRun Loops.sol:Loops --verify Loops:LoopsUnrolling.spec \
--solc solc7.6 \
--send_only \
--loop_iter 1 \
--msg "$1"