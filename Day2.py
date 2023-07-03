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

# def absolute_difference(x,y):
#     print(abs(x-y))
#
# absolute_difference(5,10)
# absolute_difference(10,5)
# absolute_difference(200,-200)


def pyramid(char, n):
    for i in range(1, n + 1):
        print(char * i)


def main():
    print('pyramid("*", 2)')
    pyramid("*", 2)

    print('pyramid("+", 5)')
    pyramid("+", 5)

    print('pyramid("x", 10)')
    pyramid("x", 10)

main()
