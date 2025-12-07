# Part 1

Okay, this is my stream of consciousness notes for Day One - Secret Entrance. The problem is that I need to find the lock number. It's a single number, an integer, that is the number of times that the dial lands on zero. So I need to create a counter for those instances and increment it each time. This will output the answer to the problem. 

To find these instances of the dial at zero, I need to set up some data structure that crosses over the zero point in a range from 0 to 99. Left-handed movements will decrement the dial count and potentially cross the zero point to 99. Right-handed movements will increment the dial count and potentially cross over the 99 threshold into 0.

The input is a long string of lines, with each line beginning with a 'l' or 'r', indicating the direction the dial should be moved, followed by an integer, which is the number of, or the count of, how many numbers should be incremented or decremented from the dial. So I need a way to parse this input and take the letters L or R as the increment or decrement indication, and then process the following number with the corresponding directional indication. 

So I will list here the components needed for this script. 
- line by line input parser for L/R directionality and increment/decrement dial count. Example: R20, R1, L22, R0
- 0-99 dial component with a crossover in both directions
- 0 dial position counter that increments dial-counter var

# Part 2

- Zero crossings can happen multiple times per rotation
- Include landing on zero as before
- If dial is 55 and input is 40, the difference between 55 and 100 is 45 which is greater than the input. If dial is 55 and input is 400, 45 is less than input. Take 45 from 400 (=355) and divide 355 by 100 (=3 remainder 55)

# Solve for positive steps

```python
dial=30
step=69

if step >= 0: # Righthand direction
    zeros += int((dial+step)/100)
else # Lefthand direction
    zeros += # Getting stuck here

dial=(dial+step)%100
```

# Solve by incremental checks

```python
def solve(path: str) -> int:
    dial = 50
    zeros = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            dir_, num = line[0], int(line[1:])
            step = -num if dir_ == "L" else num
            if step < 0:
                for _ in range(abs(step)):
                    dial -= 1
                    zeros += (dial == 0)
            else
                for _ in range(step):
                    dial += 1
                    zeros += (dial == 0)
    return zeros
```