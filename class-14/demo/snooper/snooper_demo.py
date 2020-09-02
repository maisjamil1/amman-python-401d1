import pysnooper

@pysnooper.snoop()
def print_square_of_nums_list(nums):
    square = 0
    for num in nums:
        square = num ** 2
        print(f"num: {num}, square: {square}")

print_square_of_nums_list([1,2,3,4,5])
