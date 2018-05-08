'''
106/5/8
APCS10603APCSImplementation.pdf
question 2
author: yiyu0x
'''
many = int(input())
friends = list(map(int,input().split()))

group = []
small_group = []
visited = []
source = 0
while(True):

    if len(visited) == many:
        break
    if source not in visited:

        small_group.append(source)
        visited.append(source)
        source = friends[source]

        if source in small_group:
            group.append(small_group)
            small_group = []
    else:
        source += 1
################output################
for i in group:
    for j in i:
        print(j,end=' ')
    print()

print('many of group: ',len(group))