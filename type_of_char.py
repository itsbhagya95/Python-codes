##To check the type of character entered from the keyboard

s=input('Enter any character:')
if s.isalnum():
    print('It is alphanumeric character')
    if s.isalpha():
        print('It is alphabet symbol')
        if s.islower():
            print('It is lowercase alphabet symbol')
        else:
            print('It is uppercase alphabet symbol')
    else:
        print('It is a digit')
elif s.isspace():
    print('It is space character')
else:
    print('It is nonspace special character')
### subham

