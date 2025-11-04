'''
* author:  mibrahim0pu
'''


# Competitive Programming version
# import sys

# input = lambda: sys.stdin.readline().rstrip()
# print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + '\n')

# def main():
#     n, target = map(int, input().split())
#     nums = list(map(int, input().split()))

#     seen = {}

#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             print(seen[complement], i)
#             return
#         seen[num] = i

# if __name__ == "__main__":
#     main()


# LeetCode version
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num]  = i
        return []   

if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([3,2,4], 6)
    print(*res)
