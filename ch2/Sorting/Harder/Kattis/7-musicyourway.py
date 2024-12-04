attributes = input().split()

number_of_songs = int(input())

songs = []

for i in range(number_of_songs):
    songs.append(input().split())

number_filters = int(input())

for i in range(number_filters):
    filter = input()

    songs.sort(key=lambda x: x[attributes.index(filter)])

    print(*attributes)
    for song in songs:
        print(*song)
    print()

"""
This was a fun problem to practice sorting. Since python always references to the same list of songs, i didnt have to worry about updating the list after 
each filter. I just had to sort the list of songs based on the index of the filter in the attributes list and since the songs were alredy separated by attributes
and also in the same position as the attributes list, i sorted every song based on the index of the filter in the attributes list. Then i printed the attributes list 
for each unique filter and then printed the songs list. 
"""
    
