answer = input('*You* This will be the answer. Select a number 10-49: ')
factor = 99 - int(answer)
num = input('*Player* pick any number from 50-99: ')
sum1 = int(num) + factor
sum2 = int(str(sum1)[1:]) + int(str(sum1)[0])
result = int(num) - sum2
print('I said the answer was', answer, 'and the calculation result is', result)
