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

