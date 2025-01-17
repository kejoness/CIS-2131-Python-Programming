# Kayla Jones
# Project 1

# ask user for length and width of fenced area
fenced_area_width = int(input("What is the width of your fenced area? (whole numbers only, please): "))
fenced_area_length = int(input("What is the length of your fenced area? (whole numbers only, please): "))

# ask user how far apart they'd like their posts to be
post_distance = int(input("How far apart would you like your posts to be? (whole numbers only, please): "))

# check if length or width is evenly divisible by the post distance
if fenced_area_length % post_distance != 0 or fenced_area_width % post_distance != 0:
    print("Your fence's length/width is not evenly divisible by your post distance. Please try again.")
    exit()

# calculate the number of posts the user must buy
posts_needed_to_buy = (fenced_area_length / post_distance) * (fenced_area_width / post_distance)

# ask the user how long they'd like their board to be and
# check if the board length is less than the post distance
board_length = int(input("How long would you like your board to be? (whole numbers only, please): "))
if board_length < post_distance:
    print("Your board length is too small. Please try again.")
    exit()

# calculate the number of boards needed to build the fence
number_of_boards_needed = int(fenced_area_length / board_length)

# if there is a remainder, add one to the number of boards needed
if fenced_area_length % board_length != 0:
    number_of_boards_needed += 1

# ask the user how many boards they want to run across each post
boards_per_post = int(input("How many boards would you like to run across each post? (whole numbers only, please): "))

# ask user for post and board costs
cost_per_post = float(input("How much does a single post cost? (no $ please): "))
cost_per_board = float(input("How much does a single board cost? (no $ please): "))

# show total number of boards and posts needed, post and board costs, and total costs for the project
total_posts_cost = cost_per_post * posts_needed_to_buy
total_boards_cost = cost_per_board * number_of_boards_needed
total_cost = total_boards_cost + total_posts_cost

print("Summary:")
print("Posts required: ", posts_needed_to_buy)
print("Boards required: ", number_of_boards_needed)
print("Total cost of posts: ", total_posts_cost)
print("Total cost of boards: ", total_boards_cost)
print("Grand total: ", total_cost)
