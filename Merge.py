def merge(a1,a2):
    c=[]
    x=0
    y=0

    while (x<len(a1) and y<len(a2)):
        if(a1[x]<a2[y]):
            c.append(a1[x])
            x+=1
        else:
            c.append(a2[y])
            y+=1

    while (x<len(a1)):
        c.append(a1[x])
        x+=1

    while (x<len(a2)):
        c.append(a2[y])
        y+=1
        return c

def sort(arr):
    if (len(arr)==1):
        return arr
    mid = (len(arr)) // 2
    a1 = sort(arr[:mid])
    a2 = sort(arr[mid:])
    return merge(a1, a2)


arr=[2,3,1,5,4,6,8,10,7,9]
print(sort(arr))

