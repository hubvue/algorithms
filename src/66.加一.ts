/*
 * @lc app=leetcode.cn id=66 lang=typescript
 *
 * [66] 加一
 */

// @lc code=start
function plusOne(digits: number[]): number[] {
  let curry = 1
  for(let i = digits.length - 1; i >= 0; i --) {
    if (curry === 0) {
      return digits
    }
    digits[i] = digits[i] + curry
    curry = digits[i] / 10
    digits[i] = Math.floor(digits[i] % 10)
  }
  if(curry === 1){
    digits.unshift(1)
  }
  return digits
};
// @lc code=end

