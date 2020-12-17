#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc explanation->start
# 1.中心扩展发
# 遍历S字符串，对每一个字符双向搜索先找到为最短距离，由于题中说C字符在S中必然存在，所以不必关心搜不到的问题。
# 在Python中需要注意的是序列到边界后不会产生数组越界的情况，而是成环，从另外一端继续搜索。
# 因此需要处理边界的情况
#
# @lc explanation->end

# @lc complexity->start
# - 时间复杂度：双层循环因此是O(n^2)
# - 空间复杂度：使用到了list，因此是O(n)
# @lc complexity->end

# @lc explanation->start
# 2.最小数组
# 对于每个字符S[i]，分别找到S[i]距离左边和右边最近的C的距离，去最小值。
# 方法：
#   - 第一步：从左向右遍历，记录上一个出现的C的位置prev，每个字符S[i]的最近距离是i - prev
#   - 第二步：从右向左遍历，记录上一个出现的C的位置prev，每个字符S[i]的最近距离是prev - i
#
# @lc explanation->end

# @lc complexity->start
# - 时间复杂度：两次循环O(n)
# - 空间复杂度：用到了list存最短距离O(n)
# @lc complexity->end

# @lc code=start

# @lc code=start
# 1.中间扩展法
# class Solution:
#     def shortestToChar(self, S: str, C: str) -> List[int]:
#         distances = list()
#         for i in range(len(S)):
#             distance = 0
#             while True:
#                 left = i - distance
#                 right = i + distance
#                 if left < 0:
#                     left = 0
#                 if right > len(S) - 1:
#                     right = len(S) - 1
#                 if S[left] == C or S[right] == C:
#                     break
#                 distance += 1
#             distances.append(distance)
#         return distances

# 2.最小数组
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf') #最大的数值
        ans = [ 0 for i in range(len(S))]
        for i in range(len(S)):
            if S[i] == C:
                prev = i
            ans[i] = i - prev
        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans

# @lc code=end
