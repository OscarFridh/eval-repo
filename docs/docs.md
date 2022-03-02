# Functions in this repo

This repository only contains one simple function called hello. The first parameter is the name of the person to greet. The second parameter is the preferred language to use. Currently the supported languages are English and Swedish. The following code will print: "Hej, Szymon!":
```python
hello('Szymon', preferred_language='sv')
```

If no second argument is provided, the function will default to English. The following code will print: "Hello, Oscar!"
```python
hello('Oscar')
```
