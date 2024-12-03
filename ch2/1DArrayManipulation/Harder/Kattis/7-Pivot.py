size = int(input())
numbers = list(map(int,input().split()))

possible_pivots = 0

min_list = [0]*(size+1)
max_list = [0]*(size+1)

max = 0

for index,number in enumerate(numbers):
    if number > max:
        max = number
    max_list[index] = max

min = numbers[size-1]

for index, number in enumerate(numbers[::-1]):
    if number < min:
        min = number
    min_list[size-1-index] = min

for index,number in enumerate(numbers,0):
    if number >= max_list[index] and number <= min_list[index]:
        possible_pivots += 1

print(possible_pivots)


"""With my first three solutions i get correct answer in 5 out of 6 test cases, but i got TLE in the last one.
My error was using min function everytime the min value at the moment was discarded, meaning that i was using it
at most 100,000 at the same moment that i was looping through the list of numbers (Also 100,000 numbers). Meaning that this solution is O(n^2).
I then thought about a different approach. I was always looking for the minimun into the right side and the maximun into the left side of the current number. 
So i thought about creating two temp lists that would store the max value to the left and the min value to the right of the current number. Then i would loop through the list of numbers
and check if the current number was greater than or equal to the max value to the left and less than or equal to the min value to the right. If it was, then it was a possible pivot.
This solution is O(3*n) = O(n)
"""




