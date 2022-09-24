def totalCount(n):
    dic = {}
    if n is None:
        return None
    lst = [1,2,3,4,5,6,7,8,9]    
    count = 0
    
    for i in range(len(lst)):  
        for j in range(len(n)):
            if n[j] % lst[i]== 0: 
                count += 1
            dic[i + 1] = count
        count = 0          
    print(dic)


if __name__ == "__main__":
    n = [1,2,8,9,12,46,76,82,15,20,30]
    totalCount(n)