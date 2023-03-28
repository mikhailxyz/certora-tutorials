### Unit test

- (from solution) impossible to end earlier (only checking `end` method)
- (from solution) impossible to set `ended` flag to `true` before it's time
- (from solution) impossible to restart
- (from solution) check correctness of bid functions:
  1 - if bid succeeded, the bidder should become the highestBidder and their balance should be updated respectively
  2 - if the sum of bidder's previous bids and current bid is less than current highestBid, then bid should revert
- (from solution) check correctness of withdraw():
  1 - check that current highestBidder cannot withdraw
  2 - if withdraw succeeded, then user's bids should be 0 and token balance should increase respectively
- (from solution) highest bidder cannot withdraw
- (From solution) At the end of auction a seller will get NFT back or get tokens

- NFT token can only be transferred to the highest bidder

### Variable transition

- Monotonicity of the highest bid
- bids[bidder] decreased -> withdraw function was called
- bids[bidder] increased -> deposit function was called
- 2 - if the auction was started, start() was called
<!-- - Payment remains constant for a given auction
- total supply goes up only
- can be only closed through `close()` method
- (from solution) no other way to increase users balance besides becoming a winner and calling `close()` method -->

### State transition

- nonstarted > started > ended
- (from solution) once ended, always remains ended
- (from solution)// started iff contract holds nft:
1 - if start() succeeded, auction contract must hold NFT
<!-- - If not created, getAuction() returns all 0s
- If created, getAuction() returns all non-0s -->

### Valid states

- (from solution) if noone bid, all bids are 0
- (from solution) correlation of the highestBidder with highestBid: if highestBidder is 0, then highestBid is 0
- (from solution) If a user isn't the highestBidder, they should have less bids than highestBid
- (from solution) Nobody can have a higher bid than highestBid

### High Level Properties

- NFT Token address cannot be changed
- ERC20 Token address cannot be changed
- Seller cannot be changed
- (from solution) only balance of a specific user can change after a function call
- (from solution) system should have at least the sum of all bids to be able to payback everybody
<!-- - the balance of a single arbitrary user should be no more than the total supply of tokens
- (from solution) no way to delete an auction if `auctions[id].bid_expiry == 0` or `(auctions[id].bid_expiry >= now || auctions[id].end_time >= now)` -->

### Risk assessment
