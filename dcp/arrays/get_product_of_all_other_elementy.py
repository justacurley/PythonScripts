# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# Input [1,2,3,4,5]
# Output [120,60,40,30,24]
# Input [3,2,1]
# Output [2,3,6]
# with division

from sys import prefix
import numpy
nums1 = [1,2,3,4,5]
def products1(nums):
    # Get the product of all integers in the array, then divide by the current integer
    prod = numpy.prod(nums)
    for i in range(len(nums)):
        print(prod / nums[i])
products1 (nums1)

# without division
def products2(nums):
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    print(prefix_products)

    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    print(suffix_products)
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(
                prefix_products[i-1] * suffix_products[i+1]
            )
    print(result)
    return result
products2 (nums1)

