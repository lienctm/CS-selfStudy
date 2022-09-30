alien = {'x_position' : 0, 'y_postion' : 25, 'speed':'fast'}
print(f"Original postion {alien['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print(f"New position {alien['x_position']}")
