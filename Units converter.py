def convertor(flag):
    import os # Importing the package for system clearscreen function


    # Function to accept the choice of the user:
    def choose(unit_list):
        j=1
        for i in unit_list:
            print (j, '. ', i, sep = '')
            j+=1
        return (int(input ('Enter your choice: ')))

    # Function to clear the output screen on Windows devices, but display a line of hyphens on non-Windows devices:
    def clear():
        try:
            os. system('CLS')
        except:
            print ('-----------------------------------------------------')

    # Function to be executed if user enters a choice outide valid limits
    def else_block():
        print ('Please choose only from provided options.')
        if input('Do you want to try again? [yes/no]: ')=='yes':
            convertor('')
        elif input('Do you want to try again? [yes/no]: ')=='no':
            print ('Thank you! Exiting ...')

    # Function to calculate and display relevant information based on the user's input
    def compute(unit_dict):
        clear()
        print('Choose the unit to convert from: [1-',len(unit_dict),']', sep = '')
        ch3 = choose(unit_dict)
        if 0<ch3<=len(unit_dict):
            clear()
            print('Choose the unit to convert to: [1-',len(unit_dict),']', sep = '')
            ch4 = choose(unit_dict)
            if 0<ch4<=len(unit_dict):
                clear()
                unit_list = list(unit_dict)
                from_unit = unit_dict[list(unit_dict)[ch3-1]]
                to_unit = unit_dict[list(unit_dict)[ch4-1]]
                print ('From:', unit_list[ch3-1])
                print ('To:', unit_list[ch4-1])
                if flag=='':
                    input_val = float(input('Enter value to be converted: '))
                else:
                    input_val = flag
                output_val = round(((input_val*from_unit)/to_unit),8)
                print (input_val, unit_list[ch3-1].lower(), 'is', output_val, unit_list[ch4-1].lower(), end='.\n')
                print ('-----------------------------------------------------')
                ch5 = input('Send output to convertor? [yes/no]: ')
                if ch5 =='yes':
                    convertor(output_val)
                elif ch5 =='no':
                    ch6 = input('Send output to calculator? [yes/no]: ')
                    if ch6 =='yes':               
                        pass
                    elif ch6 =='no':
                        print ('Thank you! Exiting ...')
                    else:
                        else_block()
                else:
                    else_block()
            else:
                else_block()
        else:
            else_block()

    clear()
    print ('Units convertor:')
    ch2 = ch3 = ch4 = -1 # Defining initial value for choice variables
    main_dict = {1:'Length', 2:'Mass', 3:'Temperature', 4:'Volume', 5:'Storage',6: 'Energy'}

    # Following dictionaries store the name of the unit as the key and the product for conversion to base unit as the value:
    length_dict = {'Angstrom':10**-10, 'Nanometre':10**-9, 'Micrometre':10**-6,'Millimetre':10**-3,'Centimetre':10**-2,'Decimetre':10**-1,'Metre':1,'Kilometre':10**3,'Megametre':10**6,'Foot':0.3048,'Yard':0.9144,'Inch':0.0254,'Parsec':30857*10**12,'Light-year':946*10**13,'Astronomical Unit':1496*10**8}
    mass_dict = {'Microgram':10**-6,'Milligram':10**-3,'Gram':1,'Kilogram':10**3,'Metric ton':10**6,'Tonne':1.016*10**6,'Pound':453.59,'Ounce':28.349,'Carat':0.2,'Atomic Mass Unit':1.66*10**-24}
    temp_list = ['Celsius','Fahrenheit','Kelvin']
    volume_dict = {'Cubic metre':1,'Litre':10**-3,'Cubic centrimetre':10**6,'Cubic foot':28.316*10**-3,'Cubic inch':16.387*10**-6,'Pint':0.568261*10**-3,'Gallon':4.546*10**-3,'Barrel':0.15989}
    storage_dict = {'Bit':0.125,'Nibble':0.5,'Byte':1,'Kilobyte':1024,'Megabyte':1024**2,'Gigabyte':1024**3,'Terabyte':1024**4,'Petabyte':1024**5,'Exabyte':1024**6,'Zettabyte':1024**7,'Yottabyte':1024**8}
    energy_dict = {'Erg':10**-7,'Joule':1,'Kilojoule':10**3,'Megajoule':10**6,'Gigajoule':10**9,'Calorie':4.184,'Kilocalorie':4184,'Electron volt':1.6022*10**-19,'Watt-hour':3.6*10**3,'Kilowatt-hour':3.6*10**6,'Foot-pound force':1.3558,'British Thermal Unit (BTU)':1055.0559,'Barrel-of-oil equivalent':6117863199.99928,'Therm':105505590}
    
    # Displaying the options of standards to choose from using a for loop to access elements of main_list:
    print ('Choose the standard of units you want to convert: [1-6]')
    for i in main_dict:
            j=main_dict[i]
            print (i, '. ', j, sep = '')
    ch2 = (int(input ('Enter your choice: ')))

    # Choosing the corresponding dictionary based on the user's choice:
    if ch2==1:
        compute(length_dict)
    elif ch2==2:
        compute(mass_dict)
    elif ch2==3:
        clear()
        print ('From which unit?: ')
        for i in range (len(temp_list)):
            print (i+1, '. ', temp_list[i], sep = '')
        ch3 = (int(input ('Enter your choice: ')))
        clear()

        if 0<ch3<=(len(temp_list)): # To check if the value is within list limits 
            print ('To which unit?: ')
            for i in range (len(temp_list)):
                print (i+1, '. ', temp_list[i], sep = '')
            ch4 = (int(input ('Enter your choice: ')))
            clear()
            
            if 0<ch4<=(len(temp_list)): # To check if the value is within list limits
                if ch3==1: 
                    from_unit = 'Celsius'
                    input_val = float(input('Enter value to be converted: '))
                    if ch4==1:
                        to_unit = 'Celsius'
                        output_val = input_val
                    elif ch4==2:
                        to_unit = 'Fahrenheit'
                        output_val = ((input_val*9)/5)+32
                    elif ch4==3:
                        to_unit = 'Kelvin'
                        output_val = input_val+273.15
                elif ch3==2:
                    from_unit = 'Fahrenheit'
                    input_val = float(input('Enter value to be converted: '))
                    if ch4==1:
                        to_unit = 'Celsius'
                        output_val = ((input_val*5)/9)-32
                    elif ch4==2:
                        to_unit = 'Fahrenheit'
                        output_val = input_val
                    elif ch4==3:
                        to_unit = 'Kelvin'
                        output_val = ((input_val*5)/9)+241.15
                elif ch3==3:
                    from_unit = 'Kelvin'
                    input_val = float(input('Enter value to be converted: '))
                    if ch4==1:
                        to_unit = 'Celsius'
                        output_val = input_val-273.15
                    elif ch4==2:
                        to_unit = 'Fahrenheit'
                        output_val = ((input_val*9)/5)-459.67
                    elif ch4==3:
                        to_unit = 'Kelvin'
                        output_val = input_val
                
                # To display relevant information
                print ('-----------------------------------------------------')
                print ('From:', from_unit)
                print ('To:', to_unit)
                print (input_val, from_unit.lower(), 'is', output_val, to_unit.lower(), end='.\n')
                print ('-----------------------------------------------------')
            else:
                else_block()
        else:
            else_block()
    elif ch2==4:
        compute(volume_dict)
    elif ch2==5:
        compute(storage_dict)
    elif ch2==6: # If the user enters 6. Energy as standard for unit conversion
        compute(energy_dict)
    else:
        else_block()
convertor('')