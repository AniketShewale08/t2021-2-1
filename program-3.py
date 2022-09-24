def helper(n):
    count = 1
    max_rng = 999999
    for i in range(max_rng):
        if count <= n: 
            if i % 2 == 1:
                print(i, end=", ") 
            else:
                continue
        count += 1

def seriesOfNum(n):
    if n % 2 == 0:
        return helper(n - 1)       
    else:
        return helper(n)         


if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    seriesOfNum(n)