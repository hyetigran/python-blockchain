# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.


def plus_one(fn):
    print(fn(1)+1)


# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
plus_one(lambda x: x*2)
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.


def plus_two(fn, *args):
    for arg in args:
        print(fn(arg)+2)


plus_two(lambda x: x*2, 1, 2, 3, 4, 5, 6)
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.


def plus_three(fn, *args):
    for arg in args:
        print(f"Result: {:^20.2f}".format(fn(arg)+2))
