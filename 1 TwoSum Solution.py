class Solution(object):
    def twoSum(self, nums, target):
        # This is to create a dictionary to store numbers and their corresponding indices
        number_map = {}

        # This is to loop through the array
        for i, num in enumerate(nums):
            # This is to calculate the difference between the target and the current number
            diff = target - num

            # This is to check if the value of diff exists in the dictionary
            if diff in number_map:
                # This is if the difference exists, return the indices of the current number and the number that adds up to the target
                return [number_map[diff], i]
            
            # If the difference does not exist, add the current number and its index to the dictionary
            number_map[num] = i

        # This is if no two numbers add up to the target, return None
        return None