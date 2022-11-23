#!/usr/bin/env python3

"""
! This is the solution to the problem.
"""

import rospy
from dynamic_reconfigure.srv import Reconfigure
from dynamic_reconfigure.msg import Config, DoubleParameter

# init note
rospy.init_node('unsafe_traversal', anonymous=True)

# setup service proxy
set_parameters = rospy.ServiceProxy(
    '/move_base/TebLocalPlannerROS/set_parameters', Reconfigure)
set_parameters.wait_for_service()

# get current parameters
parameters = set_parameters()
current_min_obstacle_dist = None
current_inflation_dist = None

for entry in parameters.config.doubles:
    if entry.name == 'min_obstacle_dist':
        current_min_obstacle_dist = entry.value
    elif entry.name == 'inflation_dist':
        current_inflation_dist = entry.value

print(
    f"Current parameters are:\ninflation_dist = {current_inflation_dist}\nmin_obstacle_dist = {current_min_obstacle_dist}\n")

# update the parameters
TARGET_MIN_OBSTACLE_DIST = 0.02
TARGET_INFLATION_DIST = 0.2

new_config = Config()
new_config.doubles.append(DoubleParameter(
    name="min_obstacle_dist",
    value=TARGET_MIN_OBSTACLE_DIST
))
new_config.doubles.append(DoubleParameter(
    name="inflation_dist",
    value=TARGET_INFLATION_DIST
))

set_parameters(new_config)
print(
    f"Updated parameters to:\ninflation_dist = {TARGET_INFLATION_DIST}\nmin_obstacle_dist = {TARGET_MIN_OBSTACLE_DIST}\n")

# wait for user input
input("Press enter to restore previous values.")

# restore values
old_config = Config()
old_config.doubles.append(DoubleParameter(
    name="min_obstacle_dist",
    value=current_min_obstacle_dist
))
old_config.doubles.append(DoubleParameter(
    name="inflation_dist",
    value=current_inflation_dist
))

set_parameters(old_config)
print("Restored original parameters.")
