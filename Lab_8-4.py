#Author: Sean Salafia

def cumulative_sum(x):
    #where the sum will be counted
    total = 0
    #starting value for the while loop
    start_count = 0
    while start_count < int(x):
        start_count += 1
        total += start_count
    return total

#Test cases
print (cumulative_sum(3)) == 6 
print (cumulative_sum(50)) == 1275 
print (cumulative_sum(7)) == 28

