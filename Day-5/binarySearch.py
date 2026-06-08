nums=list(map(int,input().split()))
k=int(input())
l,h=0,len(nums)-1
nums.sort()
print(nums)
while l<=h:
    mid=(l+h)//2
    if nums[mid]==k:
        print("Element",k,"found at ",mid)
        break
    elif nums[mid]<k:
        l=mid+1
    else:
        h=mid-1
else:
    print("Element not found")