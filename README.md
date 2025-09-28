# Collatz-conjecture-attempt
This repo contains twwo scipts i made while tinkering with the collatz conjecture

I have known the collatz conjecture for a while now and personally i am a collatz connjecture enjoyer.
One time, during a car ride, this question appeared in my mind: "In the collatz conjecture rules both the 2 and the 3 are raised to the first power, what happens if we increase of decrease this power? U may think that this is a stupid question, someone with more knowledge may have already found the answer to this, but i didnt care and wanted to try to investigate this further.

The rules of the collatz conjecture are: 
  1) if a number is even divide it by 2
  2) if a number is odd multiply it by 3 and add one
  quite simple, the conjecture says that for every number in the range [1, +inf) will fall to the loop 1, 4, 2, 1 after a finite amount of steps, i know that the conjecture has   yet to be proven true, thats why i didnt dare to try, what is was in fact brave enough to do it to expand it.

I noticed the rules:
  1) n/2^k
  2) n3^k + 1
  for the collatz conjecture the value of k is 1, i tried increasing it by one, the rules become:
  1) n/2^2 = n/4
  2) n3^2 + 1 = n9 + 1
  Pretty easy so far, but the rounding problem quickly appeared. Every even number is divisible by 2 but by 4, so i started testing with the floor function. Something started    happening. Creating simple charts on the data showed something that i could grasp and still cant, im not that advanced in math yet, i just thought it looked interesting.

  after trying, failing and trying again for a lot of time, after spending a lot of time thinking about it i came up with my alteration of the collatz conjecture.

The rules:
  Range: [1, +inf)
  1) if even: h(n/2^k)
  2) if odd: n3^k + 1

  Statement: the collatz conjecture will hold for every integer k in range [1, +inf) with a given rounding function h that rounds up or down in a predictable way.
  I have just expressed this conjecture, i havent proved it, i have tried calculating some paths of numbers with different h functions. I think that there is actually     something to discover here. 

I dont know if anybody has thought about this before, im not trying to take any credits in that case, im just trying to explain something i thoght about. :)
