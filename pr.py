DEFAULT = object()

def pr(times = DEFAULT , text = DEFAULT) :
    if text == DEFAULT :
        text = ""
    
    if times == DEFAULT:
        print(text)
    elif times != DEFAULT:
        [print(text) for i in range(times)]
