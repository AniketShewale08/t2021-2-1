def seriesOfNums(n):
    count = 1
    max_rng = 9999999
    for i in range(max_rng):
        if count > n:
            break
        else:
            if i % 2 == 1:
                print(i, end=", ")
            else:
                continue
        count += 1   

if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    seriesOfNums(n)
    

