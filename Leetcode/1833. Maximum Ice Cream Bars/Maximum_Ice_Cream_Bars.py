class Solution:

    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()

        count=0

        for c in costs:

            if c>coins:

                break

            else:

                coins-=c

                count+=1

        return count
