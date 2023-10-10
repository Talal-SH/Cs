# this is name generator
wellcome = ('Wellcome to the Username Generator. \nA name will be generated based on the answers')
print(wellcome)
name = input("Give me your First name:\n")
while True:
    try: 
        date = int(input('Give me the Year of birth:\n'))
        dateconfirmed = date
        break
    except ValueError:
        print('Please provide the Year of birth in integers, ex. 1999 or 99:\n')

color = input("Give me a Color: \n")

# variable % 100 would give the hundreths charecters 1990 -> 99
result_date = dateconfirmed % 100


result = f'{color[0] }{name.capitalize()}{result_date}{color[-1]}'


print(f'Your Generated Username is:\n{result}')
