import re

def is_valid_expression(expression):
    # Define valid characters and patterns
    valid_chars = set('0123456789+-*/() ')
    operators = set('+-*/')
    digits = set('0123456789')
    
    # Check for invalid characters
    for char in expression:
        if char not in valid_chars:
            return False
    
    # Check for balanced parentheses
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    if stack:
        return False
    
    # Check for forbidden substrings
    forbidden_substrings = ['(/', '-)', '//', '*/', '(*', '*)']
    for substring in forbidden_substrings:
        if substring in expression:
            return False
    
    # Check for valid operator usage
    # Ensure no two operators are adjacent (e.g., "2++3" or "2*/3")
    for i in range(len(expression) - 1):
        if expression[i] in operators and expression[i + 1] in operators:
            return False
    
    # Ensure no operator starts or ends the expression
    if expression[0] in operators or expression[-1] in operators:
        return False
    
    # Ensure no empty parentheses
    if re.search(r'\(\s*\)', expression):
        return False
    
    # Ensure numbers are valid
    # This is a simplified check; a full implementation would require a proper tokenizer
    tokens = re.findall(r'\d+|[\+\-*/()]', expression)
    for token in tokens:
        if token not in operators and token != '(' and token != ')' and not token.isdigit():
            return False
    
    return True

# Main program
if __name__ == "__main__":
    # Take input from the user
    expression = input("Enter an arithmetic expression: ")
    
    # Remove any leading/trailing whitespace
    expression = expression.strip()
    
    # Check if the expression is valid
    if is_valid_expression(expression):
        print("The expression is valid.")
    else:
        print("The expression is invalid.")
