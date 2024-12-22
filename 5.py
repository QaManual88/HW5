import keyword

name = input("Enter a variable name: ")


if name in keyword.kwlist:
    print(False)
else:

    if name[0].isdigit():
        print(False)
    else:

        if name.count('_') > 1:
            print(False)
        else:
           
            valid = True
            for char in name:
                if not (char.islower() or char.isdigit() or char == '_'):
                    valid = False
                    break
            print(valid)
