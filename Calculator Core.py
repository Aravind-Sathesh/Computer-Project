try:
    from sympy import *
except:
    import os 
    os.system('pip install sympy')
    from sympy import *

def calculator(flag):
    # if flag is a string , it means to take value input from console
    # if flag is a value , the flag is a result from a previous calculation which is to be used now
    print('')
    if flag != 'console':
        print('\nres = '+ str(flag))
        print('use "res" in the following expression for above value')
    var = input('enter the variable to be solved [enter "None" if expression ] : ')
    exp = str(input('enter expression or equation in one variable = 0 : '))
    print('')
    if ('res' in exp):

        exp= exp[:exp.index('res')] + str(flag) + exp[exp.index('res')+3:]

    global result
    result = 0.0
    try:

        if var != 'None':

            x= symbols(var)
            print("equation : {} = 0".format(exp))
            roots = solve(exp, x)
            print('roots : ')

            for i in range(len(roots)):
                print(str(var) + str(i + 1) + '= ' + str(eval(str(roots[i]))))

            result = eval(str(roots[0]))

        else:
            print('expression = ' + exp)
            print('result : ' + str(eval(exp)))
            result = eval(exp)

        ans = input('\nSend output to calculator ? [yes/no] : ').lower()

        if ans=='yes' :
            calculator(result)

        else:
            ans2 = input('Send output to converter ? [yes/no] : ').lower()
            if ans2 == 'yes':
                # converter(result)
                # once we combine programs , we'll call the converter function here 
                pass

            else:
                print('Thank you ! Exiting ...')

    except Exception as e:
        print('\nerror in expression due to "' + str(e) +'..."\ntry again ')
        calculator(float(flag))



calculator('console')
