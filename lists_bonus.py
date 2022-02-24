# listPython Lists Worksheet (Bonus)
# Setup 
# 1.	Create a new PY file 
# 2.	Create Visual Studio Code launch.json file 

# The following problems will focus on lists but will utilize other concepts you have learned up to this point, including functions, loops, conditionals, and variables.  

# Example of creating a list, creating a function that takes in a single parameter, and calling the function while passing in a list: 
  
# Lists and Functions
# 1.	Write a function that has one parameter: a list
# a.	The list that is passed in needs to be a list of numbers
# b.	Compute the average of the numbers inside the list
# c.	Any numbers in the list that are less than the computed average will be appended into a separate list. That list will then be returned from the function.

def average_num(numbers):
  average = 0
  total = 0
  length_of_list = len(numbers)
  new_list = []
  for num in numbers:
    total += num
  average = total/length_of_list
  print(average)
  for num in numbers:
    if num < average:
      new_list.append(num)
  return new_list

print('##### ex1 #####')
print(average_num([1,3,2,5,7,5,9]))


# 2.	Write a function that has two parameters: a list, a number
# a.	Return the value in the list at the index represented by the number parameter
# b.	If there is no value at the specified index, print to the console “No value here!”

def at_what_index(list, num):
  try:
   if list[num]:
     return list[num]
  except:
     return 'No value here!'

print('##### ex2 #####')
print(at_what_index([33,21,3,76,2,-1,44], 3))



# 3.	Write a function that has one parameter: a list
# a.	The list that is passed in needs to be a list of numbers
# b.	Find the most frequent value in the list and return that value

def most_frequent_value(numbers):
  frequencyCounter = {}
  array_of_keys = []
  array_of_frequencies = []
  for num in numbers:
    try:
      frequencyCounter[num] += 1
    except:
      frequencyCounter[num] = 1

  for key in frequencyCounter:
      array_of_keys.append(key)
      array_of_frequencies.append(frequencyCounter[key])
  # print(array_of_keys) 
  # print(array_of_frequencies)
  max_frequency = max(array_of_frequencies)
  index = array_of_frequencies.index(max_frequency)
  return array_of_keys[index]


print('##### ex3 #####')
print(most_frequent_value([1,1,1,1,3,4,6,7]))

# 4.	Write a function that has two parameters: a list, a list
# a.	Both lists that are passed in should contain the first names of people
# b.	Iterate over the lists comparing the values at each index from one list to the other. If there is a matching name in both lists, return that name from the function
# c.	For example: [“Nevin”, “David”, “Mike”] and [“Brett”, “Mike”, “Charles]
# i.	“Mike” would be returned from the function because it is a match in both lists

def match_name(names1, names2):
  for name in names1:
    if name in names2:
      return name
    

print(match_name(['Nevin', 'David', 'Mike'], ['Brett', 'Mike', 'Charles']))
