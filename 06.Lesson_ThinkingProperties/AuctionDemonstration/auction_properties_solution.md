### Unit test

- New auction can be created only by the owner
- (from solution) mint() correctly increases `balances[who]` and `totalSupply`
- (from solution) transferTo() correctly increases `balances[_to]` and correctly decreases `balances[msg.sender]`

### Variable transition

- Prize can only be decreased every bid
- Payment remains constant for a given auction
- total supply goes up only
- can be only closed through `close()` method
- (from solution) no other way to increase users balance besides becoming a winner and calling `close()` method

### State transition

- If not created, getAuction() returns all 0s
- If created, getAuction() returns all non-0s

### Valid states

### High Level Properties

- the balance of a single arbitrary user should be no more than the total supply of tokens
- (from solution) no way to delete an auction if `auctions[id].bid_expiry == 0` or `(auctions[id].bid_expiry >= now || auctions[id].end_time >= now)`
