def sift_down(arr, root, bottom):
    while root*2 <= bottom:
        if root*2 == bottom:
            newr = root*2
        elif arr[root*2-1]>arr[root*2]:
            newr = root*2
        else:
            newr = root*2 + 1
 
        if arr[root-1] < arr[newr-1]:
            arr[root-1], arr[newr-1] = arr[newr-1], arr[root-1]
            root=newr
        else:
            break
 
for i in range( len(arr)/2,  0, -1 ):
    sift_down(arr, i, len(arr))
for i in range( len(arr), 0, -1 ):
    arr[i-1], arr[0] = arr[0], arr[i-1]
    sift_down(arr, 1, i-1)
 
## Test if result is correct
print (sol==arr)
