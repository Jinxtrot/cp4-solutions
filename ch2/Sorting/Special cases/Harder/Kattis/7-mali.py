testcases = int(input())

a = []
b = []
a_min = 100001
b_max = 0

for i in range(testcases):
    a_entry, b_entry = list(map(int, input().split()))
    a.append(a_entry)
    b.append(b_entry)
    if a_entry < a_min:
        a_min = a_entry
    if b_entry > b_max:
        b_max = b_entry
    print(a_min+b_max)

    
