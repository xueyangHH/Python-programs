# Name: Xueyang Huang
# Date: Feb.5
# Class section: 02
# Name of the program: HuangXueyang_assign2_problem1

# ask the user for the initial investment
print('This program will project how much you can earn by investing money in a high-yield savings account over a 3 month period.')
print()
initial = float(input('To begin, enter how much money you would like to initially invest (i.e. 500): '))

# ask the user for the interest rate
rate = float(input('Next, enter your projected annual interest rate. For example, enter 5 for 5%: '))
nrate = rate * .01 / 12

# calculations for month 1
# compute interest earned for month 1
m1_interest = initial * nrate

# compute final balance for month 1
m1final = initial + m1_interest

# calculations for month 2
# compute interest earned for month 2
m2_interest = m1final * nrate

# compute final balance earned for month 2
m2final = m1final + m2_interest

# calculations for month 3
# compute interest earned for month 3
m3_interest = m2final * nrate

# compute final balance earned for month 3
m3final = m2final + m3_interest

# format the data
finitial = format(initial, '<21.2f')
fm1_interest = format(m1_interest, '<11.2f')
fm1final = format(m1final, '<14.2f')
fm2initial = format(m1final, '<21.2f')
fm2_interest = format(m2_interest, '<11.2f')
fm2final = format(m2final, '<14.2f')
fm3initial = format(m2final, '<21.2f')
fm3_interest = format(m3_interest, '<11.2f')
fm3final = format(m3final, '<14.2f')

# print out the everything
print()
print('------- Calculating --------')
print()

# format the title column
fmonth = format('Month', '6s')
fSB = format('Starting Balance', '21s')
finterest = format('Interest', '11s')
fEB = format('Ending Balance', '14s')

# print out result
print(fmonth+fSB+finterest+fEB)
print(format('1', '6s') + finitial + fm1_interest + fm1final)
print(format('2', '6s') + fm2initial + fm2_interest + fm2final)
print(format('3', '6s') + fm3initial + fm3_interest + fm3final)

# possible problem this program could cause: if the user enter a number that involves digits more than how much the formatted space can hold, the program would fail to keep the numbers aligned with the title words.
# i.e. If the user enter the initial number 1*10^12, and any integer > 0 for rate, the number of the interest would push the number of ending balance one digit to the right.
