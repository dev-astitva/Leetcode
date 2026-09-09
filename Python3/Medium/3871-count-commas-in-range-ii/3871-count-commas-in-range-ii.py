class Solution:
    def countCommas(self, n: int) -> int:
        return sum(max(0, n-i) for i in [999, 999_999, 999_999_999, 999_999_999_999, 999_999_999_999_999])