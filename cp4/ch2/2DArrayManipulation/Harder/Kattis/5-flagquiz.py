question = input()

n = int(input())

alternatives = []

for i in range(n):
    alternative = input()
    alternatives.append(alternative)

amount_of_changes = {}

for alternative in alternatives:
    global_alternative_split = alternative.split(", ")
    changes_list = []
    for i in range(len(alternatives)):
        changes = 0
        if alternative != alternatives[i]:
            local_alternative_split = alternatives[i].split(", ")
            for j in range(len(global_alternative_split)):
                if global_alternative_split[j] != local_alternative_split[j]:
                    changes += 1
        if changes > 0:
            changes_list.append(changes)
            
    amount_of_changes[alternative] = max(changes_list)

minimun = 1000

for alternative in alternatives:
    if amount_of_changes[alternative]<minimun:
        minimun = amount_of_changes[alternative]


for alternative in alternatives:
    if minimun==amount_of_changes[alternative]:
        print(alternative)

"""In this problem, i misread and didnt full understand the problem. I thought that the question of this problem
was to find the alternative with the least amount of changes respect to ALL the other alternatives.
In my first approeaches i was trying to sum the amount of changes of each alternative with all the other alternatives
and the alternative with the least sum of changes would be the answer. But this was wrong, because the question was
to find the maximun amount of changes of each alternative with all the others, once i had this amount, i had to find the
minimum of all the maximuns. I was able to solve this problem by creating a dictionary with the amount of changes of each
alternative with all the others, and then i found the minimum of all the maximuns.
"""

    



    


                    
            
        
