
import math
from termcolor import colored
import logging, sys

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
    
    
    UnitOfMass =input("What type of Unit would you like to use?")
 
    try:
        valueMap[UnitOfMass]
    except:
        print("Sorry you have not choosen the right value")
        print("Please re-try!")
        quit(1)
    Height=float(input("Please enter your height in ft - (ex: 5.5): "))
    if Height < 1.0 and Height > 15.0:
        print("Please enter your accurate height in the ft.")
        quit(1)
    Weight=float(input("Please enter your weight: "))
    return UnitOfMass, Height, Weight

def convertLbToKg(UnitMass, weight):
    if lbDict[UnitMass] == True:
        weight = weight / 2.2046
        weight = math.ceil(weight*100)/100
        logging.debug('weight = %s', weight)
        return weight
    return weight

def convertFtToMeters(height):

    tempCentermeterValue = height / 3.2808
    tempCentermeterValue = math.ceil(tempCentermeterValue*100)/100
    logging.debug('tempCentermeterValue = %s', tempCentermeterValue)

    return tempCentermeterValue

def calculateBMI(weight, height):
    
    logging.debug('height = %s', height ** 2)
    logging.debug('weight = %s', weight)
    newTempBmiValue = round(weight / height ** 2,1)
    bmiValue = math.ceil(newTempBmiValue*100)/100
    print(bmiValue)
    return bmiValue

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
    unit, height, weight = getInputArguments()
    kgweight = convertLbToKg(unit, weight)
    meterHeight = convertFtToMeters(height)
    bmi = calculateBMI(kgweight, meterHeight)
    category = checkBmiCategories(bmi)
    finalDecision(bmi, category)

if __name__ == "__main__":
    run()
