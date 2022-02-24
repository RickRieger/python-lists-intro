# 1.	Write a function that has one parameter. When you call the function, you will be passing in a list of strings. 
# a.	Print to the console the value at the 0 index of the list
# b.	Return the value at the 0 index of the list

def my_func(list_of_strings):
  single_item = list_of_strings[0]
  print(single_item)
  return single_item

print('#####  Exercise1  #####')  
result1 = my_func(['sometimes', 'I', 'like', 'to', 'play', 'music'])
print(result1)

# 2.	Write a function that has one parameter. When you call the function, you will be passing in a list of strings that represent different colors -- create a list and append the following values into the list: “blue”, “red”, “white”, “green”, “yellow”
# a.	Prompt the user to enter a color.
# b.	Iterate over the list. If the user inputted color matches any of the colors in the list, print to the console “You found my chosen color!”

def my_func2(colors):
  list_to_append = ['blue', 'red', 'white', 'green', 'yellow']
  for color in list_to_append:
    colors.append(color)
  users_color = input('Please provide a color:')
  for color in colors:
    if users_color.lower() == color.lower():
      print('You found my chosen color!')


print('#####  Exercise2  #####')  

print(my_func2(['black', 'orange', 'brown', 'pink', 'gray']))

# 3.	Write a function that has one parameter. When you call the function, you will be passing in a list of numbers.
# a.	Iterate over the list and add up all of the numbers inside of it
# b.	If the sum of the numbers is even, return string “Even” from the function
# c.	If the sum of the numbers is odd, return string “Odd” from the function

def add_all_nums_in_list(numbers):
  total = 0
  for num in numbers:
    total += num
  if (total % 2) == 0:
    print('Even')
  else: print('Odd')


print('#####  Exercise3  #####') 
print(add_all_nums_in_list([2, 6, 1, 3, 1]))


# 4.	Write a function that has two parameters. The first parameter will represent a list, the second parameter will represent a number.
# a.	The list that is passed in needs to be a list of numbers
# b.	Iterate over the list and print to the console each value in the list that is greater than the number parameter

def greater_than_this_num(list_of_nums, num_passed):
  for num in list_of_nums:
    if num > num_passed:
      print(num)
 

print('#####  Exercise4  #####')  
result4 = greater_than_this_num([2, 6, 11, 13, 1], 10)
print(result4)




