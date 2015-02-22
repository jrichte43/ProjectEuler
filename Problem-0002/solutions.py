
__problem_title__ = "Even Fibonacci numbers"
__problem_url___ = "https://projecteuler.net/problem=2"
__problem_description__ = "Each new term in the Fibonacci sequence is generated by adding the " \
                          "previous two terms. By starting with 1 and 2, the first 10 terms will " \
                          "be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms " \
                          "in the Fibonacci sequence whose values do not exceed four million, " \
                          "find the sum of the even-valued terms."

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

