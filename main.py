import random

'''
card values: 
ace = 1
jack = 11
queen = 12
king = 0
'''

#set up deck
deck = []

#4 suits for each card
for _ in range (4):
  deck.extend([1,2,3,4,5,6,7,8,9,10,11,12,0])

#initialize variables
turns = 1000
total_points = 0

#run simulation
for turn in range (turns):
  die1 = random.randint (1,6)
  die2 = random.randint (1,6)
  
  dice_sum = die1 + die2
  
  draw = random.sample(deck,5)
  
  if die1 in draw or die2 in draw or dice_sum in draw:
    points = 0
  else:
    points = dice_sum

  total_points+= points
  print(f"Turn: {turn+1} Points: {points} ")