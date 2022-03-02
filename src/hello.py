

def hello(name = None, preferred_language="en"):
    if preferred_language == "sv":
        print(f"Hej, {name}!")
    else:
        print(f"Hello, {name}!")


def fib(N):
	golden_ratio = (1 + 5 ** 0.5) / 2
	return int((golden_ratio ** N + 1) / 5 ** 0.5)