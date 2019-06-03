#UTILITY DRIVER FOR math_drill.py

#horizontal line function
#input length
#output line
def horizontal_line(integer):
    print('*' * integer)
#vertical line function
#input shift and length
#output line
def vertical_line(shift,height):
    for x in range(0,height):
        print(' ' * shift, '*', sep='')
#two vertical lines
#input height and width
#output two vertical lines
def two_vertical_lines(height,width):
    for x in range(0,height):
        print('*', ' ' * (width - 2), '*', sep='')
#function prints 0
#input width
#output number
def number_0(width):
    horizontal_line(width)
    two_vertical_lines(3,width)
    horizontal_line(width)
#function prints 1
#input width
#output number
def number_1(width):
    vertical_line(width-1,5)
#function prints 2
#input width
#output number
def number_2(width):
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)
#function prints 3
#input width
#output number
def number_3(width):
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
#function prints 4
#input width
#output number
def number_4(width):
    two_vertical_lines(2,width)
    horizontal_line(width)
    vertical_line(width-1,2)
#function prints 5
#input width
#output number
def number_5(width):
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
#function prints 6
#input width
#output number
def number_6(width):
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)
#function prints 7
#input width
#output number
def number_7(width):
    horizontal_line(width)
    vertical_line(width-1,4)
#function prints 8
#input width
#output number
def number_8(width):
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)
#function prints 9
#input width
#output number
def number_9(width):
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)
    vertical_line(width-1,2)
#function prints plus sign
#input width
#output sign
def plus(width):
    vertical_line(int((width-1)/2),2)
    horizontal_line(width)
    vertical_line(int((width-1)/2),2)
#function prints minus sign in a 5 height area.
#input width
#output sign
def minus(width):
    for x in range (0,4):
        if x != 2:
            print()
        else:
            horizontal_line(width)
#mulptiply sign function
#input width
#output sign
def star(width):
    two_vertical_lines(1,width)
    vertical_line(width // 2,1)
    horizontal_line(width)
    vertical_line(width //2, 1)
    two_vertical_lines(1,width)
#divide sign function
#input width
#output sign
def slash(width):
    dash = width // 5
    print(' ' * dash * 4, end = '')
    horizontal_line(width - 4 * dash)
    print(' ' * dash * 3, end = '')
    horizontal_line(dash)
    print(' ' * dash * 2, end = '')
    horizontal_line(dash)
    print(' ' * dash, end ='')
    horizontal_line(dash)
    horizontal_line(dash)
#Check Answer function
#input numbers, answer, operator
#output boolean
def check_answer(num1, num2, ans, op):
    if op == '+':
        return ans == (num1 + num2)
    if op == '-':
        return ans == (num1 - num2)
    if op == '*':
        return ans == (num1 * num2)
    if op == '/':
        return ans == (num1 / num2)
#function to run the closing portion of the program if the person did not use drill mode
#input is all the accumulators
#output is the full closing statements with statistics
def final_stats(q_add,c_add,q_sub,c_sub,q_mul,c_mul,q_div,c_div):
    print()
    print('Thanks for playing!')
    print()
    print('You got',c_add+c_sub+c_mul+c_div, 'out of', q_add+q_sub+q_mul+q_div,'correct!')
    if c_add+c_sub+c_mul+c_div == q_add+q_sub+q_mul+q_div:
        print('WOW! You got all the questions right! That\'s 100%')
    print()
    print('--- Your Detailed Performance ---')
    print()
    if q_add != 0:
        print('Total addition problems presented:', q_add)
        print('Correct addition problems: ', c_add, ' (',format(float(c_add*100/q_add),'.1f'),'%)',sep ='')
    elif q_add == 0:
        print('No addition questions presented')
    print()
    if q_sub != 0:
        print('Total subtraction problems presented:', q_sub)
        print('Correct subtraction problems: ', c_sub, ' (',format(float(c_sub*100/q_sub),'.1f'),'%)',sep ='')
    elif q_sub == 0:
        print('No subtraction questions presented')
    print()
    if q_mul != 0:
        print('Total multiplication problems presented:', q_mul)
        print('Correct multiplication problems: ', c_mul, ' (',format(float(c_mul*100/q_mul),'.1f'),'%)',sep ='')
    elif q_mul == 0:
        print('No multiplication questions presented')
    print()
    if q_div != 0:
        print('Total division problems presented:', q_div)
        print('Correct division problems: ', c_div, ' (',format(float(c_div*100/q_div),'.1f'),'%)',sep ='')
    elif q_div == 0:
        print('No division questions presented')
#drill final stats printout
#input is all the accumulators
#output is the statisitcs and closing statements for drill mode
def final_drill(q_add,c_add,q_sub,c_sub,q_mul,c_mul,q_div,c_div):
    print()
    print('Thanks for playing!')
    print()
    print('This was drill mode')
    print()
    print('--- Your Performance ---')
    print()
    if q_add != 0:
        print('Total addition problems presented:', q_add)
        print('# of extra attempts needed: ', c_add-q_add,sep ='',end=' ')
        if c_add-q_add == 0:
            print('(perfect!)')
    elif q_add == 0:
        print('No addition questions presented')
    print()
    if q_sub != 0:
        print('Total subtraction problems presented:', q_sub)
        print('# of extra attempts needed: ', c_sub-q_sub,sep ='',end=' ')
        if c_sub-q_sub == 0:
            print('(perfect!)')
    elif q_sub == 0:
        print('No subtraction questions presented')
    print()
    if q_mul != 0:
        print('Total multiplication problems presented:', q_mul)
        print('# of extra attempts needed: ', c_mul-q_mul,sep ='',end=' ')
        if c_mul-q_mul == 0:
            print('(perfect!)')
    elif q_mul == 0:
        print('No multiplication questions presented')
    print()
    if q_div != 0:
        print('Total division problems presented:', q_div)
        print('# of extra attempts needed: ', c_div-q_div,sep ='',end=' ')
        if c_div-q_div == 0:
            print('(perfect!)')
    elif q_div == 0:
        print('No division questions presented')
