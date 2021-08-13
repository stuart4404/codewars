# digital root


def digitalRoot(number):
    
    # set add tool too 0
    addper = 0



    while number >= 10:
        number = sum(int(digit) for digit in str(number))
        addper +=1

    print(addper)
    print(number)


digitalRoot(16)