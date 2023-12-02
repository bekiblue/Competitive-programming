class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False
    rev = 0
    cur = x
    while cur:
      rev = rev * 10 + cur % 10
      cur //= 10 
    return rev == x