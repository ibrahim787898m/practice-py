# class Solution(object):
#     def fizzBuzz(self, n):
#         res = []
#         for i in range(1, n + 1):
#             if i % 15 == 0:
#                 res.append("FizzBuzz")
#             elif i % 5 == 0:
#                 res.append("Buzz")
#             elif i % 3 == 0:
#                 res.append("Fizz")
#             else:
#                 res.append(str(i))
# 
#         return res
# 
# class Solution(object):
#     def isPalindrome(self, x):
#         s = str(x)
#         rev = s[::-1]
#         
#         if s == rev:
#             return True
#         else:
#             return False
# 
# class Solution(object):
#     def reverse(self, x):
#         if x < 0:
#             s = str(x)[1:]
#             rev = s[::-1]
#             res = int(rev) * -1
#         else:
#             res = int(str(x)[::-1])
# 
#         if res < -2**31 or res > 2**31 - 1:
#             return 0
# 
#         return res
# 
# class Solution(object):
#     def vowelStrings(self, words, left, right):
#         vowels = ["a", "e", "i", "o", "u"]
#         count = 0
# 
#         for i in range(left, right + 1):
#             if words[i][0] in vowels and words[i][-1] in vowels:
#                 count += 1
# 
#         return count
# 
# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
# 
#         return sorted(s) == sorted(t)
# 
# class Solution(object):
#     def minimumDeletions(self, nums):
#         n = len(nums)
#         max_value = max(nums)
#         min_value = min(nums)
#         max_index = max(nums.index(max_value), nums.index(min_value))
#         min_index = min(nums.index(max_value), nums.index(min_value))
# 
#         front = max_index + 1
# 
#         back = n - min_index
# 
#         mix1 = (min_index + 1) + (n - max_index)
#         mix2 = (max_index + 1) + (n - min_index)
# 
#         return min(front, back, mix1, mix2)
# 
# class Solution(object):
#     def deleteDuplicates(self, head):
#         current == head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next == current.next.next
#             else:
#                 current == current.next
# 
#         return head
# 
# class Solution(object):
#     def isPalindrome(self, s):
#         s = ''.join(ch for ch in s if ch.isalnum())
#         s = s.lower()
# 
#         left = 0
#         right = len(s) - 1
# 
#         while left < right:
#             if s[left] != s[right]:
#                 return False
# 
#             left += 1
#             right -= 1
# 
#         return True

class Solution(object):
    def addDigits(self, num):
        while True:
            old = num
            new = 0
            for digit in map(int, str(old)):
                new += digit

            if new < 10:
                break
            else:
                num = new

        return new

if __name__ == "__main__":
    sol = Solution()
    res = sol.addDigits(38)
    print(res)

