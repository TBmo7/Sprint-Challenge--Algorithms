#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n)
	for each input we're doing the same amount of work, We're looping a finite number of times until a is large enough


b) This will be 
 O(n*n)
For each input we're creating n number operation and n number of operations again,
For each n, we're looping and then looping again

c) Logrithmic, 
	for every input we're doing removing inputs as we go along
	there is a constant "2" but at large enough numbers the 2 becomes less significant.

## Exercise II


Put the eggs down, get large enough wheeled container, take the elevator.

You have a building N stories high

Eggs break at floor f(n)
but dont at (f(n)-1)

So we have broken_eggs(n):
	f(n) = True we have eggs broken here
	This would either be a divisor, or a mere subtraction element, such as 5 stories is the hieght at 
	which egg survival drops beyond acceptable 
	f(n)-1 = False not here
 	where as this would be acceptable
	

	So we would calculate n - f if this is a number greater than 0 we return (n-f) - 1 For Safety!
	if n - f is less than or equal to 0, we can return that the height of this building is within
	margins
	This calculation is constant time, it requires the same amount of work regardless of how big n
	is. 


