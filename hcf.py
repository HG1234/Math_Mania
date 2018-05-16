#for finding hcf of the numbers
factor1 = []
factor2 = []
factor3 = []
num1 = int(input('Enter First Number \n -->'))
num2 = int(input('Enter Second Number \n --'))
def hcf(num_1,num_2):

    if num_1 == num_2:
        print('The higest common factor is',num_2)
    elif num_1%num_2==0:
        print('the highst common factor is',num_2)
    elif num_2%num_1==0:
        print('The highes common factor is',num_1)
    elif num_2 % num_1 != 0 and num_1%num_2 != 0:
 		
        x = comparer(factor1,factor2)
        if x == []:
        	print('The highest common factor is 1')
        else :
        	print(x[-1])

def factor(num1,num2):
    global factor1 ,factor2
    for i in range(2,num1):
        if num1%i == 0 :
            factor1.append(i)
    for i in range(2,num2):
        if num2%i == 0:
            factor2.append(i)
    return factor1,factor2

def comparer(factor12,factor23):
    factor12,factor23 = factor(num1,num2)

    for i in factor1:
        for k in factor2:
            if i == k:
                factor3.append(i)
    return factor3
hcf(num1,num2)
