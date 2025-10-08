from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def rec(i, q, size, crossedOut, curr):
            if q <= 0:
                res.append(curr[:])
                return
            
            if (i >= size and q > 0) or i + q != size:
                return
            
            temp = ["."] * size
            pos = -1
            
            for j in range(size):
                if all(j not in sublist for sublist in crossedOut):
                    pos = j
                    temp[j] = "Q"
                    curr.append("".join(temp))
                    
                    rec(i + 1, q - 1, size, self.updateCrossedOut(crossedOut, j), curr)
                    
                    temp[j] = "."
                    curr.pop()
                
            if pos == -1:
                curr.append("".join(temp))
                
                rec(i + 1, q, size, self.updateCrossedOut(crossedOut, -1), curr)
                
                curr.pop()
        
        rec(0, n, n, [set(), set(), set()], [])
        
        return res
    
    def updateCrossedOut(self, crossedOut, j):
        copy = []
        temp = set()
        for c in crossedOut[0]:
            temp.add(c - 1)
        copy.append(temp)
        
        copy.append(set(crossedOut[1]))

        temp = set()
        for c in crossedOut[2]:
            temp.add(c + 1)
        copy.append(temp)
        
        if j != -1:
            copy[0].add(j - 1)
            copy[1].add(j)
            copy[2].add(j + 1)
            
        return copy
    
    
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     # Track crossed out spots in an array of sets where [[decrement set], [remain same set], [increment set]]
    #     crossedOut = [set(), set(), set()]
    #     res = []

    #     # We start with n size initially but the abort logic does +1 at start so we do -1 here to offset that
    #     size = n - 1
    #     # If we are unable to place the queens with the board of size "size" then abort current rec func and run another rec func with increased size
    #     abort = True

    #     def rec(i, q, size):
    #         nonlocal abort
    #         # Exit the function entirely if abort is true
    #         if abort:
    #             return

    #         # Exit out if all queens have been placed
    #         if q <= 0:
    #             return
            
    #         # Exit out with abort true if we could not place all the queens with this board size
    #         if i >= size and q > 0:
    #             abort = True
    #             return
            
    #         curr = ["."] * size
    #         pos = -1

    #         for j in range(len(curr)):
    #             # If this is the first iteration of first level depth then place the queen on the second spot instead of first
    #             # This pattern seems most efficient
    #             if len(res) == 0 and j == 0:
    #                 continue
    #             # Place the queen in the first non crossed out position and save that position
    #             if j not in crossedOut[0] and j not in crossedOut[1] and j not in crossedOut[2]:
    #                 pos = j
    #                 curr[j] = "Q"
    #                 break
            
    #         # Update the crossed out spots
    #         temp = set()
    #         for c in crossedOut[0]:
    #             temp.add(c - 1)
    #         crossedOut[0] = temp

    #         temp = set()
    #         for c in crossedOut[2]:
    #             temp.add(c + 1)
    #         crossedOut[2] = temp

    #         # If we did place a queen at this depth, then add it to the crossed out spots
    #         if pos != -1:
    #             crossedOut[0].add(pos - 1)
    #             crossedOut[1].add(pos)
    #             crossedOut[2].add(pos + 1)

    #         # Append to res
    #         res.append("".join(curr))

    #         # Recurse to move to the next level
    #         print("We did the thing")
    #         rec(i + 1, q - 1, size)

    #     while abort:
    #         res = []
    #         size += 1
    #         abort = False
    #         rec(0, n, size)

    #     return res


test = Solution()

# ans = ["Q"]
# n = 1
# print(test.solveNQueens(n))

# ans = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
n2 = 4
print(test.solveNQueens(n2))
