# 100-days-100-problems

This repository contains 100 problems solved in a span of 100 days. The goal of this project is to have the habit of coding daily.

Chosen Programming Language : Python

## DAY 1 : Retail store

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

