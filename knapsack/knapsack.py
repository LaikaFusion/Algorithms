#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# def knapsack_solver(items, capacity):
#   itemsSelected =[]
#   totalValue = 0
#   capcityIntial = capacity
#   sortedItemsValue = valueCalc(items,capacity)
#   for item in sortedItemsValue:
#     if capacity-item["weight"] < 0:
#       continue
#     itemsSelected.append(item['name'])
#     capacity -= item["weight"]
#     totalValue += item["value"]

#   print(sorted(itemsSelected))
#   return {'Value':totalValue,"Size":capcityIntial-capacity,"Chosen":sorted(itemsSelected)}


def knapsack_solver(items,capacity):
  if items == None:
    return
  highestcombination =  {'Value':0,"Size":capacity,"Chosen":[]}
  for item in items:
    itemscopy = items.copy()
    print(itemscopy)

    highestValue = knapsack_solver(itemscopy,capacity-item['weight'])
    highestValue['Value'] += item['value']
    highestValue['Chosen'].append(item['name'])
    if highestValue['Value'] > highestcombination['Value']:
      highestcombination = highestValue

  return highestcombination

def greedy(items,capacity):
  return sorted(items, key=lambda k: k['value'],reverse=True)

 

def valueCalc(items,capacity):
  for item in items:
    item["calcedRatio"] = item["value"]/item["weight"]
  return sorted(items, key=lambda k: k['calcedRatio'],reverse=True)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')