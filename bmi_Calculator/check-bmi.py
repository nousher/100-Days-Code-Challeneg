
import math
from termcolor import colored
import logging, sys
import pint

u = pint.UnitRegistry()

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
print('Welcome to the BMI Calculator!')

valueMap = {'Kg': True,
'kg': True,
'Kilogram': True,
'lb': True,
'Lb': True,
'Pounds': True}

lbDict = {
   'lb': True,
'Lb': True,
'Pounds': True,
'Kg': False,
'kg': False,
'Kilogram': False
}

def getInputArguments():
    

    Height=float(input("Please enter your height in meters - (ex: 1.56): "))
    if Height < 1.0 and Height > 15.0:
        print("Please enter your accurate height in meters")
        quit(1)
    Weight=float(input("Please enter your weight in Kg: "))
    return  Height, Weight


def calculateBMI(weight, height):
    
    tempBMI= weight/ height ** 2
    tempBMI=round(tempBMI, 2)
    logging.debug('tempBMI = %s', tempBMI)

    return tempBMI

def checkBmiCategories(bmiValue):
    category =""
    if bmiValue < 18.5:
        category = "Under Weight"
    elif bmiValue >= 18.5 and bmiValue <= 24.99:
        category = "Normal Weight"
    elif bmiValue >= 25 and bmiValue <= 29.99:
        category = "Over Weight"
    elif bmiValue >= 30 and bmiValue <= 34.99:
        category = "Obesity"
    elif bmiValue >= 35 and bmiValue <= 39.99:
        category = "Obesity - 2"
    elif bmiValue >= 40:
        category = "Dangerous"
    return category

def finalDecision(bmi, category):

    if category == "Under Weight":
        print(colored(f"Your BMI is {bmi} and category is {category}. Please eat something healthy", 'blue'))
    if category == "Normal Weight":
        print(colored(f"Your BMI is {bmi} and category is {category}. You have perfect BMI", 'green'))
    if category == "Over Weight":
        print(colored(f"Your BMI is {bmi} and category is {category}. You need to evaluate your dietary choices", 'yellow'))
    if category == "Obesity":
        print(colored(f"Your BMI is {bmi} and category is {category}. You are considered obese, make sure to get at least 150 mins of exercise in a week", 'cyan'))
    if category == "Obesity - 2":
        print(colored(f"Your BMI is {bmi} and category is {category}. You are close to get dangerously obese, make sure to get at least 200 mins of exercise in a week", 'magenta'))
    if category == "Dangerous":
        print(colored(f"Your BMI is {bmi} and category is {category}. You are dangerously obese, please consult a healthcare professional", 'red'))
    

def run():
    height, weight = getInputArguments()
    bmi = calculateBMI(weight, height)
    category = checkBmiCategories(bmi)
    finalDecision(bmi, category)

if __name__ == "__main__":
    run()
