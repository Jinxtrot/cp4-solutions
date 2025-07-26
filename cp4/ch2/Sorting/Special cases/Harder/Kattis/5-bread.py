def sort_breads(breads : list):
    breads_positions = {}

    for index,bread in enumerate(breads):
        breads_positions[bread] = index
    
    print(breads_positions)


number_breads = int(input())

breads = list(map(int, input().split()))
final_breads_sorted = list(map(int, input().split()))

for index,bread in enumerate(breads):
    print("Help")