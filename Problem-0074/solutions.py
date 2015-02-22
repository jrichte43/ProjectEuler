
__problem_title__ = "Digit factorial chains"
__problem_url___ = "https://projecteuler.net/problem=74"
__problem_description__ = "The number 145 is well known for the property that the sum of the " \
                          "factorial of its digits is equal to 145: 1! + 4! + 5! = 1 + 24 + 120 " \
                          "= 145 Perhaps less well known is 169, in that it produces the longest " \
                          "chain of numbers that link back to 169; it turns out that there are " \
                          "only three such loops that exist: 169 → 363601 → 1454 → 169 871 → " \
                          "45361 → 871 872 → 45362 → 872 It is not difficult to prove that EVERY " \
                          "starting number will eventually get stuck in a loop. For example, 69 " \
                          "→ 363600 → 1454 → 169 → 363601 (→ 1454) 78 → 45360 → 871 → 45361 (→ " \
                          "871) 540 → 145 (→ 145) Starting with 69 produces a chain of five " \
                          "non-repeating terms, but the longest non-repeating chain with a " \
                          "starting number below one million is sixty terms. How many chains, " \
                          "with a starting number below one million, contain exactly sixty " \
                          "non-repeating terms?"

import timeit


class Solution():

    @staticmethod
    def solution1():
        pass

    @staticmethod
    def time_solutions():
        setup = 'from __main__ import Solution'
        print('Solution 1:', timeit.timeit('Solution.solution1()', setup=setup, number=1))


if __name__ == '__main__':
    s = Solution()
    print(s.solution1())
    s.time_solutions()

