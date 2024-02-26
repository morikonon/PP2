camel_case=str(input())
snake_case=''
for char in camel_case:
    if char.isupper() and snake_case:
        snake_case +='_'
        snake_case += char.lower()
print(snake_case)