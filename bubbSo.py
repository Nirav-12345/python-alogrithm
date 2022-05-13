def bubble_sort(list):
    n=len(list)
    # Looping from size of array from last index[-1] to index [0]
    for i in range(n-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                # swapping data if the element is less than next element in the array
                list[j], list[j+1] = list[j+1] ,list[j]








if __name__=="__main__":
    
list=[4,1,2,3]
bubble_sort(list)
print(list)



