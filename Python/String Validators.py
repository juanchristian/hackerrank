string = list(str(input()))

def do(method):
    for item in string:
        response = []
    
        if method(item):
            return True
    return False    
    
for item in map(do, [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]):
    print(item)