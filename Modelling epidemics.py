# Epidemiological models are an essential tool for understanding Covid-19 pandemic outbreaks. For instance, public health professionals and policy makers rely on epidemiological models as they make key decisions. Those decisions include which social distancing measures to put in place, how to best utilise resources within a health system, and what other measures can be taken to reduce COVID-19’s impact on their communities.

# A simple estimate of the daily number of cases uses the normal distribution can be found in [1]. This illustration is a basic version of an epidemiological model—a system of mathematical equations used to track the spread of a pathogen and predict how an epidemic might unfold. The epidemiologists have estimated that the daily number of cases are normally distributed with a mean of 
# μ
#  and a standard deviation of 
# σ
# . That is, the number of cases on day 
# x
#  can be estimated by

# f
# (
# x
# )
# =
# n
# ×
# e
# −
# (
# x
# −
# μ
# )
# 2
# 2
# σ
# 2
# where 
# x
#  is taken to be an integer in the range 
# 0
# …
# 56
#  (8 weeks) and 
# f
# (
# x
# )
#  is proportional to the probability density function (PDF) of the normal distribution[2]. 
# n
#  is the theoretical peak number of patients in the hospital.

# Write a program that accepts three float numbers n, mu and sigma, followed by an int number x, and output an estimate of the number of cases on day x, as an integer.

# First sample session with the program:

# n? 270
# mu? 23
# sigma? 17.5
# x? 50
# Estimated number of cases on day 50 is 82
# ​
# Second sample session with the program:

# n? 1000
# mu? 35
# sigma? 11.25
# x? 20
# Estimated number of cases on day 20 is 411
# ​
# see https://www.path.org/articles/making-sense-covid-19-models/
# see https://en.wikipedia.org/wiki/Normal_distribution



def probility_density_function(n,mu,sigma,x):
  
  import math
  #For square root using **.
  power_square = - ((x - mu)**2)/(2 * sigma**2)
  #The math.exp() method returns E raised to the power of x (Ex).
  exponent = n * math.exp(power_square) 
  return round(exponent)


#call the function 
n = float(input("n? ")) # n = Peak number of patients.
mu = float(input("mu? "))# u or mu = Daily number cases.
sigma = float(input("sigma? "))# @ or sigma = Standard devaition of normal distribuation.
x = int(input("x? ")) # x = The day for estimate the number of cases.
estimate = probility_density_function(n,mu,sigma,x)
#estimnate = round(exponent)
print (f"Estimated number of cases on day {x} is {estimate}")


