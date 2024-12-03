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
            
    amount_of_changes[alternative] = changes_list

print(amount_of_changes)


    



    


                    
            
        
