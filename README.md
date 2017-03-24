Aim:-Implement the Muller’s Algorithm in Python.

Background:-Muller’s method is a Root-Finding Algorithm, a numerical method for solving
equations of the form f (x) = 0 . It was first presented by David E. Muller in 1956.
Muller’s method is based on the Secant Method, which constructs a line at every
iteration through two points on the graph of function f .
Muller’s method instead uses three points. It constructs a parabola through these
three points. The intersection of the parabola with the x-axis is the next
approximation.

The Algorithm:-
1. Given a function :
f (x) = 0
2. Guess three initial values for
x 0 , x 1 , x 2
3. Calculate x with the below equations:-
h 0 = x 1 − x 0
h 1 = x 2 − x1
δ 0 =(f ( x 1 ) − f ( x 0 ))/h 0
δ 1 =(f ( x 2 ) − f ( x 1 ))/h 1
a =(δ 1 − δ 0)/(h 0 + h 1)
b = a h 1 + δ 1
c = f ( x 2 )
4. If b is less than zero, compute x as :
 x 3 = x 2 + ((-2 * c)/(b - (math.sqrt((b * b) - (4 * a * c)))))
else
 x 3 = x 2 + ((-2 * c)/(b + (math.sqrt((b * b) - (4 * a * c)))))

5. Calculate the error as:
error =(x 2 − x 3)/x 3
6.
1. Case 1 : If the error is less than or equal to Allowed Error then
Terminate.
2. Case 2 : Otherwise, use the below value of x , x and x , and rework
from Step 3.
x 0 = x 1
x 1 = x 2
x 2 = x 3
