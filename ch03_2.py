def funnydivision(anum):
    try:
        if anum == 13:
            raise ValueError("13 not good no they say")
        return 100/anum
    except(ZeroDivisionError, TypeError):
        print("input number and not zero")
    except(ValueError):
        print("Not again man")
        raise 

for val in ("hello", 0, 50, 13):
    print(funnydivision(val))