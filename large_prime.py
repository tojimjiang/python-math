#accumulator for validation
allow_in = 0
#while loop for captive input
while allow_in == 0:
    start_test = int(input('Start number: '))
    end_test = int(input('End number: '))
    if start_test < 0:
        print('Start and end must be positive. Try again.')
        print()
    elif end_test < 0:
        print('Start and end must be positive. Try again.')
        print()
    elif start_test > end_test:
        print('End number must be greater than start number. Try again.')
        print()
    else:
        allow_in += 1
        print()
#identify the longest length, don't need to adjuest the start test because that is the minimum
for a in range(start_test, end_test + 1):
    for b in range (2, end_test + 1):
        rem_length = a % b
        if rem_length == 0:
            if a == b:
                max_value = a
            else:
                break     
#accumulator for printing
line_print = 0
#testing primes engine
for x in range(start_test, end_test + 1):
    for y in range (2, end_test + 1):
        remainder = x % y
        if remainder == 0:
            if x == y:
                line_print += 1
                if line_print == 10:
                    print(format(str(x),'>' + str(len(str(max_value))) + 's'))
                    line_print -= 10
                else:
                    print(format(str(x),'>' + str(len(str(max_value))) + 's'), end = '  ')
            else:
                break
