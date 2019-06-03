#while loop for captive user input
allow_in = 0
while allow_in == 0:
    user_in = input('Input number to test prime numbers up to. Greater than 9 please. ')
    if user_in.isnumeric():
        if int(user_in) < 0:
            print('That\'s a negative number! Please enter a value greater than 9. Please try again.')
            print()
        elif int(user_in) < 10:
            print('That\'s too little! Please use a value greater than 9. Please try again.')
            print()
        else:
            allow_in += 1
    else:
        print('That\'s not an integer!')
# Create the List for Prime Number Positions:
list_stat = 0
prime_list = []
while list_stat != int(user_in) + 1:
    if list_stat < 2:
        prime_list += ['N']
    else:
        prime_list += ['P']
    list_stat += 1
print('Your range is from 0 to ', user_in,'. Processing will complete shortly. Please be patient.', sep='')
print()
#testing for the primes and adjusting as necessary
for x in range(2, int(user_in)//2 +1):
    for y in range (2, int(user_in)+1):
        if prime_list[x]=='P':
            if prime_list[y]=='P':
                if y != x:
                    if y % x == 0:
                        prime_list[y] = 'N'

#create the prime NUMBERS list from the p/N
prime_num = []
#identify the values of the prime numbers:
for z in range(0,int(user_in)+1):
    if prime_list[z] == 'P':
        prime_num += [z]
#identify the largest prime
prime_len = len(prime_num)
large_len = prime_num[prime_len - 1]
#print out finished statement
print('Processing is complete! The prime numbers in your range are:')
#line print is a printout accumuator that will reset in the for loop when it hits 9, when we need a line break
line_print = 0
print()
#print out the prime numbers in 10 columns
for a in range (0, prime_len):
    if line_print == 9:
        print(format(str(prime_num[a]),'>' + str(len(str(large_len))) + 's'))
        line_print -= 9
    else:
        print(format(str(prime_num[a]),'>' + str(len(str(large_len))) + 's'), end = '  ')
        line_print += 1
    
