##########################################################
# Code Academy Reggie's Linear Regression Coding Challenge
##########################################################

# Defining get_y. Slope-intercept form. We use this in the next function in order to
# calculate the differences between points.
def get_y(m, b, x):
    y = m * x + b
    return y


# This function is a representation of error between a line and a given point.
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    get_y(m, b, x_point)
    return abs(get_y(m, b, x_point) - y_point)


# Print statements for debug - working correctly.
print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))

# Data to be used for the next function.
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]


# Calculating error, incrementing it, then returning the error to be used later.
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error


# Possible m's and b's, used for the nested loops below in order to find the best m and b for
# Reggie's use case, which is finding sizes of rubber balls and their bounce heights for a ball pit.
possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]

# Setting the values for the smallest_error, best_m, and best_b. Initial values are 0 for use in the nested loop below.
# We set smallest_error to a float with "inf" in order to preemptively combat any errors that might arise in the event
# of bad code.
smallest_error = float("inf")
best_m = 0
best_b = 0

# Reassigning datapoints as a requirement for the project. Datapoints can be set to mostly anything. This nested loop
# is actually designed to run on multiple different datasets, but for this particular project, we are working with
# the assumption that Reggie is actually manually entering these points with each use of his program, which is
# inelegant, but setting up an efficient randomizer for datapoints would be counterintuitive because proper "bounciness"
# is subjective. Computers are awful when it comes to nuance and subjectivity.
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m, b, datapoints) < smallest_error:
            best_m = m
            best_b = b
            smallest_error = calculate_all_error(m, b, datapoints)

# Print the result of the above nested loops
print(best_m, best_b, smallest_error)

# Print the result of get_y with the values that we discovered in the last print statement. This is how high the ball
# bounces depending on its x value, in this case it's 6.
print(get_y(0.3, 1.7, 6))

#######################################################################################################################
# After completeing this project, it actually surprises me how much I retained throughout the program so far.
# I've used Codeacademy in the past, around 2016, and I remember having a particularly hard time even understanding
# the concepts of loops and functions, almost pulling my hair out over it, and I really didn't retain anything except
# for the basics. This course so far has been from a near-fresh set of eyes, and it surprises me that I actually have
# at least an idea as to what I'm doing. After seeing the initial directions for the project, I thought I was going to
# have to look at the hints and solutions far more than I actually did. The first was for properly setting up
# lines 30 - 35. I did get a little bit lost in the directions, and after trying several times to get something working
# it turned out I was doing everything right, but forgot to set a variable to actually count the errors and increment
# them. The second time was for having to remind myself on how to do a list comprehension, and I needed the hint on how
# to properly increment the intervals, since we weren't using a traditional function. The last time was to proofread
# my nested loops. I'm proud to say I got them right on the first time, I just forgot to update the datapoints list.
# Just goes to show how a lot of the time you can do a lot of things right, but one small detail causes some hell
# later on.
#######################################################################################################################
