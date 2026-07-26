package leetcode

import "sort"

// HashMap and Sort - Time = O(n * k log k) - Space = O(log n)
func groupAnagrams(strs []string) [][]string {
    mp := make(map[string][]string, len(strs))

    for _, s := range strs {
        b := []byte(s)

        sort.Slice(b, func(i, j int) bool {
            return b[i] < b[j]
        })
        sortedS := string(b)

        mp[sortedS] = append(mp[sortedS], s)
    }

    result := make([][]string, 0, len(mp))
    for _, v := range mp {
        result = append(result, v)
    }
    return result
}

// HashMap and Freq Count - Time = O(n * k) - Space = O(k)
func groupAnagrams2(strs []string) [][]string {
    mp := make(map[[26]int][]string, len(strs))

    for _, s := range strs {
        freq := [26]int{}
        for _, c := range s {
            freq[c - 'a'] += 1
        }
        mp[freq] = append(mp[freq], s)
    }

    result := make([][]string, 0, len(mp))
    for _, v := range mp {
        result = append(result, v)
    }
    return result
}
