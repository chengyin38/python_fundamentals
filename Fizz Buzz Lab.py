# Databricks notebook source
# MAGIC %md 
# MAGIC # Fizz Buzz Lab
# MAGIC 
# MAGIC * Write a function called `fizzBuzz` that takes in a number. 
# MAGIC * If the number is divisible by 3 print `Fizz`. If the number is divisible by 5 print `Buzz`. If it is divisible by both 3 and 5 print `FizzBuzz` on one line.
# MAGIC * If the number is not divisible by 3 or 5, just print the number.
# MAGIC 
# MAGIC HINT: Look at the modulo (`%`) operator.

# COMMAND ----------

# TODO

# COMMAND ----------

# ANSWER
def fizzBuzz(i):
  if (i % 5 == 0) and (i % 3 == 0):
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)

# COMMAND ----------

# MAGIC %md 
# MAGIC This function expects a numeric type. If it receives a different type, it will throw an error. 
# MAGIC 
# MAGIC * Add a check so that if the input to the function is not numeric (either `float` or `int`) print `Not a number`.
# MAGIC 
# MAGIC HINT: Use the `type()` function.

# COMMAND ----------

# TODO

# COMMAND ----------

# ANSWER
def typeCheckFizzBuzz(i):
  if type(i) == int or type(i) == float:
    if (i % 5 == 0) and (i % 3 == 0):
      print("FizzBuzz")
    elif i % 5 == 0:
      print("Buzz")
    elif i % 3 == 0:
      print("Fizz")
    else:
      print(i)
  else:
    print("Not a number")

# COMMAND ----------

# MAGIC %md But what if the argument passed to the function were a list of values? Write a function that accepts a list of inputs, and applies the function to each element in the list.
# MAGIC 
# MAGIC A sample list is provided below to test your function.

# COMMAND ----------

my_list = [1, 1.56, 3, 5, 15, 30, 50, 77, "Hello"]

# COMMAND ----------

# TODO

# COMMAND ----------

# ANSWER
def listFizzBuzz(my_list):
  for i in my_list:
    if (type(i) == int) or (type(i) == float):
      if (i % 5 == 0) and (i % 3 == 0):
        print("FizzBuzz")
      elif i % 5 == 0:
        print("Buzz")
      elif i % 3 == 0:
        print("Fizz")
      else:
        print(i)
    else:
      print("Not a number")
      
listFizzBuzz(my_list)
