# def mana(a,b):
#  return a+b
# x = input()
# y = input()
# z=mana(x,y)
# print(z)

import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
