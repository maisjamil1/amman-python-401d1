# factorial(4) ==> 4*3*2*1
# factorial(6) ==> 6*factorial(5)
# factorial(2) ==> 2 * factorial(1)
# factorial(1) ==> 1  BASE CASE


# base case
# recursive call

def factorial(n):
    # BASE CASE
    if n <= 1:
        return 1
    # RECURSIVE CALL
    return n * factorial(n-1)



    # 2 * factorial(1)
    #     1
    # 2 * 1 = 2


    # 4 * factorial(3)
    #     3 * factorial(2)
    #         2 * factorial(1)
    #             1
    # 4 * 3 * 2 * 1 = 24
