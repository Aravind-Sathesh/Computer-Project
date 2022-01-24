import os
os. system('CLS')
list_l = ['Picometre', 'Angstrom', 'Nanometre', 'Micrometre','Millimetre','Centimetre','Decimetre','Metre','Decametre','Hectometre','Kilometre','Megametre','Gigametre','Foot','Yard','Inch','Parsec','Light-year','Astronomical Unit']
list_m = ['Microgram','Milligram','Gram','Kilogram','Metric ton','Tonne','Pound','Ounce','Carat','Atomic Mass Unit']
temp_list = ['Celsius','Fahrenheit','Kelvin']
vol_list = []
stg_list = ['Bit','Nibble','Byte','Kilobyte','Megabyte','Gigabyte','Terabyte','Petabyte','Exabyte','Zettabyte','Yottabyte']
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
    print ('From which unit?: ')
    unit_list = list_l
    for i in range (len(unit_list)):
        print (i+1, '. ', unit_list[i], sep = '')
    ch3 = int(input ('Enter your choice: '))
    pico_l = 10**-12
    angs_l = 10**-10
    nano_l = 10**-9
    micr_l = 10**-6
    mill_l = 10**-3
    cent_l = 10**-2
    deci_l = 10**-1
    metr_l = 10**0
    deca_l = 10**1
    hect_l = 10**2
    kilo_l = 10**3
    mega_l = 10**6
    giga_l = 10**9
    foot_l = 0.3048
    yard_l = 0.9144
    inch_l = 0.0254
    pars_l = 30857 * (10**12)
    ligh_l = 946 * (10**13)
    astr_l = 1496 * (10**8)
    if ch3>0 and ch3<=(len(unit_list)):
        if ch3==1:
            from_unit=pico_l
        elif ch3==2:
            from_unit=angs_l
        elif ch3==3:
            from_unit=nano_l
        elif ch3==4:
            from_unit=micr_l
        elif ch3==5:
            from_unit=mill_l
        elif ch3==6:
            from_unit=cent_l
        elif ch3==7:
            from_unit=deci_l
        elif ch3==8:
            from_unit=metr_l
        elif ch3==9:
            from_unit=deca_l
        elif ch3==10:
            from_unit=hect_l
        elif ch3==11:
            from_unit=kilo_l
        elif ch3==12:
            from_unit=mega_l
        elif ch3==13:
            from_unit=giga_l
        elif ch3==14:
            from_unit=foot_l
        elif ch3==15:
            from_unit=yard_l
        elif ch3==16:
            from_unit=inch_l
        elif ch3==17:
            from_unit=pars_l
        elif ch3==18:
            from_unit=ligh_l
        elif ch3==19:
            from_unit=astr_l
    else:
        print ('Please choose only from provided choice')
    os. system('CLS')
    print ('To which unit?: ')
    for i in range (len(unit_list)):
        print (i+1, '. ', unit_list[i], sep = '')
    ch4 = int(input ('Enter your choice: '))
    if ch4>0 and ch4<=(len(unit_list)):
        if ch4==1:
            to_unit=pico_l
        elif ch4==2:
            to_unit=angs_l
        elif ch4==3:
            to_unit=nano_l
        elif ch4==4:
            to_unit=micr_l
        elif ch4==5:
            to_unit=mill_l
        elif ch4==6:
            to_unit=cent_l
        elif ch4==7:
            to_unit=deci_l
        elif ch4==8:
            to_unit=metr_l
        elif ch4==9:
            to_unit=deca_l
        elif ch4==10:
            to_unit=hect_l
        elif ch4==11:
            to_unit=kilo_l
        elif ch4==12:
            to_unit=mega_l
        elif ch4==13:
            to_unit=giga_l
        elif ch4==14:
            to_unit=foot_l
        elif ch4==15:
            to_unit=yard_l
        elif ch4==16:
            to_unit=inch_l
        elif ch4==17:
            to_unit=pars_l
        elif ch4==18:
            to_unit=ligh_l
        elif ch4==19:
            to_unit=astr_l
    else:
        print ('Please choose only from provided choice.')
elif ch2==2:
    os. system('CLS')
    print ('From which unit?: ')
    unit_list = list_m
    for i in range (len(unit_list)):
        print (i+1, '. ', unit_list[i], sep = '')
    ch3 = int(input ('Enter your choice: '))
    micr_m = 10**-6
    mill_m = 10**-3
    gram_m = 10**0
    kilo_m = 10**3
    metr_m = 10**6
    tonn_m = 1.016 * (10**6)
    poun_m = 453.59
    ounc_m = 28.349
    cara_m = 0.2
    atom_m = 1.66 * (10**-24)
    if ch3>0 and ch3<=(len(unit_list)):
        if ch3==1:
            from_unit=micr_m
        elif ch3==2:
            from_unit=mill_m
        elif ch3==3:
            from_unit=gram_m
        elif ch3==4:
            from_unit=kilo_m
        elif ch3==5:
            from_unit=metr_m
        elif ch3==6:
            from_unit=tonn_m
        elif ch3==7:
            from_unit=poun_m
        elif ch3==8:
            from_unit=ounc_m
        elif ch3==9:
            from_unit=cara_m
        elif ch3==10:
            from_unit=atom_m
    else:
        print ('Please choose only from provided choice')
    os. system('CLS')
    print ('To which unit?: ')
    for i in range (len(unit_list)):
        print (i+1, '. ', unit_list[i], sep = '')
    ch4 = int(input ('Enter your choice: '))
    if ch4>0 and ch4<=(len(unit_list)):
        if ch4==1:
            to_unit=micr_m
        elif ch4==2:
            to_unit=mill_m
        elif ch4==3:
            to_unit=gram_m
        elif ch4==4:
            to_unit=kilo_m
        elif ch4==5:
            to_unit=metr_m
        elif ch4==6:
            to_unit=tonn_m
        elif ch4==7:
            to_unit=poun_m
        elif ch4==8:
            to_unit=ounc_m
        elif ch4==9:
            to_unit=cara_m
        elif ch4==10:
            to_unit=atom_m
    else:
        print ('Please choose only from provided choice')
os.system('CLS')
if ch3>0 and ch4>0 and ch3<=(len(unit_list)) and ch4<=(len(unit_list)):
    input_val = float(input('Enter value to be converted: '))
print ('-----------------------------------------------------')
print ('From:', unit_list[ch3-1])
print ('To:', unit_list[ch4-1])
output_val = (input_val*from_unit)/to_unit
print (input_val, unit_list[ch3-1].lower(), 'is', output_val, unit_list[ch4-1].lower(), end='.\n')
print ('-----------------------------------------------------')