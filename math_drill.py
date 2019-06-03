#Requires dot_display.py as utility module.

#This program does include, multiplication, division, drill mode, and detailed statistics (statistics by problem type)
#drill mode is optional

#question type accumulator
q_add = 0
q_sub = 0
q_mul = 0
q_div = 0
#answer type correct accumulator
c_add = 0
c_sub = 0
c_mul = 0
c_div = 0
#need random module
import random
#need the module created
import dot_display
#use input while loop for number of problems
allow_in = 0
while allow_in == 0:
    num_problems = int(input('How many problems would you like to attempt? 5-20: '))
    if num_problems < 21:
        if num_problems > 4:
            allow_in += 1
            break
    print('Invalid number, try again')
    print()
#use input while loop for width of numbers
while allow_in == 1:
    width = int(input('How wide do you wany your digits to be? 5-20: '))
    if width < 21:
        if width > 4:
            allow_in += 1
            break
    print('Invalid width, try again')
    print()
while allow_in == 2:
    drill = input('Would you like to activate \'drill\' mode? yes or no: ')
    if drill == 'yes':
        allow_in += 1
        break
    elif drill == 'no':
        allow_in += 1
        break
    else:
        print('Invalid input, try again')
#formating for prints
print()
print('Here we go!')
print()
#Maths Question Program Engine.
for x in range(0,num_problems):
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    rand_op = random.randint(0,3)
    if rand_op == 0:
        operator = '+'
    elif rand_op == 1:
        operator = '-'
    elif rand_op == 2:
        operator = '*'
    else:
        operator = '/'
        #check generated numbers result in integer
        while operator == '/':
            while number2 == 0:
                number2 = random.randint(0,9)
            if number1 % number2 != 0:
                number1 = random.randint(0,9)
                number2 = random.randint(0,9)
            else:
                break
    print('What is .....')
    #this barrage of if statements is the method I employed to print out the
    #characters needed in this program
    print()
    if number1 == 0:
        dot_display.number_0(width)
    elif number1 == 1:
        dot_display.number_1(width)
    elif number1 == 2:
        dot_display.number_2(width)
    elif number1 == 3:
        dot_display.number_3(width)
    elif number1 == 4:
        dot_display.number_4(width)
    elif number1 == 5:
        dot_display.number_5(width)
    elif number1 == 6:
        dot_display.number_6(width)
    elif number1 == 7:
        dot_display.number_7(width)
    elif number1 == 8:
        dot_display.number_8(width)
    elif number1 == 9:
        dot_display.number_9(width)
    else:
        print('Error - Graphics Printout Basic')
    print()
    if operator == '+':
        dot_display.plus(width)
        q_add += 1
    elif operator == '-':
        dot_display.minus(width)
        q_sub += 1
    elif operator == '*':
        dot_display.star(width)
        q_mul += 1
    elif operator == '/':
        dot_display.slash(width)
        q_div += 1
    else:
        print('Error - Graphics Printout -Signs')
    print()
    if number2 == 0:
        dot_display.number_0(width)
    elif number2 == 1:
        dot_display.number_1(width)
    elif number2 == 2:
        dot_display.number_2(width)
    elif number2 == 3:
        dot_display.number_3(width)
    elif number2 == 4:
        dot_display.number_4(width)
    elif number2 == 5:
        dot_display.number_5(width)
    elif number2 == 6:
        dot_display.number_6(width)
    elif number2 == 7:
        dot_display.number_7(width)
    elif number2 == 8:
        dot_display.number_8(width)
    elif number2 == 9:
        dot_display.number_9(width)
    else:
        print('Error - Graphics Printout Basic')
    print()
    #non drill question correction
    if drill == 'no':
        answer = int(input('= '))
        answer_check = dot_display.check_answer(number1, number2, answer, operator)
        if answer_check == 1:
            if operator == '+':
                c_add += 1
            elif operator == '-':
                c_sub += 1
            elif operator == '*':
                c_mul += 1
            elif operator == '/':
                c_div += 1
            print('Correct!')
        else:
            print('Sorry, that\'s not correct')
    #drill question re-attempt
    elif drill == 'yes':
        while drill == 'yes':
            answer = int(input('= '))
            if operator == '+':
                c_add += 1
            elif operator == '-':
                c_sub += 1
            elif operator == '*':
                c_mul += 1
            elif operator == '/':
                c_div += 1
            answer_check = dot_display.check_answer(number1, number2, answer, operator)
            if answer_check == 1:
                print()
                print('Correct!')
                print()
                break
            print('Sorry, that\'s not correct')
#This will call on the correct final statistics printout as drill mode is not the
#same as regular mode in terms of counting and output.            
if drill == 'no':
    dot_display.final_stats(q_add,c_add,q_sub,c_sub,q_mul,c_mul,q_div,c_div)
elif drill == 'yes':
    dot_display.final_drill(q_add,c_add,q_sub,c_sub,q_mul,c_mul,q_div,c_div)
