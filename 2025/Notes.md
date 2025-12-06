# Part 1

Okay, this is my stream of consciousness notes for Day One - Secret Entrance. The problem is that I need to find the lock number. It's a single number, an integer, that is the number of times that the dial lands on zero. So I need to create a counter for those instances and increment it each time. This will output the answer to the problem. 

To find these instances of the dial at zero, I need to set up some data structure that crosses over the zero point in a range from 0 to 99. Left-handed movements will decrement the dial count and potentially cross the zero point to 99. Right-handed movements will increment the dial count and potentially cross over the 99 threshold into 0.

The input is a long string of lines, with each line beginning with a 'l' or 'r', indicating the direction the dial should be moved, followed by an integer, which is the number of, or the count of, how many numbers should be incremented or decremented from the dial. So I need a way to parse this input and take the letters L or R as the increment or decrement indication, and then process the following number with the corresponding directional indication. 

So I will list here the components needed for this script. 
- line by line input parser for L/R directionality and increment/decrement dial count. Example: R20, R1, L22, R0
- 0-99 dial component with a crossover in both directions
- 0 dial position counter that increments dial-counter var

# Part 2

- zero crossings can happen multiple times per rotation
- include landing on zero as before