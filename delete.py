class Solution:

	def lis(self, A):
		max_length = [0] * len(A)
		for i in range(len(A)):
			length = 0
			for j in range(i):
				if A[i] >= A[j]:
					length = max(length, max_length[j])
			max_length[i] = length + 1
			print(A)
			print(max_length)
			print("========================")

		return max_length[-1]


print(Solution().lis([30, 92, 22, 48, 52, 64, 92, 50, 85, 38, 97, 15, 14, 75, 59, 46, 74, 6, 95, 67, 86, 88, 25, 49, 67, 69, 50, 99, 83, 49, 60, 6, 90, 1, 50, 41, 57, 18, 36, 5, 44, 100, 23, 33, 52, 11, 46, 49, 34, 27, 77, 57, 93, 82, 38, 95, 6, 51, 100, 32, 11, 26, 50, 3, 55, 39, 84, 54, 44, 75, 76, 51, 21, 40, 28, 50, 30, 6, 84, 58, 76, 42, 35, 49, 98, 49, 13, 101, 3, 1, 60, 48, 99, 70]))