# python-leetcode-solutions
# 10. Regular Expression Matching

**Difficulty:** Hard  
**Link:** https://leetcode.com/problems/regular-expression-matching/  
**Topic:** Dynamic Programming, String  

## Problem Summary
Implement regex matching with `.` (any single char) and `*` 
(zero or more of preceding char) that covers the entire string.

## Approach — Dynamic Programming
Build a 2D table `dp[i][j]` where each cell answers:
> "Does `s[:i]` match `p[:j]`?"

### Key Logic
- If `p[j-1] == '*'`: either skip it (zero times) or use it (if preceding char matches)
- If `p[j-1] == '.'` or direct match: carry over diagonal value

## Complexity
| | Complexity |
|---|---|
| Time | O(m × n) |
| Space | O(m × n) |

## Test Cases
```python
isMatch("aa", "a")        # False
isMatch("aa", "a*")       # True
isMatch("ab", ".*")       # True
isMatch("aab", "c*a*b")   # True
```
