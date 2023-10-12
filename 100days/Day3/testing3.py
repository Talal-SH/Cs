# trying to add while true and if togather for My pizza order version
print("Thank you for choosing Python Pizza Deliveries!")
order = input('Do you want a pizza\n')
 
#small =15
#medium =20
#large =25

#perp for S =2 and M\L =3
#cheese =1

accepted_size = ['S','M','L']
accepted_answers = ['Y', 'N']
bill = 0 # The chaning variables through out the ordering prossedure , and to be set at default = 0
if order[0].capitalize() == accepted_answers[0]:
    while True:   
        size = input('Choose the size of the pizza, S, M ,L ?\n')
        order_size = size[0].capitalize()

        if any([x in order_size for x in accepted_size]): # if small was chosen
            if order_size == 'S':
                bill += 15
            if order_size == 'M':
                bill +=20
            if order_size == 'L':
                bill +=25
            add_pepperoni = input('Do you want extra pepperoni? Y, N\n') # ask for pepp
            extra_cheese = input('Do you want extra cheese? Y, N\n')
            if add_pepperoni[0].capitalize() == accepted_answers[0]:
                if order_size == 'S':
                    bill +=2
                    print('added 2$ - extra pep for small pizza')
                else:
                    bill += 3
                    print('added 3$ - extra pep for Medium/Larg pizza')
                
            if extra_cheese[0].capitalize() == accepted_answers[0]:
                bill += 1
                print('added 1$ - extra cheese')
                print(f'Your bill is {bill}$')
                break
            else:
                print(f'Your bill is {bill}$ -')
                break
        else:
            print('sizes are: S, M, L')

else:
    print('Ok bye')



