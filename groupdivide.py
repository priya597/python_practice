import math


T = input()
newList = list(map(int, T.split()))
print(newList)
GroupA = 0
GroupB = 0
newlistLen = len(newList);
if(newlistLen <= 1):
    GroupA += newList[-1];
    print(GroupA)
else: 
    for i in range(len(newList)):
        print(newlistLen/2)
        if( i < newlistLen/2):
            GroupA += newList[i];
        else:
            GroupB += newList[i];

    print(GroupA)
    print(GroupB)