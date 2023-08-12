def cough_dec(func):


    def func_wrapper():
        print("*cough*")
        func()
        print("*cough*")

    return func_wrapper()

@cough_dec
def question():
    print("Can you give me a discount on that?")

@cough_dec
def answer():
    print("Yes! you can get some discount after your purchase is over N100,000")