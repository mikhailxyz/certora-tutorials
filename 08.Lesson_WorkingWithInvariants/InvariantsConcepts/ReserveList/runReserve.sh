certoraRun ReserveListFixed.sol:ReserveList --verify ReserveList:Reserve.spec \
--solc solc8.19 \
--optimistic_loop \
--loop_iter 3 \
--msg "correlated lists broken"

# --optimistic_loop and --loop_iter 3 are flags that handle loops.
# They are needed here, but don't mind them, you will learn about loop handling in a future lesson.