# linear search algorithms
def linearsearch(A, key):
# function takes two parameter A for list and key for search item from the list
    pos = 0
    #pos is position of the item in the list
    flag = False
    #flag is to a boolean that allows us to know if an item is within a list
    
    while pos < len(A) and not flag:
        # while the position is less that lenght of the list which is A
        # and also position is (not flag) which is TRUE   
        if A[pos] == key :
            # assign the item being search for if found in the postion of the 
            #item in the list (A)
            flag = True
            #flag become true
        else:
            pos = pos + 1
            # or keep moving from one element to the next in the list (A) 
    return flag

A = [3,5,57,90,45,20]
found = linearsearch(A, 1)
print("Found element from list: ", found)