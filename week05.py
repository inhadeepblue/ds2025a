def is_valid_parentheses(expression : str) -> bool:  # type hint
    stack = list()
    brackets = {']': '[', '}': '{', ')': '('}
    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack

print(is_valid_parentheses("[({1+2)]}"))
print(is_valid_parentheses("[({1+2})]"))
print(is_valid_parentheses(")1+2()"))
print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((3*2)/2)"))
print(is_valid_parentheses("((3*2/2)"))