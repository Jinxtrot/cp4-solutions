first_group = True

while True:
    group = []
    while True:
        try:
            word = input()
            if not word.isalpha():
                break
            group.append(word)
        except EOFError:
            break

    if len(group) == 0:
        break

    if not first_group:
        print()
    first_group = False

    group.sort(key=lambda x: x[::-1])

    max_len = max(len(word) for word in group)
    for word in group:
        print(f"{' ' * (max_len - len(word))}{word}")

"""
This problem was easy regarding the sorting part and printing the words in the correct format. But i didnt have experience working with EOFError.
In my first submission i get it right but i was printing a blank line at the end of the output. I fixed it by adding a condition to check if the group is empty and break the loop.
I also added a condition to check if the group in case needed to print a blank line before the next group and make sure the line was printed before the next sorted group. Not in the end of the output.
"""