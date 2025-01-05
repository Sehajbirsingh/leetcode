class Solution:
    def maxLength(self, nums: List[int]) -> int:
        N= len(nums)
        L=1

        for left in range(N):
            g=l=p=nums[left]

            for right in range(left+1,N):
                x=nums[right]
                p*=x
                l=lcm(l,x)
                g=gcd(g,x)

                if p==l*g:
                    L=max(L,right-left+1)

        return L