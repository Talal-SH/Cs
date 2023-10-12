#testing 
#simple if else statment byt using it in age verification

#age = int(input('Please type your age\n'))

#if age >= 18:
#    print('Pass')
#else:
#    print('Fail')


#-----------make it only accept only int
#-----------I think this while true contarption is: take what inside and do it, if no error apears break out like nothin happend..?
#-----------~~~~~~~except this specific (not the right return) usually an error, when it apear, it excecute a print stating error , do it agin ( the error in this case is a int() does not accept this input = letter no no numberss yeseysss )  

#while True:
#    try:
#        age = int(input('Please type your age\n'))
#        break
#    except ValueError:
#        print('Please provide it in integers \n')
#---------we got age now 
#if age >= 18:
#    print('Pass')
#    sex = input('which sex are you? Answer with M or F')
#    print(sex)
#else:
#    print('Fail')

#----------messing around and constracting this [ while true ] for insuring the user only inputs one charecter either M or F, and capitalizing it while at it <.< bdm ts
while True:
        sex = input('which is your sex? M or F\n')
        if len(sex) == 1:
            sex = sex.capitalize()
            break
        else:
            print('please type onlt the letter, M or F?\n')

print(sex)

#age checker for park entry fees for a whole day based on age while making sure input passed is int

#  age <= 5         pays 5$
#  6 >= aga <=11    pays 10$
#  12 >= age < 18   pays 15$
#  age >= 18        pays 20$

while sex == 'M':
        #now altering the True above me means the loop only start when this condition is met and not automaticly py python order
    try:
        age = int(input('How old are you?\n'))
        if age <= 5:
            print('Your kid entry fees: 5$')
        elif age <= 11:
            print('Your child entry fees: 10$')
        elif age < 18:
            print('Your Teen entry fees: 15$')
        else:
            print('Your Adult entry fees: 20$')
        break
    except ValueError:
        print('type in numbers please')


# make the input only takes 1 non-numrical alphapatic(string) chatrecter
while True:
    sex = input('which is your sex? M or F\n')
    if len(sex) == 1 and sex.isnumeric() == False:
            
            sex = sex.capitalize()
            break
    else:
        print('please type onlt the letter, M or F?\n')
print(sex)

