#!/usr/bin/env python3

target={}
tl=8
th=12


symbol='ABT'
t=tl, th


target.update({symbol:t})

symbol='IBM'
t=88, 124

target.update({symbol:t})

print(target)

print(target['ABT'][1])
print(type(target['ABT']))

symbol='ABT'
t=9, 15

target.update({symbol:t})


print(target)

print(target['ABT'][1])
