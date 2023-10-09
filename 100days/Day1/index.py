# this is name generator
wellcome = ('Wellcome to the Username Generator. \nA name will be generated based on the answers')
print(wellcome)
name = input("Give me your First name: ")
while True:
    try: 
        date = int(input('Give me the Year of birth: '))
        dateconfirmed = date
        break
    except ValueError:
        print('Please provide the Year of birth in integers, ex. 1999 or 99: ')

color = input("Give me a Color: ")


result_date = dateconfirmed % 100


result = f'{color[0] }{name.capitalize()}{result_date}{color[-1]}'


print(f'Your Generated Username is: {result}')
