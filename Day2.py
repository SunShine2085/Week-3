# Writing functions
# Chris Courville
# 7/3/2023


# def header(text, surround):
#     length = len(text) + 4
#     print(surround * length)
#     print(surround,text,surround)
#     print(surround * length)

# header("Chris is going to be super succesful in life", "$")
# header("The world is my oyster","^")
# header("I love living","@")

# Function problems

def absolute_difference(x,y):
    diff = abs(x-y)
    return diff

def pyramid(char, n):
    for i in range(1, n + 1):
        print(char * i)


def main():
    print("difference 5 10", absolute_difference(5,10) == 5 )
    print("difference 10 5", absolute_difference(10,5) == 5)
    print("difference 5 10", absolute_difference(200,-200) == 400)

    print('pyramid("*", 2)')
    pyramid("*", 2)

    print('pyramid("+", 5)')
    pyramid("+", 5)

    print('pyramid("x", 10)')
    pyramid("x", 10)

main()

# def is_even(n):
#     if (n % 2) == 0:
#         print(even)
#     else:
#         print("The number is odd")
#
# is_even(3)

# def calculate_total(meal, tax_rate, tip_rate):
#     print((meal * (1 + tip_rate)) * (1 + (tax_rate)))
#
# calculate_total(53.48, .07, .18)

# def hey(x):
#     print(x**2)
#
# def main():
#     hey(5)
#     hey(0)
#     hey(-3)
#
# main()


# def there(n):
#     if n>=0:
#         print(2**n)
#     else:
#         print("0")
#
# def main():
#     there(5)
#     there(0)
#     there(3)
#     there(-2)
#     there(-6)
#
# main()

def are_we(n, phrase):
    for i in range(1, n + 1):
        print("Are we", phrase, "yet?")
def main():
    are_we(2,"there")
    are_we(3,"50")
    are_we(1,"")
    are_we(0,"hey!")
main()




