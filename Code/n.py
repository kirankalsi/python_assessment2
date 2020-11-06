def four(input1, input2):
    return ''.join(''.join(f for f in tup) for tup in zip(input1, input2))






print(four("String","Fridge"))
print(four("Dog","Cat"))
print(four("True","Tree"))
print(four("return","letter"))