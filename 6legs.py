"""6legs controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import math 
# create the Robot instance.


# get the time step of the current world.
timestep = 32
robot = Robot()
motorRPC = robot.getDevice("RPC")
mortorRPF = robot.getDevice("RPF")
motorRMC = robot.getDevice("RMC")
motorRMF = robot.getDevice("RMF")
motorRAC = robot.getDevice("RAC")
motorRAF = robot.getDevice("RAF")

motorLPC = robot.getDevice("LPC")
motorLPF = robot.getDevice("LPF")
motorLMC = robot.getDevice("LMC")
motorLMF = robot.getDevice("LMF")
motorLAC = robot.getDevice("LAC")
motorLAF = robot.getDevice("LAF")
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
