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