# Great, nimic nu mi-a iesit, am incercat o gramada de variante..pb am erori mari si la conversia valorilor..

# Sa se scrie o functie care primeste in numar nedefinit de parametri si sa se calculeze suma parametrilor
# care reprezinta numere intregi sau reale

import math
def get_function(*args):
    if type(args) == int or type(args) == float:
        return sum(args)
    else:
        args == 0
        return sum(args)

my_fct = get_function(1, 3, 1.0, "bb")
print(my_fct)

# Sa se scrie o functie recursiva care primeste ca parametru un numar intreg si returneaza:...

def get_sum(n):
    sum1 = 0
    sum_even = 0
    if n == 0:
        return 0

    elif n != 0:
        sum1 == n + get_sum(n-1)

        for i in range(0, n+1):
            if i % 2 == 0:
                sum_even == n + get_sum(n-1)
    return sum1 and sum_even

print(get_sum(7))

# Sa se scrie o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un numar intreg,
# altfel returneaza valoarea 0.

number1 = input("Choose a number, please: ")
def func_input(number1):
    if type(number1) == int:
        return number1
    else:
        return 0

print(func_input(number1))