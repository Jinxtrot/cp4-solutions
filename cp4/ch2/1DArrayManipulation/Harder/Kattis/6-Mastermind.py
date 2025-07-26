entry = input().split()
length = int(entry[0])
code = entry[1]
guess = entry[2]

r = 0 
s = 0
used_letters = []

for index, letter in enumerate(code):
    if letter == guess[index]:
        r += 1
        pass
    if letter in guess:
        if letter not in used_letters:
            s += min(code.count(letter), guess.count(letter))
            used_letters.append(letter)
    

print(r,s-r)

"""Firstly, i thought about getting the letters that are in the same position
in both strings. Then, i thought in creating a list of used letters to avoid
counting the same letter twice. Finally, i thought about getting the minimum
between the number of times the letter appears in the code and the guess because
we can't count the same letter twice even if it appears more times in the guess, finally since 
i was counting each individual letter that was in the guess and code, i subtracted the number of
right letters from the total number of letters that were in the guess and code to get the number of
letters that were in the wrong position.
"""