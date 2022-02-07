
### English-metric conversions

step 1: converting units. Please complete each of these functions.
## If you need the formulas, you can find them here: https://www.mathsisfun.com/metric-imperial-conversion-charts.html

## convert miles to KM and return the result. Remove 'pass' and add your code.

def milesToKM(miles) :
    pass


## convert kilometers to miles and return the result
def KMToMiles(km) :
   pass

## convert kilograms to pounds and return the result.

def KGToPounds(kg) :
    pass

## convert pounds to kilograms and return the result

def poundsToKG(pounds) :
   pass


## convert liters to quarts and return the result
def litersToQuarts(liters) :
    pass

## convert liters to quarts and return the result
def quartsToLiters(quarts) :
    pass


##  Use the milesToKM function as a helper here.
def getKMPerSecond(distanceInMiles, mph) :
    pass


## One gallon of water weighs 8.34 pounds.
## This function takes as input a number of pounds of water and returns
## the metric volume  in liters. Please use your functions  above as helpers.

def waterVolumeFromMass (mass_in_pounds):
    pass


##  This should take as input a temperature (in Celsius).
## if the temp is less than or equal to zero, print "Ice". If it's between
## 0 and 100, print "Liquid water". If it's greater than 100, print "Steam".

def determine_water_state(temp)  :
    pass

### The formula for compund interest is:
## amount = principal * (1 + r/n) ^(nt)
## where principal is the initial investment, r is the interest rate, n  is the number of times it
## compounds per year (12 for monthly, 52 for weekly, etc) and t is the number of years.

def compound_interest(principal, rate, compounding, num_years) :
    pass

## Next, let's write a function called model_growth. It should use a loop to call compound_interest for years 1-10 and print out our 
# balance for each year. Assume 8% interest and 12 compounds per year.

def model_growth(principal, rate, compounding) :
    pass


if  __name__ == "__main" :
    print(milesToKM(100))
    print(KMToMiles(100))
    print(KGToPounds(200))
    print(poundsToKG(250))
    print(litersToQuarts(30))
    print(quartsToLiters(40))
    print(getKMPerSecond(100, 40))
    print(waterVolumeFromMass(100))
    print(determine_water_state(-3))
    print(determine_water_state(30))
    print(determine_water_state(140))
    model_growth(10)
    











### Question 3. Write a function called tooHeavy. It should take as input a weight in pounds, convert
### that to kilograms, and then return true if the object is greater than 10 kilograms, and false otherwise.
### Make use of the functions from question 1 as necessary.

def tooHeavy(weightInPounds) :
    weightInKilos = poundsToKG(weightInPounds)
    if weightInKilos > 10 :
        return True
    else :
        return False

### Question 4.  Write a function that takes a list of five distances: [10 miles, 50 miles, 100 miles,
## 250 miles, 1000 miles] converts each amount to km, and then prints out how
## long it would take to travel that distance if we were traveling 110 km/hr.
### Make use of the functions from question 1 as necessary.

distanceList = [10,50,100,250,1000]

def convertListOfDistances(distanceList) :
    for item in distanceList :
        km = milesToKM(item)
        hours = km / 110
        print(hours)


### question 5: Extend convertListOfDistances to print out "pack a lunch!" for all the trips greater than 2 hours.

def convertListOfDistancesWithLunch(distanceList) :
    for item in distanceList :
        km = milesToKM(item)
        hours = km / 110
        print(hours)
        if hours > 2:
            print("pack a lunch")


### question 6: you're done! Review the GitHub video to make sure you know how to submit your assignment,
### and then use commit and push to add it to your GitHub repo.

