

def hello(name = None, preferred_language="en"):
    if preferred_language == "sv":
        print(f"Hej, {name}!")
    else:
        print(f"Hello, {name}!")


def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))