number_house = 1

while True:
    directions = {"Right": (1, 0), "Down": (0, 1), "Left": (-1, 0), "Up": (0, -1)}
    sizes = input()
    if sizes == "0 0":
        break
    w, l = map(int, sizes.split())
    house = []
    for i in range(l):
        house.append(input())
        if "*" in house[i]:
            x, y = house[i].index("*"), i
            if x == 0:
                direction = "Right"
            elif x == w-1:
                direction = "Left"
            elif y == 0:
                direction = "Down"
            else:
                direction = "Up"
    print("HOUSE", number_house)
    number_house += 1
        
    while True:
        x += directions[direction][0]
        y += directions[direction][1]
        if house[y][x] == "x":
            house[y] = house[y][:x] + "&" + house[y][x+1:]
            break
        elif house[y][x] == "/":
            if direction == "Right":
                direction = "Up"
            elif direction == "Down":
                direction = "Left"
            elif direction == "Left":
                direction = "Down"
            else:
                direction = "Right"
        elif house[y][x] == "\\":
            if direction == "Right":
                direction = "Down"
            elif direction == "Down":
                direction = "Right"
            elif direction == "Left":
                direction = "Up"
            else:
                direction = "Left"
    for line in house:
        print(line)
                
    
"""
This problem was very interesting and fun to solve. It was very move forward to solve this problem, i had to create a dictionary
with the possible directions and how they would affect the x and y coordinates. Then i had to find the initial position of the
door (*) and depending on the position of the door, I would know the initial direction. Then depending in the direction, i would use
my dictionary to know how to move the x and y coordinates. I would keep moving the x and y coordinates until i found a wall (x) which means
that i found the exit of the house. I would change the wall for a "&" and print the house. I would keep doing this until i found the exit.
If i found a mirror (/ or \) i would change the direction. This was easy because i alredy knew the actual direction and if the mirror was 
(\ or /) i would change the direction like it would be in a real mirror. I would keep doing this until i found the (x) wall.
"""