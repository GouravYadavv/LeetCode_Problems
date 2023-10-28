class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a_count = e_count = i_count = o_count = u_count = 1
        for _ in range(1, n):
            a_count, e_count, i_count, o_count, u_count = \
                (e_count + i_count + u_count) % MOD, \
                (a_count + i_count) % MOD, \
                (e_count + o_count) % MOD, \
                i_count, \
                (i_count + o_count) % MOD
        return (a_count + e_count + i_count + o_count + u_count) % MOD