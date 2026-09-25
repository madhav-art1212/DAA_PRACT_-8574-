def bubble_sort(lst):
    
    size = len(lst)
    for i in range(size):
        swapped = False

        for j in range(size-i-1):
            if(lst[j]>lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swapped = True
        
        if not swapped:
            break
    return lst
print(bubble_sort([1,2,4,9,6]))
