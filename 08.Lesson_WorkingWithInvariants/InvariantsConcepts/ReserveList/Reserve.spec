methods {
  getTokenAtIndex(uint256 id) returns (address token) envfree
  getIdOfToken(address token) returns (uint256 id) envfree
  getReserveCount() returns (uint256 count) envfree
  removeReserve(address) envfree
}

// invariant mappingCorrelation(uint256 index, address token)
//     (( index != 0 && token != 0 ) => (getTokenAtIndex(index) == token <=> getIdOfToken(token) == index)) 
//             &&
// 	(( index == 0 && token !=0 ) => (getTokenAtIndex(index) == token => getIdOfToken(token) == index))
//         {
//             preserved
//             {
//                 requireInvariant indexLessThanCount(token);
//             }
            
//             preserved removeReserve(address t) {
// 			    require t == token;
// 		    }
//         }

// // if the number of elements in the list is non-zero,
// // the id of an existing asset must not exceed the number of elements
// invariant indexLessThanCount(address token)
//     (getReserveCount() > 0 => getIdOfToken(token) < getReserveCount()) &&
//     (getReserveCount() == 0 => getIdOfToken(token) == 0)
//         {
//             preserved removeReserve(address t) {
// 			    require t == token;
// 		    }
//         }

invariant validTokenId(address token)
  (getReserveCount() > 0 => getIdOfToken(token) < getReserveCount()) &&
  (getReserveCount() == 0 => getIdOfToken(token) == 0)
        {
            preserved removeReserve(address t) {
			        require t == token;
		        }
        }


invariant listsAreCorrelated(uint256 id, address token) 
    id > 0 && token != 0  => (getTokenAtIndex(id) == token <=> getIdOfToken(token) == id)
   && (id == 0 && token != 0  => (getTokenAtIndex(id) == token => getIdOfToken(token) == id))
    { 
        preserved
        {
            requireInvariant validTokenId(token);
        }

        preserved removeReserve(address t) {
			    require t == token;
		    }
    }

invariant noTokenAtIndexGreaterThanReserveCount(address tokenAddress)
  (getReserveCount() > 0 => getIdOfToken(tokenAddress) < getReserveCount()) && (getReserveCount() == 0 => getIdOfToken(tokenAddress) == 0)
    {
        preserved removeReserve(address t) {
          require t == tokenAddress;
        }
    }