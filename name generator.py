def calfact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1) # type: ignore
    factorial=calfact(2)
    print("the factorial of the number is= ",factorial)
    


