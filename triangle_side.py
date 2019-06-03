print('Valid Triangle Tester')
#ask for coordinates 1
point_1x = float(input('Enter Position #1 - x position: '))
point_1y = float(input('Enter Position #1 - y position: '))
#coordinates 2
point_2x = float(input('Enter Position #2 - x position: '))
point_2y = float(input('Enter Position #2 - y position: '))
#coordinates 3
point_3x = float(input('Enter Position #3 - x position: '))
point_3y = float(input('Enter Position #3 - y position: '))
print()
#distance 1 and 2 (forms side a)
side_a = (((point_1x - point_2x)**2 + (point_1y - point_2y)**2))**0.5
#distance 2 and 3 (forms side b)
side_b = (((point_2x - point_3x)**2 + (point_2y - point_3y)**2))**0.5
#distance 1 and 3 (forms side c)
side_c = (((point_1x - point_3x)**2 + (point_1y - point_3y)**2))**0.5
#print side lenghts
print('The length of each side of your test shape is:')
print('Side 1:', format(side_a,'.2f'))
print('Side 2:', format(side_b,'.2f'))
print('side 3:', format(side_c,'.2f'))
print()
#sums of sides
side_ab = side_a + side_b
side_bc = side_b + side_c
side_ac = side_a + side_c
#creating variables for if statements
check_ab_c = 0
check_bc_a = 0
check_ac_b = 0
#if statements to check
if side_ab > side_c:
    check_ab_c = 1
else :
    print('This is not a valid triangle')
if side_bc > side_a:
    check_bc_a = 1
else :
    print('This is not a valid triangle')
if side_ac > side_b:
    check_ac_b = 1
else :
    print('This is not a valid triangle')
#sum the checks and check again if valid
check = check_ab_c + check_bc_a + check_ac_b
if check == 3:
    print('This is a valid triangle!')

