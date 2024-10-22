def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

# Example usage:

stack = [10, 20, 30, 40, 50, 60]
reverse_stack(stack)
print(stack)  

# Output should be [60, 50, 40, 30, 20, 10]
