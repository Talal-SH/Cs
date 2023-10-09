# this is name generator
wellcome = ('wellcome to the name username Generator')
print(wellcome)
name = input("Give me your First name  ") 
date = input("Give me year of birth ") 
color = input("Give me a Color ")


result_date = int(date) % 100


result = f'{color[0] }{name.capitalize()}{result_date}{color[-1]}'


print(f'Your generated name is: {result}')
