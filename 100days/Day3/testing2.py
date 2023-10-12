#day3
# now finalize what you gained on loops and ifs lists and make non-native pay chatrted fees based on age upon entry and the native free
# yes_list = ['y', 'Y']
# no_list = ['n', 'N']
# while True:
#     nationality = input('Are you native to this country? use Y or N\n')
#     if any([x in nationality[0] for x in yes_list]):
#         print('Enjoy free entry on YOUR national day')
#         break
#     elif any([x in nationality[0] for x in no_list]):
#         try:
#             age = int(input('How old are you?\n'))
#             if age <= 5:
#                 print('Your kid entry fees: 5$')
#             elif age <= 11:
#                 print('Your child entry fees: 10$')
#             elif age < 18:
#                 print('Your Teen entry fees: 15$')
#             else:
#                 print('Your Adult entry fees: 20$')
#             break
#         except ValueError:
#             print('type in numbers please')
#         break
#     else:
#         print('Y for yes N for no!')




# accepted_answers = ['y','Y','n', 'N']
# while True:
#     nationality = input('Are you native to this country? use Y or N\n')
#     if len(nationality) == 1 and nationality.isnumeric() == False:
#             na = nationality.capitalize()
#             break
#     elif nationality[0] == 'y' or 'Y':
#          native = True
#          print('Enjoy the park for free on this national day!')
#     else:   
#         print('type Y for Yes and N for No')
    
# print(na)



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
    size = input('Choose the size of the pizza, S, M ,L ?\n')
    if size[0].capitalize() == accepted_size[0]: # if small was chosen
        bill += 15
        add_pepperoni = input('Do you want extra pepperoni? Y, N\n') # ask for pepp
        extra_cheese = input('Do you want extra cheese? Y, N\n')
        if add_pepperoni[0].capitalize() == accepted_answers[0]:
            bill += 2
            print('added 2$ - extra pepp')
        if extra_cheese[0].capitalize() == accepted_answers[0]:
            bill += 2
            print('added 2$ - extra cheese')
            print(f'Your bill is {bill}$')
        else:
            print(f'Your bill is {bill}$ with no extra addetions')
    else:
        print('sorry we only have Small for now')
else:
    print('Ok bye')

