from robo_controller import Robot, Keyboard
import math

import random

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice("left wheel motor");
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)

right_motor = robot.getDevice("right wheel motor");
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)

imu= robot.getDevice("inertial unit")
imu.enable(timestep)

ds_front = robot.getDevice("ds_front")
ds_front.enable(timestep)
ds_left = robot.getDevice("ds_left")
ds_left.enable(timestep)
ds_right = robot.getDevice("ds_right")
ds_right.enable(timestep)

movement=0
robo_orientation=180
reached_end=0
random_turn=0

def move(left_speed,right_speed):
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)    
    
def turn_towards_angle(target,movement):
    if(target != yaw_current):
        move(-4,4) 
    else:
        move(0,0)
        movement+=1    
    return movement 

def move_forward_till_wall_detection(movement,random_turn):
    if(ds_front_value>900):
        move(15,15)
    else:
        print(movement)
        # assign 0 to movement and random_turn variable to reset and stop the robot using move() method
        
        
    return movement,random_turn
    
def random_movement(movement,random_turn):  
    if(movement==0):
        movement+=1  
        # write the code assign a random value to random_turn varible
        
        
    if(movement==1):
        movement=turn_towards_angle(random_turn%360, movement) 
    return movement, random_turn
    
while robot.step(timestep) != -1:
       
    ds_front_value= ds_front.getValue()
    ds_left_value= ds_left.getValue()
    ds_right_value= ds_right.getValue()
    
    angle=imu.getRollPitchYaw()

def startMotion(motion):
    motion.play()

key = Keyboard.getKey()
random_turn = random.randint(0, 360)
yaw_current=round(math.degrees(angle[2]))+180
while():
    if(key == Keyboard.SPACE):
        startMotion()
    robot.random_turn()


    
    # the range was -180 to 180 , we change it to 0 to 360
    
    
    # call random_movement method when variable movement holds a value less than or equals 1
    # call move_forward_till_wall_detection method when variable movement holds a value greater than 1


        
        
            