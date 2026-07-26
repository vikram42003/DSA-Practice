package leetcode

func ValidAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var seen [26]int

    for _, i := range s {
        seen[i - 97] += 1
    }

    for _, i := range t {
        if seen[i - 97] == 0 {
            return false
        }
        seen[i - 97] -= 1
    }

    return true
}
