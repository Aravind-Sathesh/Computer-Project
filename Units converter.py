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
    length_list = ['Picometre', 'Angstrom', 'Nanometer', 'Micrometer','Millimetre','Centimetre','Decimetre','Metre','Decametre','Hectometre','Kilometre','Megametre','Gigametre','Foot','Yard','Inch','Parsec','Light-year','Astronomical Unit']
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
            input_val*=pico
        elif ch3==2:
            input_val*=angs
        elif ch3==3:
            input_val*=nano
        elif ch3==4:
            input_val*=micr
        elif ch3==5:
            input_val*=mill
        elif ch3==6:
            input_val*=cent
        elif ch3==7:
            input_val*=deci
        elif ch3==8:
            input_val*=metr
        elif ch3==9:
            input_val*=deca
        elif ch3==10:
            input_val*=hect
        elif ch3==11:
            input_val*=kilo
        elif ch3==12:
            input_val*=mega
        elif ch3==13:
            input_val*=giga
        elif ch3==14:
            input_val*=foot
        elif ch3==15:
            input_val*=yard
        elif ch3==16:
            input_val*=inch
        elif ch3==17:
            input_val*=pars
        elif ch3==18:
            input_val*=ligh
        elif ch3==19:
            input_val*=astr
    else:
        print ('Please choose only from provided choice')
    os. system('CLS')
    print ('Select the unit you want to convert to: ')
    length_list = ['Picometre', 'Angstrom', 'Nanometer', 'Micrometer','Millimetre','Centimetre','Decimetre','Metre','Decametre','Hectometre','Kilometre','Megametre','Gigametre','Foot','Yard','Inch','Parsec','Light-year','Astronomical Unit']
    for i in range (len(length_list)):
        print (i+1, '. ', length_list[i], sep = '')
    ch4 = int(input ('Enter your choice: '))
    pico = 1/(10**-12)
    angs = 1/(10**-10)
    nano = 1/(10**-9)
    micr = 1/(10**-6)
    mill = 1/(10**-3)
    cent = 1/(10**-2)
    deci = 1/(10**-1)
    metr = 1/(10**0)
    deca = 1/(10**1)
    hect = 1/(10**2)
    kilo = 1/(10**3)
    mega = 1/(10**6)
    giga = 1/(10**9)
    foot = 1/(0.3048)
    yard = 1/(0.9144)
    inch = 1/(0.0254)
    pars = 1/(30857 * (10**12))
    ligh = 1/(946 * (10**13))
    astr = 1/(1496 * (10**8))
    if ch4>0 and ch4<=(len(length_list)):
        if ch4==1:
            input_val*=pico
        elif ch4==2:
            input_val*=angs
        elif ch4==3:
            input_val*=nano
        elif ch4==4:
            input_val*=micr
        elif ch4==5:
            input_val*=mill
        elif ch4==6:
            input_val*=cent
        elif ch4==7:
            input_val*=deci
        elif ch4==8:
            input_val*=metr
        elif ch4==9:
            input_val*=deca
        elif ch4==10:
            input_val*=hect
        elif ch4==11:
            input_val*=kilo
        elif ch4==12:
            input_val*=mega
        elif ch4==13:
            input_val*=giga
        elif ch4==14:
            input_val*=foot
        elif ch4==15:
            input_val*=yard
        elif ch4==16:
            input_val*=inch
        elif ch4==17:
            input_val*=pars
        elif ch4==18:
            input_val*=ligh
        elif ch4==19:
            input_val*=astr
    else:
        print ('Please choose only from provided choice.')
    print ('Converted value:', input_val)