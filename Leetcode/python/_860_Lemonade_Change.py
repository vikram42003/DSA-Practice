from typing import List


class Solution:
    # Unoptimized Greedy - Time = O(n) - Space = O(1)
    # Time = O(n) roughly, since while loop wil run a maximum of 3 times cause max(bills) == 20
    def lemonadeChange(self, bills: List[int]) -> bool:
        # [0] = $5   [1] = $10   [2] = $20
        cash_register = [0, 0, 0]

        for bill in bills:
            match bill:
                case 5:
                    cash_register[0] += 1
                case 10:
                    cash_register[1] += 1
                case 20:
                    cash_register[2] += 1
            
            change = bill - 5
            
            while True:
                if change >= 20 and cash_register[2] > 0:
                    change -= 20
                    cash_register[2] -= 1
                elif change >= 10 and cash_register[1] > 0:
                    change -= 10
                    cash_register[1] -= 1
                elif change >= 5 and cash_register[0] > 0:
                    change -= 5
                    cash_register[0] -= 1
                else:
                    break
            
            if change > 0: return False

        return True
    
    # Greedy - Time = O(n) - Space = O(1)
    
    # Possible cases -
    # customer pays $5 = $5++ $0--
    # customer pays $10 = $10++ $5--
    # customer pays $20 = $20++ $10-- $5-- or $20++ $5 -= 3
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -= 1
                tens += 1
            elif tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
            
            if fives < 0 or tens < 0:
                return False
            
        return True
    
test = Solution()
# ans = False
bills = [5,5,10,10,20]
print(test.lemonadeChange(bills))
