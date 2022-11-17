# 100-days-100-problems

This repository contains 100 problems solved in a span of 100 days. The goal of this project is to have the habit of coding daily.

Chosen Programming Language : Python

## Day 1 : Retail store

A retailer is having a store-wide "buy 2, get 1 free" sale. For legal reasons, they can't charge their customers $0 for an article so a discount is applied to all products instead. For example, if a customer gets three products a, b and c:
Product A	Product B	Product C
$15.99	$23.50	$10.75

She gets the cheapest one for free, so she ends up paying $15.99 + $23.50 = $39.49, but what her receipt says is:

    * Product A: $15.99 − Special Discount = $12.57
    * Product B: $23.50 − Special Discount = $18.47
    * Product C: $10.75 − Special Discount = $8.45
    
    Total: $39.49

Create a function that takes in a list of prices for a customer's shopping cart and returns the prices with the discount applied. Round all prices to the cent.

### Examples 

```
discount([2.99, 5.75, 3.35, 4.99]) ➞[2.47, 4.74, 2.76, 4.12]
First product for free.

discount([10.75, 11.68]) ➞ [10.75, 11.68]
No discounts applied.

discount([68.74, 17.85, 55.99]) ➞ [60.13, 15.62, 48.98]
Second product for free.

discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) ➞ [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]
First and sixth products for free (see second note).
```
### Conditions : 
    * The discount is calculated in percentual terms.
    * The deal applies to sets of three products: if a customer gets 9 products, she will get the three cheapest ones for free, but if she gets 10 or 11 products, she will still get three for free. Buying a 12th product would get her a fourth free product.
    * No cart splitting allowed.
### Keywords : 
    * Lambda function 
    * Unit testing
    * Arrays

## Day 2 : Josephus Permutation

A group of n prisoners stand in a circle awaiting execution. Starting from an arbitrary position(0), the executioner kills every kth person until one person remains standing, who is then granted freedom (see examples).
Create a function that takes 2 arguments — the number of people to be executed n, and the step size k, and returns the original position (index) of the person who survives.

### Examples

```
who_goes_free(9, 2) ➞ 2

# Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Executed people replaced by - (a dash) for illustration purposes.
# 1st round of execution = [0, -, 2, -, 4, -, 6, -, 8]  -> [0, 2, 4, 6, 8]
# 2nd round = [-, 2, -, 6, -] -> [2, 6]  # 0 is killed in this round because it's beside 8 who was skipped over.
# 3rd round = [2, -]

who_goes_free(9, 3) ➞ 0

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
# [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
# [0, 1, -, 6] -> [0, 1, 6]
# [0, -, 6] -> [0, 6]
# [0, -] -> [0]
```

### Keywords : 
    * Recursive
    * Arthmetic

## Day 3 : Crack the Pin Code

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```
Your secret agent Mubashir has already given you a pincode. However, he also said it's possible that each of the digits he saw could be another adjacent digit (horizontally or vertically, but not diagonally).

Suppose the secret agent has given you the code: 46:

```
# Instead of the 4 it could also be 1, 5, or 7.
# Instead of the 6 it could also be 3, 5, or 9.

crack_pincode("46") ➞
["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]
```

Create a function that takes an argument of pincode informed by your secret agent and returns a list of all possible variations of the pin codes.

### Examples

```
crack_pincode("0") ➞ ["0", "8"]

crack_pincode("2") ➞ ["1", "2", "3", "5"]

crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]
```

### Conditions

    * All pin codes must be strings, because of potentially leading 0s.


## Day 4 : Minesweeper Number of Neighbouring Mines

Create a function that takes a list representation of a Minesweeper board, and returns another board where the value of each cell is the amount of its neighbouring mines.
Mines are either diagonally or adjacent to each cell

### Examples

The input may look like this:

```
[
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
]
```

The `0` represents an empty space. The `1` represents a mine.

You will have to replace each mine with a `9` and each empty space with the number of adjacent mines, the output will look like this:

```
[
  [1, 9, 2, 1],
  [2, 3, 9, 2],
  [3, 9, 4, 9],
  [9, 9, 3, 1]
]
```

### Notes 

* Since in the output the numbers `0-8` are used to determine the amount of adjacent mines, the number `9` will be used to identify the mines instead.

## Day 5 : Recursion: Reversed List Index 

Write a recursive function that filters the items in a list (given as parameter `arr`) by positional parity (odd or even), given as parameter `par`, starting from the opposite end. Return a list of items on odd positions (... 5, 3, 1) or on even positions (... 6, 4, 2) and counting from the last item in the list.

### Examples

```
get_items_at([2, 4, 6, 8, 10], "odd") ➞ [2, 6, 10]
// 2, 6 & 10 occupy the 5th, 3rd and 1st positions from right.
// Odd positions, hence the parity, and from the opposite.

get_items_at(["E", "D", "A", "B", "I", "T"], "even") ➞ ["E", "A", "I"]
// E, A and I occupy the 6th, 4th and 2nd positions from right.
// Even positions, hence the parity, and from the opposite.

get_items_at([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "even") ➞ [")", "*", ^", "$", "@"]

get_items_at(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "even") ➞ ["R", "I", "R", "R", "L"]
```

### Notes

* IMPORTANT: You are advised to solve this challenge via a recursive approach, hence, the very purpose of this challenge. You can check the Resources tab about a few topics on recursion.
* Lists are zero-indexed, so, index+1 = position or position-1 = index.
* Items in the list may contain duplicates. See example #4.
* The last item in the list is always the first item to start a positional count.
* The sequence of the items in the resulting list should be retained (i.e. example #1 - 6 should come after 2 and before 10, example #2 - "A" should come after "E" and before "I").


## Day 6 : Where's the bomb ? 

A large flat field measures 50x50 kilometers. At a time `t = 0`, a bomb explodes somewhere on the field. There are 3 scattered sensors with synchronized clocks that record the exact time (in seconds) that the sound of the exploding bomb reaches them.

Given the x, y coordinates of each of the 3 sensors and the recorded time of each, find the location of the bomb:

```
bomb([[x1, y1, t1], [x2, y2, t2], [x3, y3, t3]]) ➞ (xb, yb)
# Bomb location
```

### Examples 

```
bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]]) ➞ (0, 25)

bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]]) ➞ (0, 0)

bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]) ➞ (21, 13)

bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]]) ➞ (8, 35)
```

### Notes

* The origin is at one corner of the square field so all the coordinates are positive integers in km units.
* The bomb's coordinates are integers.
* The speed of sound in air is 0.343 km/sec.

