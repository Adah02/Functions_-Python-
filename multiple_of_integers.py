def multiple(first_input,second_input):
  multiple_of_inputs = 0
  for i in range(second_input):
    multiple_of_inputs += first_input 
  return multiple_of_inputs


first_input = int(input('Enter first number: '))
second_input = int(input('Enter second number: '))
result = multiple(first_input,second_input)
print(result)
