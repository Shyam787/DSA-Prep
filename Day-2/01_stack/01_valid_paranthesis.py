def isValid(s):

    stack = []
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    for ch in s:

        if ch in '({[':
            stack.append(ch)
        
        else:
            if not stack:
                return False
            
            top = stack.pop()
            
            if top != mapping[ch]:
                return False
    
    return len(stack) == 0

s = '{[()]}'

print(isValid(s))