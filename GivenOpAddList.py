
##Given a list of integers nums, a string op representing either "+", "-", "/", or "*", 
##and an integer val, perform the operation on every number in nums with val and return the result.

Note: "/" is integer division.
class Solution:
    def solve(self, nums, op, val):
        nu = list()
        if op == "+":
            for num in nums:
                num = num + val
                nu.append(num)
            return nu

        elif op == "-":
            for num in nums:
                num = num - val
                nu.append(num)
            return nu
        elif op == "/":
            for num in nums:
                num = num // val
                nu.append(num)
            return nu
        elif op == "*":
            for num in nums:
                num = num * val
                nu.append(num)
            return nu
