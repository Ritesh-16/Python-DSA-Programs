s = '[{(a+b)+(c+d)}]'
#In this i am using python list as Stack
# Balance Paranthesis using real custom stack is not done yet
def balance_paranthesis(s):
    brackets = {')':'(',"}":"{", "]":"["}
    stack = []
    for i in s:
        if i in brackets.values():#checking for opening brackets
            stack.append(i)
        elif i in brackets.keys():#checking for closing brackets
            if not stack or stack.pop() !=  brackets[i]:
                return False
    return not stack
print(balance_paranthesis(s))

