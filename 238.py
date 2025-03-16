from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products: List[int] = [1] * length

        prefix_product, suffix_product = 1, 1
        left, right = 1, length - 2

        while left < length:
            prefix_product *= nums[left - 1]
            products[left] *= prefix_product
            left += 1

            suffix_product *= nums[right + 1]
            products[right] *= suffix_product
            right -= 1

        return products
