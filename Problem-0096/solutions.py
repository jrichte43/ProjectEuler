
__problem_title__ = "Su Doku"
__problem_url___ = "https://projecteuler.net/problem=96"
__problem_description__ = "Su Doku (Japanese meaning ) is the name given to a popular puzzle " \
                          "concept. Its origin is unclear, but credit must be attributed to " \
                          "Leonhard Euler who invented a similar, and much more difficult, " \
                          "puzzle idea called Latin Squares. The objective of Su Doku puzzles, " \
                          "however, is to replace the blanks (or zeros) in a 9 by 9 grid in such " \
                          "that each row, column, and 3 by 3 box contains each of the digits 1 " \
                          "to 9. Below is an example of a typical starting puzzle grid and its " \
                          "solution grid. A well constructed Su Doku puzzle has a unique " \
                          "solution and can be solved by logic, although it may be necessary to " \
                          "employ "guess and test" methods in order to eliminate options (there " \
                          "is much contested opinion over this). The complexity of the search " \
                          "determines the difficulty of the puzzle; the example above is " \
                          "considered because it can be solved by straight forward direct " \
                          "deduction. The 6K text file, (right click and 'Save Link/Target " \
                          "As...'), contains fifty different Su Doku puzzles ranging in " \
                          "difficulty, but all with unique solutions (the first puzzle in the " \
                          "file is the example above). By solving all fifty puzzles find the sum " \
                          "of the 3-digit numbers found in the top left corner of each solution " \
                          "grid; for example, 483 is the 3-digit number found in the top left " \
                          "corner of the solution grid above."

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

