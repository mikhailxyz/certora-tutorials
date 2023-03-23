date=$(date "+%Y-%m-%d %H:%M:%S")

certoraRun  EnglishAuction.sol dependencies/DummyERC20A.sol dependencies/DummyERC721A.sol \
    --verify EnglishAuction:exampleSpec.spec \
    --link EnglishAuction:token=DummyERC20A \
    --link EnglishAuction:nft=DummyERC721A --solc solc8.19 \
    --optimistic_loop \
    --send_only \
    --msg "EnglishAuction $date"
