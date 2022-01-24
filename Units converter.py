import os
os. system('CLS')
print ('Units convertor:')
print ('Enter the standard of units you want to convert: ')
print ('1. Length')
print ('2. Mass')
print ('3. Temperature')
print ('4. Volume')
print ('5. Storage')
ch2 = int(input ('Enter your choice: '))
if (ch2==1):
    os. system('CLS')
    print('Selected standard: Length')
    print ('Select the unit you want to convert from: ')
    length_list = ['Picometre', 'Angstrom', 'Nanometre', 'Micrometre','Millimetre','Centimetre','Decimetre','Metre','Decametre','Hectometre','Kilometre','Megametre','Gigametre','Foot','Yard','Inch','Parsec','Light-year','Astronomical Unit']
    for i in range (len(length_list)):
        print (i+1, '. ', length_list[i], sep = '')
    ch3 = int(input ('Enter your choice: '))
    pico = 10**-12
    angs = 10**-10
    nano = 10**-9
    micr = 10**-6
    mill = 10**-3
    cent = 10**-2
    deci = 10**-1
    metr = 10**0
    deca = 10**1
    hect = 10**2
    kilo = 10**3
    mega = 10**6
    giga = 10**9
    foot = 0.3048
    yard = 0.9144
    inch = 0.0254
    pars = 30857 * (10**12)
    ligh = 946 * (10**13)
    astr = 1496 * (10**8)
    if ch3>0 and ch3<=(len(length_list)):
        input_val = float(input('Enter value to be converted: '))
        if ch3==1:
            to_metre=pico
        elif ch3==2:
            to_metre=angs
        elif ch3==3:
            to_metre=nano
        elif ch3==4:
            to_metre=micr
        elif ch3==5:
            to_metre=mill
        elif ch3==6:
            to_metre=cent
        elif ch3==7:
            to_metre=deci
        elif ch3==8:
            to_metre=metr
        elif ch3==9:
            to_metre=deca
        elif ch3==10:
            to_metre=hect
        elif ch3==11:
            to_metre=kilo
        elif ch3==12:
            to_metre=mega
        elif ch3==13:
            to_metre=giga
        elif ch3==14:
            to_metre=foot
        elif ch3==15:
            to_metre=yard
        elif ch3==16:
            to_metre=inch
        elif ch3==17:
            to_metre=pars
        elif ch3==18:
            to_metre=ligh
        elif ch3==19:
            to_metre=astr
    else:
        print ('Please choose only from provided choice')
    os. system('CLS')
    print ('Select the unit you want to convert to: ')
    length_list = ['Picometre', 'Angstrom', 'Nanometre', 'Micrometre','Millimetre','Centimetre','Decimetre','Metre','Decametre','Hectometre','Kilometre','Megametre','Gigametre','Foot','Yard','Inch','Parsec','Light-year','Astronomical Unit']
    for i in range (len(length_list)):
        print (i+1, '. ', length_list[i], sep = '')
    ch4 = int(input ('Enter your choice: '))
    if ch4>0 and ch4<=(len(length_list)):
        if ch4==1:
            to_unit=pico
        elif ch4==2:
            to_unit=angs
        elif ch4==3:
            to_unit=nano
        elif ch4==4:
            to_unit=micr
        elif ch4==5:
            to_unit=mill
        elif ch4==6:
            to_unit=cent
        elif ch4==7:
            to_unit=deci
        elif ch4==8:
            to_unit=metr
        elif ch4==9:
            to_unit=deca
        elif ch4==10:
            to_unit=hect
        elif ch4==11:
            to_unit=kilo
        elif ch4==12:
            to_unit=mega
        elif ch4==13:
            to_unit=giga
        elif ch4==14:
            to_unit=foot
        elif ch4==15:
            to_unit=yard
        elif ch4==16:
            to_unit=inch
        elif ch4==17:
            to_unit=pars
        elif ch4==18:
            to_unit=ligh
        elif ch4==19:
            to_unit=astr
    else:
        print ('Please choose only from provided choice.')
    os.system('CLS')
    print ('From:', length_list[ch3-1])
    print ('To:', length_list[ch4-1])
    output_val = input_val*to_metre/to_unit
    print (input_val, length_list[ch3-1].lower(), 'is', output_val, length_list[ch4-1].lower(), end='.')
    print ('------------------------------------------------------------------------')