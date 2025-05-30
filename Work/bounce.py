# bounce.py
#
# Exercise 1.5

'''
A rubber ball is dropped from a height of 100 meters
and each time it hits the ground, it bounces back up to 3/5 the height it fell.
Write a program bounce.py that prints a table showing the height of the first 10 bounces.
'''

# A rubber ball is dropped from a height of 100 meters
initial_drop = 100

# and each time it hits the ground, it bounces back up to 3/5 the height it fell.
rebound_factor = 3/5

# Write a program bounce.py that prints a table showing the height of the first 10 bounces.
bounce_number = 1 # Counts which bounce we're on, hence initialize it to the first bounce
final_bounce = 10

# before we go into bounce #1, set the drop_height used in the loop
drop_height = initial_drop

while bounce_number <= final_bounce:  # For the bounce we're on is upto and including the final bounce
    # take the drop_height and calculate the new_height
    bounced_back_to = drop_height * rebound_factor
    print(bounce_number, round(bounced_back_to, 4))

    # now we've printed the new height, set up the variables for the next iteraction
    drop_height = bounced_back_to
    bounce_number = bounce_number + 1
