
### Assignment 1. 

### Due - Tuesday Feb 15, start of class.

This assignment is intended to give you some practice writing basic Python code, including functions, parameters, loops and conditionals. 
You'll also learn how to set up your own gitHub repo; we'll be using that to submit this assignment.

1. To begin, watch [this video](https://www.youtube.com/watch?v=HYYWQadJ0Pw), which will show you a little bit about GitHub and how to use it. 

2. Then, go to GitHub Classroom to check out the assignment. Here's the URL: https://classroom.github.com/a/HwAHWfUq

3. For this assignment, we're going to write some functions to help us convert from English measurements to metric and back. I've provided a few empty functions to get you started.  
   Please complete each of them.  I've also provided a 'main' that will execute your functions.

- milesToKM

- KMToMiles

- KGToPounds

- poundsToKG 

- litersToQuarts

- quartsToLiters

4. write a function that takes a distance in miles and a velocity in MPH
and returns the equivalent velocity in KM/second.

5. Write a function that takes as input a mass of water (in pounds) and returns the volume of water (in liters). 
You should use the functions above as helpers.


6. Write a function called determine_water_state. It should take as input a temperature (in Celsius). 
If the temp is less than or equal to zero, return the string "Ice". If it's between
0 and 100, return "Liquid water". If it's greater than 100, return "Steam".

7. Implement the function for computing compound interest. 
The formula for compund interest is:

amount = principal * (1 + r/n) ^(nt)

where principal is the initial investment, r is the interest rate, n  is the number of times it
ompounds per year (12 for monthly, 52 for weekly, etc) and t is the number of years. r is a float, so 5% interest is 0.05

9. Then, write a function called model_growth. It should use a loop to call compound_interest for years 1-10 and print out our 
balance for each year. Assume 8% interest and 12 compounds per year. 

10. And you're done! Use git to check your code back into your repo.
