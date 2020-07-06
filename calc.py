class Calc:
    def __init__(self, *nums):  # initialising our class
        self.nums = nums

    def multiply(self, *nums):
        result = nums[0]
        for num in nums[1:]:
            result *= num
        return result

    def divide(self, *nums):
        result = nums[0]
        for num in nums[1:]:
            result /= num
        return result

    def modulo(self, *nums):
        if len(nums) > 2:  # Modulo can only be performed with 2 numbers
            return print("you have chosen too many numbers for this function")
        elif (nums[0] % nums[1] == 0):
            return True
        else:
            return False

    def addition(self, *nums):
        result = 0
        for num in nums:
            result += num
        return result

    def subtraction(self, *nums):
        result = nums[0]
        for num in nums[1:]:
            result -= num
        return result



calc = Calc()
calc.addition(2, 2)