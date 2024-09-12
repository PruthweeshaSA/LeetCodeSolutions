op_dict = {0:1,1:1,2:2}
mod_base = 10**9 + 7

class Solution:
    def numTilings(self, n: int) -> int:
        #return numTilingsFunction(n)
        if n in op_dict:
            return op_dict[n]
        if n-1 in op_dict:
            op_dict[n] = ( 2 * op_dict[n-1] + op_dict[n-3] ) % mod_base
            return  op_dict[n]
        op_dict[n] = ( 2 * self.numTilings(n-1) + op_dict[n-3] ) % mod_base
        return op_dict[n]
        
        