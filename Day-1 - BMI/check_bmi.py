
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
   'lb': False,
'Lb': False,
'Pounds': False,
'Kg': True,
'kg': True,
'Kilogram': True
}

def getInputArguments():
    
    
    UnitOfMass =input("What type of Unit would you like to use?")
 
    try:
        valueMap[UnitOfMass]
    except:
        print("Sorry you have not choosen the right value")
        print("Please re-try!")
        quit(1)
    Height=input("Please enter your height in ft - (ex: 5.5): ")
    height = float(Height)
    if height < 1.0 and height > 15.0:
        print("Please enter your accurate height in the ft.")
        quit(1)
    Weight=input("Please enter your weight: ")
    Weight = float(Weight)
    return UnitOfMass, height, Weight

def convertKgToLb(UnitMass, weight):
    if lbDict[UnitMass] == True:
        weight = weight * 2.204622621852
        weight = math.ceil(weight*100)/100
        logging.debug('weight = %s', weight)
        return weight
    return weight

def convertFtToCentemers(height):

    tempCentermeterValue = height * 30.48
    tempCentermeterValue = math.ceil(tempCentermeterValue*100)/100
    logging.debug('tempCentermeterValue = %s', tempCentermeterValue)

    return tempCentermeterValue

def calculateBMI(weight, height):

    height = height * 0.39370
    weight = int(weight)
    logging.debug('weight = %s , height = %s', weight, height)

    tempHeight = int(height)
    newHeight = tempHeight * tempHeight
    logging.debug(' newHeight = %s', newHeight)

    tempBmiValue =  (weight / newHeight)
    logging.debug('tempBmiValue = %s ', tempBmiValue)

    newTempBmiValue = tempBmiValue * 703
    logging.debug('newTempBmiValue = %s ', newTempBmiValue)

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
    kgweight = convertKgToLb(unit, weight)
    meterHeight = convertFtToCentemers(height)
    bmi = calculateBMI(kgweight, meterHeight)
    category = checkBmiCategories(bmi)
    finalDecision(bmi, category)

if __name__ == "__main__":
    run()
