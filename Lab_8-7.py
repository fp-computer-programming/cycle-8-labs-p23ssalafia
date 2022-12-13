# Author: Sean Salafia 8/7/2022

def is_palindrome(word):
    return word[::-1] == word

print (is_palindrome("racecar"))
print (is_palindrome("level"))
print (is_palindrome("asdfghjkllkjhgfdsa"))
print (is_palindrome("Cloudy"))
