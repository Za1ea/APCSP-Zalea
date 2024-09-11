# Project 1: Space Travel Calculator

# Step 1: Print the message “Welcome to the space travel calculator.” to the console.

# Step 2: Create a variable called distance. Ask the user to input the distance to their destination (in light-years). Make sure to convert their answer to a number.

# Step 3: Create a variable called speed. Ask the user to input the speed of their spaceship (as a fraction of the speed of light). Make sure to convert their answer to a float value (decimal number)

# Step 4: Create a variable called time. Calculate the time using the formula distance / time. Set the time to this calculation.

# Step 5: Print a message telling the user how much time it would take to reach their destination.

print('Welcome to the space travel calculator.')

distance = float(input('Distance to your destination (light years): '))
speed = float(input('Speed of your spaceship (fraction of speed of light): '))

time = distance / speed

print(f'It will take {time} years to reach your destination.')

# Project 2: Restaurant Ranker
# You just got hired by restaurantboxd, the restaurant rating app. Your first task is to create a program that asks a user for their favorite restaurants and store these restaurants as a list.

# Step 1: Create a variable called restaurants. This will store the user’s favorite restaurants.

# Step 2: Create a loop that will continue to ask the user for their favorite restaurant. This loop should break once the user enters the word “stop”.

# Step 3: During each iteration of the loop, you should ask the user for a new restaurant and add it to the restaurants list.

# Step 4: Once the loop is complete, print out the list to the console.
restaurants = []
message = 'What is one of your favorite restaurants? Type "stop" to stop.\n'
restaurant = input(message)
while restaurant != 'stop':
  restaurants.append(restaurant)
  restaurant = input(message)

print(restaurants)

# Project 3: Rock, Paper, Scissors
# You just applied to a job at Nintendo. For your interview, they want you to code a rock, paper, scissors game but add a fun twist.

# Create a function called playGame() adding whatever fun twist you want. This function must call at least one helper function (using a function inside a function). It’s up to you to decide how you want to organize your code to do this.

# The playGame function should return which user won the game. At the end of your program you should print out a win message based on the return of the playGame function.

# For one point extra credit, ask the user if they want to do best of 3 and use a loop to continue playing until a user has won two games.

import getpass

moves = ['r', 'p', 's']


def get_user_move():
  player1_move = getpass.getpass(
      prompt='Player 1, choose rock (r), paper (p), or scissors (s): ').lower(
      )
  player2_move = getpass.getpass(
      prompt='Player 2, choose rock (r), paper (p), or scissors (s): ').lower(
      )
  return player1_move, player2_move


def check_valid_move(move_1, move_2):
  move_1_idx = 0
  move_2_idx = 0
  try:
    move_1_idx = moves.index(move_1)
    move_2_idx = moves.index(move_2)
  except ValueError:
    print('Invalid move. Please try again. Only input "r", "p", or "s".')
    move_1, move_2 = get_user_move()
    move_1_idx = moves.index(move_1)
    move_2_idx = moves.index(move_2)
  return move_1_idx, move_2_idx


def check_winner(move_1_idx, move_2_idx, player1_pts, player2_pts):
  if move_2_idx - move_1_idx == 1 or move_2_idx - move_1_idx == -2:
    player2_pts += 1
  elif move_1_idx - move_2_idx == 1 or move_1_idx - move_2_idx == -2:
    player1_pts += 1
  return player1_pts, player2_pts


def playGame():
  p1_pts = 0
  p2_pts = 0
  print('Welcome to Rock, Paper, Scissors!')
  best_of_3 = input('Do you want to play best of 3? (y/n) ')

  if best_of_3 == 'y':
    print(
        "Ok, there\'s a twist. You won\'t know who\'s winning until the end.")
    while p1_pts < 2 and p2_pts < 2:
      move_1, move_2 = get_user_move()
      move_1_idx, move_2_idx = check_valid_move(move_1, move_2)
      p1_pts, p2_pts = check_winner(move_1_idx, move_2_idx, p1_pts, p2_pts)
      # print(f'Player 1: {p1_pts} points, Player 2: {p2_pts} points')
    if p1_pts == 2:
      print('Player 1 wins!')
    else:
      print('Player 2 wins!')

  else:
    move_1, move_2 = get_user_move()
    move_1_idx, move_2_idx = check_valid_move(move_1, move_2)
    p1_pts, p2_pts = check_winner(move_1_idx, move_2_idx, p1_pts, p2_pts)
    # print(p1_pts, p2_pts)
    if p1_pts > p2_pts:
      print('Player 1 wins!')
    elif p2_pts > p1_pts:
      print('Player 2 wins!')
    else:
      print('It\'s a tie!')


playGame()

total_count = {'aluminum': 135, 'plastic': 102, 'paper': 213}


def sortItems(item_string):
  total_count['aluminum'] += item_string.count('A')
  total_count['plastic'] += item_string.count('P')
  total_count['paper'] += item_string.count('R')


sortItems('AAPAARRPAAPRRP')
print(total_count)