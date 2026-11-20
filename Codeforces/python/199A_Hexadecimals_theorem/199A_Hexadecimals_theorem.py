import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    n = int(input().strip())

    fibNums = getFibNumsUptoN(n)
    m = len(fibNums)
    
    sum = 0
    res = []
    # Since we know the depth of the tree, we're using nested loops instead of recursive backtracking
    for i in range(m - 1, -1, -1):
        sum += fibNums[i]
        res.append(fibNums[i])
        
        if sum <= n:
            for j in range(i, -1, -1):
                sum += fibNums[j]
                res.append(fibNums[j])
                
                if sum <= n:
                    for k in range(j, -1, -1):
                        sum += fibNums[k]
                        res.append(fibNums[k])
                        
                        if sum == n:
                            print(*res)
                            return
                        
                        sum -= fibNums[k]
                        res.pop()
                
                sum -= fibNums[j]
                res.pop()
        
        sum -= fibNums[i]
        res.pop()
    
    print("I'm too stupid to solve this problem")

def getFibNumsUptoN(n):
    arr = [0, 1]
    
    num = arr[-1] + arr[-2]
    while num < n:
        arr.append(num)
        num += arr[-2]
    
    return arr

def solution():
    solve()

if __name__ == "__main__":
    solution()
