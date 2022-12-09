# Author: Sean Salafia 8/7/2022


def count_a(word):
    x = 0
    a = 0
    while a in word:
        x += 1
    return x

print (count_a ("Banana"))

