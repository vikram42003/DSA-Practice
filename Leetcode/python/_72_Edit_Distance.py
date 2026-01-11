class Solution:
    # DP (Bottom Up) - Time = O(n * m) - Space = O(m)
    # When we compress the dp we keep 1 row at a time so prevRow is m + 1, for base case of m'th row we compute it when initializing it
    # and for the n'th col we calculate it at runtime within the loop by setting the new row (filled with 0s) m'th col as n - i
    # Then the rest can remain the same
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prevRow = [m - j for j in range(m + 1)]

        for i in range(n - 1, -1, -1):
            curRow = [0] * (m + 1)
            curRow[m] = n - i
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    curRow[j] = prevRow[j + 1]
                else:
                    curRow[j] = min(
                        curRow[j + 1] + 1,
                        prevRow[j] + 1,
                        prevRow[j + 1] + 1
                    )
            prevRow = curRow

        return prevRow[0]
    
    # DP (Bottom Up) (LCS Pattern) - Time = O(n * m) - Space = O(n * m)
    # The state will be dp[n + 1][m + 1] where each element is the min operations we need to perform to convert word1 into word2
    # Thus the base case will be, if both word1 and word2 are empty then it'll take 0 operations, if word1 has n chars and word2
    # has 0 then it'll be len(n) operations since we'll have to delete each element, same if word1 empty word2 m chars except
    # we'll be inserting len(m) chars, so fill the extra row and col with that
    # 
    # Then iterate backwards and if word1[i] == word2[j], move both i and j and we dont have to add 1 here since no oepration
    # is required, but if its not equal then perform all 3 actions at this index and take the min
    # 
    # We'll do a + 1 as the cost to do any of these 3 actions
    # INSERT: if we insert a character then the i pointer will remain same since we imagine we
    # inserted at that spot so the next character to consider will be where i already points at
    # and j will move since that character is not converted
    # DELETE: if we delete then i will move because we deleted the i character we were checking
    # and j will remain the same because that deletion doesnt mean that j was converted, we're
    # just gonna check the next one cause maybe next one will match j
    # REPLACE: on replace we move both i and j because now both characters are converted and will
    # match
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        x = 0
        for i in range(n, -1, -1):
            dp[i][m] = x
            x += 1

        x = 0
        for j in range(m, -1, -1):
            dp[n][j] = x
            x += 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        dp[i][j + 1] + 1,  # Insert
                        dp[i + 1][j] + 1,  # Delete
                        dp[i + 1][j + 1] + 1,  # Replace
                    )

        return dp[0][0]
