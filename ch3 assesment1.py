##This program is developed Kritaansh Talwar
##This program will calculate the factorial of a number


def factorial (fac_num):

    if fac_num < 2:
        return 1
       
    else:
           
        return fac_num * ( factorial (fac_num-1) )

inp_num=int(input('enter ur number: '))
result=factorial(inp_num)
print(result)