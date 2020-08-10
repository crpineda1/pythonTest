
# *** notes from introductory class in python

# downloaded pythong from python.org
# to run python environment in CLI type python 3, will show verion of python installed
# to exit python environment => quit()

# to run python file in CLI type python3 [file]

#  print("hello world")

# check is to take an input from the CLI -  inputs are in strings
check = input("how much was your meal?")
print(type(check))
# float() is convert the input to a float
check = float(check)
# type() is to check the data tyope
print(type(check))

# apparently snake case is customary with python
tax_rate = 0.08
tip_rate = 0.20

tax = check * tax_rate
tip = check * tip_rate


total = check + tax + tip
# print is similar to console.log (or p/puts/print for ruby)
print("Your total is ${:.2f}".format(total))
# interpolation is done by ${} and .format() at the end for any amounts of instances
# :.2f is to set the format of the float to 2 decimals
print("Your tax rate is ${} and tip rate is  is ${}".format(tax_rate,tip_rate))



# test
