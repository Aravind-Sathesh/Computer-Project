import os # Importing the package for system clearscreen function

# Function to accept the choice of the user:
def choose (unit_list):
    for i in range (len(unit_list)):
        print (i+1, '. ', unit_list[i], sep = '')
    return (int(input ('Enter your choice: ')))

# Function to clear the output screen on Windows devices, but display a line of hyphens on non-Windows devices:
def clear():
    print ('-----------------------------------------------------')
    try:
        os. system('CLS')
    except:
        pass

clear()
ch2 = ch3 = ch4 = -1 # Defining initial value for choice variables
# Storing the possible initial standards and units for conversion in lists:
main_list = ['Length','Mass','Temperature','Volume','Storage','Energy']
list_length = ['Picometre', 'Angstrom', 'Nanometre', 'Micrometre','Millimetre','Centimetre','Decimetre','Metre','Decametre','Hectometre','Kilometre','Megametre','Gigametre','Foot','Yard','Inch','Parsec','Light-year','Astronomical Unit']
list_mass = ['Microgram','Milligram','Gram','Kilogram','Metric ton','Tonne','Pound','Ounce','Carat','Atomic Mass Unit']
list_temp = ['Celsius','Fahrenheit','Kelvin']
list_volume = ['Cubic metre','Cubic decimetre','Cubic centrimetre','Cubic foot','Cubic inch','Pint','Gallon','Barrel']
list_storage = ['Bit','Nibble','Byte','Kilobyte','Megabyte','Gigabyte','Terabyte','Petabyte','Exabyte','Zettabyte','Yottabyte']
list_energy = ['Joule','Erg','Calorie','Kilocalorie','']
print ('Units convertor:')

# Displaying the options of standards to choose from using a for loop to access elements of main_list
print ('Choose the standard of units you want to convert: ')
ch2 = choose(main_list)

if ch2==1: # If the user enters 1. Length as standard for unit conversion
    clear()
    print ('From which unit?: ')
    unit_list = list_length
    ch3 = choose(unit_list)
    # Units in terms of standard unit (SI):
    picometre = 10**-12
    angstrom = 10**-10
    nanometre = 10**-9
    micrometre = 10**-6
    millimetre = 10**-3
    centimetre = 10**-2
    decimetre = 10**-1
    metre = 10**0 # Standard unit (SI)
    decametre = 10**1
    hectometre = 10**2
    kilometre = 10**3
    megametre = 10**6
    gigametre = 10**9
    foot = 0.3048
    yard = 0.9144
    inch = 0.0254
    parsec = 30857 * (10**12)
    light_year = 946 * (10**13)
    astro_unit = 1496 * (10**8)

    # Choosing the from_unit for the value entered by the user:
    if ch3>0 and ch3<=(len(unit_list)):
        if ch3==1:
            from_unit=picometre
        elif ch3==2:
            from_unit=angstrom
        elif ch3==3:
            from_unit=nanometre
        elif ch3==4:
            from_unit=micrometre
        elif ch3==5:
            from_unit=millimetre
        elif ch3==6:
            from_unit=centimetre
        elif ch3==7:
            from_unit=decimetre
        elif ch3==8:
            from_unit=metre
        elif ch3==9:
            from_unit=decametre
        elif ch3==10:
            from_unit=hectometre
        elif ch3==11:
            from_unit=kilometre
        elif ch3==12:
            from_unit=megametre
        elif ch3==13:
            from_unit=gigametre
        elif ch3==14:
            from_unit=foot
        elif ch3==15:
            from_unit=yard
        elif ch3==16:
            from_unit=inch
        elif ch3==17:
            from_unit=parsec
        elif ch3==18:
            from_unit=light_year
        elif ch3==19:
            from_unit=astro_unit
    else:
        print ('Please choose only from provided options.')
    clear()
    print ('To which unit?: ')
    ch4 = choose (unit_list)

    # Storing the to_unit as the unit to convert the user's value to:
    if ch4>0 and ch4<=(len(unit_list)):
        if ch4==1:
            to_unit=picometre
        elif ch4==2:
            to_unit=angstrom
        elif ch4==3:
            to_unit=nanometre
        elif ch4==4:
            to_unit=micrometre
        elif ch4==5:
            to_unit=millimetre
        elif ch4==6:
            to_unit=centimetre
        elif ch4==7:
            to_unit=decimetre
        elif ch4==8:
            to_unit=metre
        elif ch4==9:
            to_unit=decametre
        elif ch4==10:
            to_unit=hectometre
        elif ch4==11:
            to_unit=kilometre
        elif ch4==12:
            to_unit=megametre
        elif ch4==13:
            to_unit=gigametre
        elif ch4==14:
            to_unit=foot
        elif ch4==15:
            to_unit=yard
        elif ch4==16:
            to_unit=inch
        elif ch4==17:
            to_unit=parsec
        elif ch4==18:
            to_unit=light_year
        elif ch4==19:
            to_unit=astro_unit
    else:
        print ('Please choose only from provided options.')

elif ch2==2: # If the user enters 2. Mass as standard for unit conversion
    clear()
    print ('From which unit?: ')
    unit_list = list_mass
    ch3 = choose (unit_list)

    # Units in terms of standard unit (SI):
    microgram = 10**-6
    milligram = 10**-3
    gram = 10**0 # Standard unit (SI):
    kilogram = 10**3
    metric_ton = 10**6
    tonne = 1.016 * (10**6)
    pound = 453.59
    ounce = 28.349
    carat = 0.2
    a_m_u = 1.66 * (10**-24)

    # Choosing the from_unit for the value entered by the user:
    if ch3>0 and ch3<=(len(unit_list)):
        if ch3==1:
            from_unit=microgram
        elif ch3==2:
            from_unit=milligram
        elif ch3==3:
            from_unit=gram
        elif ch3==4:
            from_unit=kilogram
        elif ch3==5:
            from_unit=metric_ton
        elif ch3==6:
            from_unit=tonne
        elif ch3==7:
            from_unit=pound
        elif ch3==8:
            from_unit=ounce
        elif ch3==9:
            from_unit=carat
        elif ch3==10:
            from_unit=a_m_u
    else:
        print ('Please choose only from provided options.')
    clear()
    print ('To which unit?: ')
    ch4 = choose (unit_list)
    
    # Storing the to_unit as the unit to convert the user's value to:
    if ch4>0 and ch4<=(len(unit_list)):
        if ch4==1:
            to_unit=microgram
        elif ch4==2:
            to_unit=milligram
        elif ch4==3:
            to_unit=gram
        elif ch4==4:
            to_unit=kilogram
        elif ch4==5:
            to_unit=metric_ton
        elif ch4==6:
            to_unit=tonne
        elif ch4==7:
            to_unit=pound
        elif ch4==8:
            to_unit=ounce
        elif ch4==9:
            to_unit=carat
        elif ch4==10:
            to_unit=a_m_u
    else:
        print ('Please choose only from provided options.')

elif ch2==4: # If the user enters 4. Volume as standard for unit conversion
    clear()
    print ('From which unit?: ')
    unit_list = list_volume
    ch3 = choose (unit_list)

    # Units in terms of standard unit (SI):
    cubic_metre = 10**0 # Standard unit (SI)
    cubic_decimetre = 10**-3
    cubic_centimetre = 10**-6
    cubic_foot = 28.316 * (10**-3)
    cubic_inch = 16.387 * (10**-6)
    pint = 0.568261 * (10**-3)
    gallon = 4.546 * (10**-3)
    barrel = 0.15989

    # Choosing the from_unit for the value entered by the user:
    if ch3>0 and ch3<=(len(unit_list)):
        if ch3==1:
            from_unit=cubic_metre
        elif ch3==2:
            from_unit=cubic_decimetre
        elif ch3==3:
            from_unit=cubic_centimetre
        elif ch3==4:
            from_unit=cubic_foot
        elif ch3==5:
            from_unit=cubic_inch
        elif ch3==6:
            from_unit=pint
        elif ch3==7:
            from_unit=gallon
        elif ch3==8:
            from_unit=barrel
    else:
        print ('Please choose only from provided options.')
    clear()
    print ('To which unit?: ')
    ch4 = choose (unit_list)

    # Storing the to_unit as the unit to convert the user's value to:
    if ch4>0 and ch4<=(len(unit_list)):
        if ch4==1:
            to_unit=cubic_metre
        elif ch4==2:
            to_unit=cubic_decimetre
        elif ch4==3:
            to_unit=cubic_centimetre
        elif ch4==4:
            to_unit=cubic_foot
        elif ch4==5:
            to_unit=cubic_inch
        elif ch4==6:
            to_unit=pint
        elif ch4==7:
            to_unit=gallon
        elif ch4==8:
            to_unit=barrel
    else:
        print ('Please choose only from provided options.')
clear()
if ch3>0 and ch4>0 and ch3<=(len(unit_list)) and ch4<=(len(unit_list)): # To display all data obtained from the user
    input_val = float(input('Enter value to be converted: '))
    print ('-----------------------------------------------------')
    print ('From:', unit_list[ch3-1])
    print ('To:', unit_list[ch4-1])
    output_val = ((input_val*from_unit)/to_unit)
    print (input_val, unit_list[ch3-1].lower(), 'is', output_val, unit_list[ch4-1].lower(), end='.\n')
    print ('-----------------------------------------------------')
