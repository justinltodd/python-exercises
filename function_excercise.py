#!/usr/bin/python
print("")

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

print("")

def c_to_f(c_temp):
  f_temp = c_temp  * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

print("")

def get_force(mass, acceleration):
  force = mass * acceleration
  return force
train_force = get_force(mass = train_mass, acceleration = train_acceleration)
print(train_force)

print("")

print("The GE train supplies " + str(train_force) + " Newtons of force.")

print("")

def get_energy(mass, c):
  energy = mass * c ** 2
  return energy
bomb_energy = get_energy(bomb_mass, 3*10**8)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

print("")

def get_work(mass, acceleration, distance):
    force = mass * acceleration
    work = force * distance
    return work
train_work = get_work(mass = train_mass, acceleration = train_acceleration, distance = train_distance)
print(train_work)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
print("")

def average(num1, num2):
  average = (float(num1) + float(num2)) / 2
  return average

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
print("")

def tenth_power(num):
  power = num ** 10
  return power

# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
print("")

# introduction function here:
def introduction(first_name, last_name):
    name = last_name + ", " + first_name + " " + last_name
    #print(last_name + ", " + first_name + " " + last_name)
    return name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
print("")

# square_root function here with math or without:
import math
def square_root(num):
    root = num ** 0.5
    #root = math.sqrt(num)
    return root

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10
print("")

# Write your tip function here:
def tip(total, percentage):
  payment = float(percentage) / float(100) * total
  return payment

# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
print("")

# Write your win_percentage function here:
def win_percentage(wins, losses):
  average = float(wins) / (float(wins) + float(losses)) * 100
  return average

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
print("")

# Write your remainder function here:
def remainder(num1, num2):
  remainder = (num1 * 2) % (num2 / 2)
  return remainder

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
