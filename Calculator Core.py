try:
    from sympy import *
except:
    import os 
    os.system('pip install sympy')
    from sympy import *

def calculator(flag):
    global roots
    roots = ''

    # if flag is a string , it means to take value input from console
    # if flag is a value , the flag is a result from a previous calculation which is to be used now
    choice = int(input('''Do you want to evaluate 
1) An Expression
2) An Equation

Enter choice 1 or 2 :'''))
    print(choice )


    if choice == 1:
        print('You have chosen An Expression : ')
    elif choice == 2:
        print('You have chosen An Equation')
    else:
        print('Invalid Choice ')
        calculator(flag)
    if flag != 'console':
        print('\n     res = '+ str(flag))
        print('     NOTE : use "res" in the following expression for above value\n')
    var = ''

    if choice == 2:
        var = input('enter the variable to be solved : ')
        exp = str(input(('enter equation in one variable = 0 : ')))
    else:
        exp = str(input('enter expression to be solved : '))
    print('')
    if ('res' in exp):

        exp= exp[:exp.index('res')] + '(' + str(flag) +')' + exp[exp.index('res')+3:]

    global result
    result = 0.0

    try:

        if choice == 2:

            x= symbols(var)
            print("equation : {} = 0".format(exp))
            roots = solve(exp, x)
            print('roots : ')

            for i in range(len(roots)):
                roots[i] = str(roots[i]).replace('*I','j')

                print(str(var) + str(i + 1) + '= ' + str(eval(str(roots[i]))))

            result = str(eval(str(roots[0])))

        else:
            print('expression = ' + exp)
            print('result : ' + str(eval(exp)))
            result = str(eval(exp))

        ans = input('\nSend output to calculator ? [yes/no] : ').lower()

        if ans=='yes' :

            if len(roots) >= 2:
                ch = int(input('Enter which value you want to export [1,2...] :'))
                if 0 < ch <= len(roots):
                    result = roots[ch-1]
                else:
                    print('Exporting default')

            calculator(result)

        else:
            ans2 = input('Send output to converter ? [yes/no] : ').lower()
            if ans2 == 'yes':
                if len(roots) >= 2:
                    ch = int(input('Enter which value you want to export [1,2...] :'))
                    if 0 < ch <= len(roots):
                        result = roots[ch - 1]
                    else:
                        print('Exporting default')
                # converter(result)


            else:
                print('Thank you ! Exiting ...')

    except Exception as e:
        print('\nerror in expression due to "' + str(e) +'..."\ntry again ')
        calculator(eval(flag))



calculator('console')
