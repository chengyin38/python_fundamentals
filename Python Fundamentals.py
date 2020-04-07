# Databricks notebook source
# MAGIC %md
# MAGIC # Python Fundamentals
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC  - Learn Python Fundamentals
# MAGIC    * Variables
# MAGIC    * Print statements
# MAGIC    * Lists
# MAGIC    * For Loops
# MAGIC    * Functions
# MAGIC    * Conditional Statements
# MAGIC    * Types and Type Checking
# MAGIC    
# MAGIC This is a good [reference sheet](http://www.cogsci.rpi.edu/~destem/igd/python_cheat_sheet.pdf) to bookmark. If you want a comprehensive tutorial on how you can use Python, check out this [official tutorial](https://docs.python.org/3/tutorial/) from the Python website. 

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Numbers: Using Python as your calculator! 

# COMMAND ----------

# Hit the run button, or shift + enter
123456/8

# COMMAND ----------

# try giving Python the hardest math problem
2^568

# COMMAND ----------

# MAGIC %md
# MAGIC ### Strings

# COMMAND ----------

'Ice cream' 'is paradise'

# COMMAND ----------

'Ice cream' + 'is paradise'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lists
# MAGIC 
# MAGIC Let's make a list of what everyone ate for breakfast this morning.
# MAGIC 
# MAGIC <img src="https://www.simplyrecipes.com/wp-content/uploads/2018/06/Scrambled-Eggs-2.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]

# COMMAND ----------

# MAGIC %md Let's get the first breakfast element from this list. 
# MAGIC 
# MAGIC **Note:** Everything in Python is 0-indexed, so the first element is at position 0.

# COMMAND ----------

breakfast_list[0]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's get the last breakfast item from this list.

# COMMAND ----------

breakfast_list[-1]

# COMMAND ----------

# MAGIC %md
# MAGIC What if I want the second breakfast item and onwards?

# COMMAND ----------

breakfast_list[1:]

# COMMAND ----------

# MAGIC %md ### 1) Variables
# MAGIC 
# MAGIC As Shakespeare famously wrote: `A rose by any other name would smell as sweet`. A variable in Python simply holds a value - you can call it any name you want (within reason...)!

# COMMAND ----------

simple_math = 8*50
simple_math

# COMMAND ----------

best_food = 'Ice cream'
best_food

# COMMAND ----------

# MAGIC %md ### 2) Print Statements
# MAGIC 
# MAGIC In Databricks/Jupyter notebooks, it will automatically print out the last line of the cell that it evaluates.
# MAGIC 
# MAGIC However, we can force it to print out other components by using a `print` statement. 

# COMMAND ----------

print("Hi there, tell me your hard math answer and the best food.")
print(simple_math)
print(best_food)

# COMMAND ----------

# MAGIC %md 
# MAGIC You can also be more explicit about what you are printing. You can add your variable within your print statement. 

# COMMAND ----------

print(f"The answer to hard math is {simple_math}")
print(f"{best_food} is the best food on earth.")

# COMMAND ----------

# MAGIC %md Try printing this statement: `I need {simple_math} {best_food}`.

# COMMAND ----------

# MAGIC %md ### 3) Conditionals
# MAGIC 
# MAGIC Sometimes, depending on certain conditions, we don't always want to execute every line of code. We can control this through using the `if`, `elif`, and `else` statements. Try changing `name` in the cell below and see the 3 different types of outputs.

# COMMAND ----------

best_food = "ice cream"
ice_cream_count = 1000

if best_food == "ice cream":
  print(f"I want {ice_cream_count} cones of ice cream.")
elif best_food == "":
  print("Tell us your favorite food")
else:
  print("Too bad. No ice cream")

# COMMAND ----------

best_food = "chocolate"

if best_food == "ice cream":
  print(f"I want {ice_cream_count} cones of ice cream.")
elif best_food == "":
  print("Tell us your favorite food.")
else:
  print("Really? Isn't ice cream better?")

# COMMAND ----------

# MAGIC  %md We want print plural forms of a food (try changing `food` to something else)! This requires adding an 's' to the end of a string only if it doesn't already have an 's' there.

# COMMAND ----------

best_food = "chocolate"

if best_food.endswith("s"):
  print(best_food)
else:
  print(best_food + "s")

# COMMAND ----------

# MAGIC 
# MAGIC %md ### 4) For Loops
# MAGIC 
# MAGIC What if we wanted to print every breakfast we had this morning?
# MAGIC 
# MAGIC Loops are a way to repeat a block of code while iterating over a sequence ("for-loop")

# COMMAND ----------

for food in breakfast_list:
  print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC What if I want to count how many letters are there in each word?

# COMMAND ----------

for food in breakfast_list:
  print(f"{food} has {len(food)} letters.")

# COMMAND ----------

# MAGIC %md ### 5) Functions
# MAGIC 
# MAGIC The code above only works with `breakfast_list` but we can generalize it to work with different lists by making a function! A `function` is created with the `def` keyword and uses `return` to give its output.

# COMMAND ----------

# General syntax
# def function_name(parameter_name):
#   block of code that is run every time function is called

# defining the function
def print_length(breakfast_list):
  """
  breakfast_list is a variable that we can use within the function code
  """
  for food in breakfast_list:
    print(f"{food} has {len(food)} letters.")

# execute the function by passing print_foods a list
print_length(breakfast_list)

# COMMAND ----------

breakfast_list = ["bacon", 'sausage', 'yoghurt']

print_length(breakfast_list)

# COMMAND ----------

# MAGIC %md
# MAGIC What if you worry you'd forget what the function needs to be computed? Annotate it! <br>
# MAGIC 
# MAGIC Check out this [reference](https://docs.python.org/3/tutorial/controlflow.html#function-annotations) if you want to learn more!
# MAGIC 
# MAGIC As you can see below, annotating it doesn't affect how the function works at all. But it helps you to recall what the function takes in and outputs later!

# COMMAND ----------

def print_length(breakfast_list: 'list') -> 'string':
  """
  breakfast_list is a variable that we can use within the function code
  """
  for food in breakfast_list:
    print(f"{food} has {len(food)} letters.")
    
    
print_length(breakfast_list)

# COMMAND ----------

# MAGIC %md ### 6) Functions with Multiple Arguments
# MAGIC 
# MAGIC Let's define a function that will add two numbers together.

# COMMAND ----------

ice_cream_count = 1000
chocolate_count = 500

def count_fav_food(x, y):
  total = x + y
  return total

# count_fav_food(x = ice_cream_count, y = chocolate_count)
count_fav_food(ice_cream_count, chocolate_count)

# COMMAND ----------

# MAGIC %md
# MAGIC What if you know that your `chocolate_count` is always going to be 500? You can set a default value!

# COMMAND ----------

def count_fav_food(x, y=500):
  total = x + y
  return total

count_fav_food(123)

# COMMAND ----------

# MAGIC %md
# MAGIC What if you want to calculate the proportion of food to approximately gauge how much you like each one?

# COMMAND ----------

def calculate_percentage(chocolate, ice_cream):
  percentage = chocolate / (ice_cream + chocolate) * 100
  return round(percentage, 2)

print(f"I like chocolate {calculate_percentage(985, 5123)}% of the time.")

percent = calculate_percentage(985, 5123)

# COMMAND ----------

# MAGIC %md
# MAGIC Without function annotation...

# COMMAND ----------

help(count_fav_food)

# COMMAND ----------

# MAGIC %md
# MAGIC With function annotation...

# COMMAND ----------

help(print_length)

# COMMAND ----------

# MAGIC %md ### 7) Types and Type Checking
# MAGIC 
# MAGIC We have been defining quite a number of variables. What if we forget what types are the variables? Don't worry -- we can always check!
# MAGIC 
# MAGIC Here are some of the variables we have defined:
# MAGIC 0. `simple_math`
# MAGIC 0. `percent`
# MAGIC 0. `best_food`
# MAGIC 0. `breakfast_list`

# COMMAND ----------

type(simple_math)

# COMMAND ----------

type(percent)

# COMMAND ----------

type(best_food)

# COMMAND ----------

type(breakfast_list)

# COMMAND ----------

# MAGIC %md
# MAGIC Let's define a new variable.

# COMMAND ----------

YouAreCool = True

# COMMAND ----------

print("She is cool.", YouAreCool)

# COMMAND ----------

type(YouAreCool)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also check the equality of the variables by using `==` (equal) or `!=` (not equal).

# COMMAND ----------

YouAreCool != False

# COMMAND ----------

best_food == 'ice cream'

# COMMAND ----------

best_food

# COMMAND ----------

# MAGIC %md
# MAGIC Summary of types:
# MAGIC 0. An `int` is a numeric type in Python. It is an integer, so a whole number without decimals. 
# MAGIC 0. A `float` is a numeric type in Python. It is basically a number that has decimal places. 
# MAGIC 0. A `String` type is a sequence of characters, such as the food `"chocolate"`. It can be any sequence of characters too, not just words. `"Hello123"` or even `"123"` could also be a string. They are enclosed in quotes.
# MAGIC 0. A `Boolean` type is either True or False.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 8) Append to List / Remove from List 
# MAGIC 
# MAGIC You can add more items to a list later if you wish as well! 

# COMMAND ----------

breakfast_list.append("milk")
breakfast_list

# COMMAND ----------

breakfast_list.remove("milk")
breakfast_list
