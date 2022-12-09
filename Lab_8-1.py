#Author: Sean Salafia 12/2/22

def num_sum (number):
    #create a starting sum for the for function to add to
    cumulative_sum = 0
    #for loop with range function to run a function finding each iteration of numbers, then adding that to the starting sum.
    for x in range(number + 1):
        cumulative_sum += x
    return cumulative_sum

#Test cases
print(num_sum(5)) == 15
print(num_sum(4)) == 10
print(num_sum(3)) == 6
    
