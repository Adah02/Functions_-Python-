def cube(user_input):
  cube_of_number = ((user_input)**(3)) 
  return cube_of_number


user_input = int(input('Enter number: '))
result = cube(user_input)
print(result)
