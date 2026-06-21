def mergesort(arr,cnt):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        mergesort(left,cnt)
        mergesort(right,cnt)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                cnt+=len(left)-i
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return cnt
arr=list(map(int,input().split()))
cnt=0
inversion=mergesort(arr,cnt)
print(inversion)
