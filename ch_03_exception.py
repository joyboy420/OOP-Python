class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integer could ber added")
        if integer%2:
            raise ValueError("Only even number could be added")
        super().append(integer)

    def no_return():
        print("I am about to raise an exception")
        raise Exception("This is always raised")
        print("This line will never execute")
        return "I won't be returned"

    def call_exceptor():
        print("call_exceptor starts here...")
        no_return()
        print("an exception was raised...")
        print("...so these lines don't run")

    
    try:
        no_return()
    except:
        print("caught an exception")
