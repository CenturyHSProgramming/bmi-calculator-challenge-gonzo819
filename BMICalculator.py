# BMICalculator.py
# Your job is to write a BMI calculator that matches the formula
# and chart on http://flightphysical.com/medical-exam/weight

# Define Function below
# be sure to return an integer
def calculateBMI(inches,pounds):
    """ receives pounds & inches -> returns bmi """
    bmi =  pounds /  inches ** 2 *703
    bmi = round (bmi)
    return bmi 

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    weight = int(input( " Please enter your weight pounds:"))
    height = int(input("Please enter your height in inches:"))
    calculateBMI(height,weight)
    print()



