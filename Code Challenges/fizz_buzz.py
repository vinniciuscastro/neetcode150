"""
FizzBuzz is a classic programming challenge that involves printing numbers from 
1 to n, but with a twist:
- For multiples of 3, print "Fizz" instead of the number.
- For multiples of 5, print "Buzz" instead of the number.
Leetcode 1195
"""
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

    def fizz(self, i: int):
        print("fizz")

    def buzz(self, i: int):
        print("buzz")

    def fizzbuzz(self, i: int):
        print("fizzbuzz")

    def number(self, i: int):
        print(i)

    def run(self):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzz(i)
            elif i % 3 == 0:
                self.fizz(i)
            elif i % 5 == 0:
                self.buzz(i)
            else:
                self.number(i)
# Time complexity: O(n), where n is the input number
# Space complexity: O(1), since we are not using any additional data structures

fb = FizzBuzz(20)
fb.run()