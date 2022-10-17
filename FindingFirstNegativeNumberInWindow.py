 
 
array = list(map(int,input().split(' ')))
 
ws = int(input())
n = len(array)
 
i,j,ans=0,0,[]
 
while j<n:
    if array[j]<0:
        ans.append(array[j])
    if j-i+1 < ws:
        j+=1
    elif j-i+1 == ws:
        if ans!=[]:
            print(ans[0])
        else:
            print("none")
        
        if ans!=[] and array[i] == ans[0]:
            ans.pop(0)
        i+=1
        j+=1
        
    
        
        
        
