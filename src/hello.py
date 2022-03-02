

def hello(name = None, preferred_language="en"):
    if preferred_language == "sv":
        print(f"Hej, {name}!")
    else:
        print(f"Hello, {name}!")