from typing import List

def maxPathSum(matrix: List[List[int]]) -> int:
    height = len(matrix)
    if height == 0:
        return 0

    # Initialize the dp array. Set the last row equal to the last row of the input matrix
    dp = [[float('-inf')] * (i + 1) for i in range(height)]
    dp[-1] = matrix[-1]

    # Iterate from the bottom to the top
    for i in range(height - 2, -1, -1):
        for j in range(i + 1):
            # For each number, calculate the maximum sum of the path from the bottom to the number
            # Considers the current number and the maximum of the two possible numbers below (below, diagonally right)
            dp[i][j] = matrix[i][j] + max(
                dp[i + 1][j],  # Below
                dp[i + 1][j + 1] if j < i else float("-inf")  # Diagonally right
            )

    # The answer is the value in the first row
    return dp[0][0]

if __name__ == '__main__':
    matrix_1 = [[3],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3]]

    print("Maximum Path Sum for the first matrix:", maxPathSum(matrix_1))

    matrix_2 = [[75],
                [95, 64],
                [17, 47, 82],
                [18, 35, 87, 10],
                [20, 4, 82, 47, 65],
                [19, 1, 23, 75, 3, 34],
                [88, 2, 77, 73, 7, 63, 67],
                [99, 65, 4, 28, 6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

    print("Maximum Path Sum for the second matrix:", maxPathSum(matrix_2))

    # Initialize an empty list to hold all the rows
    matrix_3 = []

    # Open the file and read the data
    with open('0067_triangle.txt', 'r') as file:
        for line in file:
            # Convert each line to a list of integers
            numbers = list(map(int, line.split()))
            # Append the list of numbers to the 2D array
            matrix_3.append(numbers)

    print("Maximum Path Sum for the third matrix:", maxPathSum(matrix_3))


