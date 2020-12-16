#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc explanation->start
# 这道题最容易的做法就是将数组转为数字，加1后再转为数组，这种解决方案太不AC了，肯定不能这么干不能这么干。
#
# 解法主要分两种情况考虑：
#  - 第一种情况：当数组末尾数字小于9时，加1之后直接返回数组即可。
#  - 第二种情况：当数据末尾数字等于9时，加1后需要往前进一位，因此需要从后往前遍历输入，因为前面的数也可能有进位的情况。
# 将两种情况合并起来的思路就是寻找一个进位符，当这个进位符不为0的时候即时可进位，需要继续遍历；当这个进位符为0的时候，则不需要进位，返回即可。
# 特殊情况是整个数组全为9的时候，也就意味着全部都需要进位，所以在循环结束的时候判断进位符是否要进位，如果需要进位，此时数组中全为0，则需要再数组的前面插入1。
# 
# @lc explanation->end

# @lc complexity->start
# - 时间复杂度：
#   - 最好的情况：也就是第一种情况，数组末尾数字小于9，时间复杂度为O(1)
#   - 最坏的情况：也就是数组中全为9时，需要遍历整个数组进位，时间复杂度为O(n)
# - 空间复杂度：整个过程中用到了一个进位符，空间复杂度为O(1)
# @lc complexity->end

# @lc code=start

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curry = 1
        for i in range(len(digits) - 1, -1, -1):
            if curry == 0:
                return digits
            digits[i] = digits[i] + curry
            curry = digits[i] / 10
            digits[i] = int(digits[i] % 10)
        if curry == 1:
            digits.insert(0, 1)
        return digits
# @lc code=end

