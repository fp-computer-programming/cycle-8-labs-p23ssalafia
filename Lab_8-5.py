# Author: Sean Salafia 8/7/2022

def count_a(word):
    #Start count at 0
    count = 0
    # Crate function to look for charachter in a word and add +1 to the count
    for charachter in word:
        # If the character is an 'a' or an 'A', increase count
        if charachter == 'a' or charachter == 'A':
            count += 1

    # Return the final count
    return count

print(count_a("Aardvark")) == 3
#-------------------------------------------------------------------------------------------------------------------------------------
#8-6

def factorial(num):
    count = 1
    for n in range(1, num+1):
        count *= n
    return count

print(factorial(500))
