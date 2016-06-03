# The-Ackermann-Function

A brief project to examine the Ackermann function, then record and graph the results.

At the moment I don't have a great grasp of proof theory.
However, I can tell you the Ackermann function is an important part of proof theory since it was the first computable function that is not primative recursive.

What does that even mean?

A computable function is just a function that can be solved algorithmically.

A primative recursive function is a little more complicated. 
According to wikipedia: "In computability theory, primitive recursive functions are a class of functions that are defined using primitive recursion and composition as central operations and are a strict subset of the total µ-recursive functions (µ-recursive functions are also called partial recursive)"

Now what does that mean to the average programmer who doesn't understand computability theory as well as the editors of the wikipedia page do?

Essentially, a primitive recursive function (PR) is a function that can be solved either iteratively or recursively due to the nature of the problem.

This typifies pretty much every problem I've encountered so far. In fact, when realizing this, I tried to come up with a solvable problem that was not PR. I was getting frustrated because I made essentially no progress, but that's okay because after a quick google search i found out that it's actually incredibly difficult to do this.

Enter Wilhelm Ackermann.

This guy fucks.

The Ackermann function is considered the simplest and earliest example of a solveable function that must be solved recursively. (Theoretically, with infinite resources, it could be solved iteratively but you'll understand why that isn't feasible in a moment).

In this case I use the Ackermann-Peter function as it is considered the simples variation of Ackermann's original function.
It can be viewed here: https://en.wikipedia.org/api/rest_v1/media/math/render/svg/1a15ea2fcf1977e497bccdf1916ae23edc412fff

The first statement is very simple and does not perform a recursive call. Thus, m == 0 can be considered the base case for the function.
The second statement does involve one recursive call and is thus more complicated. If n == 0 and m > 0, return the result of calling the function again with m-1 instead of m and n = 1.
The third statement involves a NESTED RECURSIVE CALL. This is the main reason why the problem is so complex. I could try and follow it, but it's simply not worth it. To emphasize why, observe that in order to get just the second input to the outer recursive call, you must make another recursive call. This arduous process occurs for any input n>0 and m>0. If you still don't believe that this would be very difficult just try and trace through it. Here, try and use inputs m = 4 and n = 2 you stubborn fuck. "Those numbers aren't that large, I can trace through that easily," you say...

Let me save you the trouble.

19,729.

The result of ackermann(4,2) is NOT 19,729.

The result of ackermann(4,2) has 19,729 digits in it.

Try and trace through that. Try and find an iterative function to solve the same problem for all inputs. You can't.


#So Yeah
There is my brief summary of the ackermann function. Basically all I did was program the function in python and record how long each solution took as well as how many recursive calls it took for the function to be solved.

Judging by my intuition, I thought that the computer would not be able to even solve half of the inputs I gave to it after 30 minutes. However, my hypothesis could not be accurately tested since after about 1 minute and 45 seconds the program stopped and produced a segmentation fault error (an error I got from my previous wikipedia spider which was an infinite recursive call). Thus, most likely the problem is that one of the modules can't handle such large recursive calls, even when the recursion limit is set so high.

Still, I got the data from after 1 minute and 45 seconds and am currently trying to find out the best way to visualize it.

After looking at the data, I believe I underestimated the power of my computer. After the time alloted, the function completed all combinations of values for m<4 and n<10. However, as m increased, the real power of the algorithm would be tested.
