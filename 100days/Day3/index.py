
#my BMI cal
# Enter your height in meters e.g., 1.55
#height = float(input())
# Enter your weight in kilograms e.g., 72
#weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bmi = (weight) / ((height) * (height))
#if bmi < 18.5:
#  print(f'Your BMI is {bmi}, you are underweight.')
#elif bmi > 18.5 and bmi < 25:
#  print(f'Your BMI is {bmi}, you have a normal weight.')
#elif bmi >= 25 and bmi < 30:
#  print(f'Your BMI is {bmi}, you are slightly overweight.')
#elif bmi > 30 and bmi < 35:
#  print(f'Your BMI is {bmi}, you are obese.')
#else :
#  print(f'Your BMI is {bmi}, you are clinically obese.')

# skipping it as it is , need wokring on error handeling and input minipulation 


#day3
# now finalize what you gained on loops and ifs lists and make non-native pay chatrted fees based on age upon entry and the native free
yes_list = ['y', 'Y']
no_list = ['n', 'N']
while True:
    nationality = input('Are you native to this country? use Y or N\n')
    if any([x in nationality[0] for x in yes_list]):
        print('Enjoy free entry on YOUR national day')
        break
    elif any([x in nationality[0] for x in no_list]):
        try:
            age = int(input('How old are you?\n'))
            if age <= 5:
                bill = 5
                print(f'Your kid entry fees: {bill}')
            elif age <= 11:
                bill = 10
                print(f'Your child entry fees: {bill}')
            elif age < 18:
                bill = 15
                print(f'Your Teen entry fees: {bill}')
            else:
                bill = 20
                print(f'Your Adult entry fees: {bill}')
            
        
            photo = input('do you want to take a photo?\n')
            if any([x in photo[0] for x in yes_list]):
                print(f'Your total fees {bill + 3}$')
                break
            elif any([x in photo[0] for x in no_list]):
                print('Thank you')
            else:
                print('Answer with Y OR N')    
        except ValueError:
            print('type in numbers please')    
    else:
        print('Y for yes N for no!')



