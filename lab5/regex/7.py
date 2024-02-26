snake_case=str(input())
parts=snake_case.split('_')
camel_case=parts[0]+''.join(word.capitalize()for word in parts[1:])
print(camel_case)