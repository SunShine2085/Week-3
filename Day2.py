# Writing functions
# Chris Courville
# 7/3/2023


def header(text, surround):
    length = len(text) + 4
    print(surround * length)
    print(surround,text,surround)
    print(surround * length)

header("Chris is going to be super succesful in life", "$")
