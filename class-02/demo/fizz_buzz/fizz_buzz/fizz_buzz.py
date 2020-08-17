a = 6

# def fizz_buzz(num):
#     if num%5 == 0 and num%3 == 0:
#         return 'FizzBuzz'
#     elif num%5 == 0:
#         return 'Buzz'
#     elif num%3 == 0:
#         return 'Fizz'
#     else:
#         return num


# def fizz_buzz(num):
#     output = ''
#     if num%3 == 0:
#         output = 'Fizz'
#     if num%5 == 0:
#         output += 'Buzz'

#     if output == '':
#         output = num

#     return output


def fizz_buzz(num):
    output = ''
    if not num%3:
        output = 'Fizz'
    if not num%5:
        output += 'Buzz'
    return output or num



def fizz_buzz_as_list(nums):
    # output = []
    # for num in nums:
    #     output.append(fizz_buzz(num))
    # return output
    return [fizz_buzz(num) for num in nums]
