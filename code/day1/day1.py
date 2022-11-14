import numpy as np


class Day1:

    def __init__(self):
        pass

    staticmethod

    def sum_x_first_elements(self, arr, x):
        somme = 0
        for i in range(x):
            somme += arr[i]
        return somme

    def discount(self, shopping_cart):
        if len(shopping_cart) < 3:
            return False
        nb_discounts = len(shopping_cart) // 3
        shopping_cart_sorted = sorted(np.array(shopping_cart))
        discount = self.sum_x_first_elements(shopping_cart_sorted, nb_discounts) / sum(shopping_cart)
        shopping_cart = np.array(list(map(lambda x: round(x - discount*x,2), shopping_cart)))
        return shopping_cart
