# My Exploration of the Collatz Conjecture

This repo contains two scripts I made while tinkering with the Collatz conjecture.

I’ve known the Collatz conjecture for a while now, and personally, I’m a Collatz conjecture enjoyer.  
One time, during a car ride, this question appeared in my mind:

> “In the Collatz conjecture rules, both the 2 and the 3 are raised to the first power.  
> What happens if we increase or decrease this power?”

You may think this is a silly question — maybe someone with more knowledge has already explored it —  
but I didn’t care. I wanted to see what would happen myself.

---

## 🧩 The Classic Rules

The Collatz conjecture is simple:

- If a number is **even**, divide it by 2  
- If a number is **odd**, multiply it by 3 and add 1  

The conjecture says that every number in the range `[1, +∞)` will eventually fall into the loop:

1 → 4 → 2 → 1

after a finite number of steps.

I know that the conjecture hasn’t been proven true (yet), which is why I didn’t try to prove it myself —  
but I *was* brave enough to try expanding on it.

---

## 🔍 My Observation

I noticed the following pattern:

n / 2^k
n * 3^k + 1

For the original Collatz conjecture, the value of `k` is 1.  
So I tried increasing it by one:

n / 2^2 = n / 4
n * 3^2 + 1 = 9n + 1

Pretty easy so far — but then the **rounding problem** appeared.  
Every even number is divisible by 2, but not necessarily by 4, so I started testing with the floor function.

Something started happening.  
Creating simple charts from the data showed patterns I could kind of grasp, but not fully understand.  
I’m not that advanced in math yet, but I thought it looked really interesting.

---

## ⚙️ My Alteration of the Collatz Conjecture

After a lot of trying, failing, and thinking, I came up with my own alteration of the Collatz conjecture.

**Range:** `[1, +∞)`

**Rules:**

if even: h(n / 2^k)
if odd: n * 3^k + 1

where `h` is a rounding function (like `floor()` or `ceil()`) that rounds up or down in a predictable way.

### My Statement

> The Collatz conjecture will hold for every integer `k` in range `[1, +∞)`  
> with a given rounding function `h`.

I haven’t proved this — I’ve just tried calculating some paths of numbers with different `h` functions.  
But I think there’s actually something interesting to discover here.

---

## 🧠 About This Project

This repository contains:

- Simple **Python scripts** where I experiment with different values of `k` and `h`
- **Charts** showing how the modified Collatz paths behave
- Notes and results from my tests and thoughts

Feel free to explore the code, try different functions, or suggest improvements!  
I’m not claiming this is original research — I just wanted to follow my curiosity and share what I found interesting. :)

---

## 💭 Final Thoughts

I don’t know if anybody has thought about this before, and I’m not trying to take any credit in that case.  
I just wanted to explain something I thought about. :)

> “Mathematics is not about numbers, equations, or algorithms: it’s about curiosity and patterns.”
