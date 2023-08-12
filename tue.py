multiplication_list = []
# def multiply(digit):
#     for number in range(1, 13):
#         multiplication = digit * number
#         multiplication_list.append(multiplication)
#     return multiplication_list
# print(multiply(3))


given_list = [1, 2, 3, 4, 5, 6]
def multiple(passing):
    intializer = 1
    for number in given_list:
        intializer = number * intializer
    return intializer
print(multiple(given_list))