def f(n):
    a=0
    b=1
    i=3
    result=0
    if n == 1:
        return a
    elif n == 2:
        return b
    while i <= n:
        result= a+b
        a=b
        b=result
        i+=1
    return result

if __name__ =="__main__":
    print(f(5))
