class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dig_sum=0
        dig_prod=1
        x=n

        while x:
            dig=x%10
            x=x//10
            dig_sum+=dig
            dig_prod*=dig
        
        return n%(dig_sum+dig_prod)==0
