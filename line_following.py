from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_sensor = ColorSensor(Port.C)
right_sensor = ColorSensor(Port.D)

def two_sensor_bangbang(threshold=50, speed=300, turn=40):
    if left_sensor.reflection() < threshold and right_sensor.reflection() > threshold:
        robot.drive(speed, -turn)
    elif left_sensor.reflection() > threshold and right_sensor.reflection() < threshold:
        robot.drive(speed, turn)
    elif left_sensor.reflection() > threshold and right_sensor.reflection() > threshold:
        robot.drive(speed, 0)
    else:
        robot.stop()

def one_sensor_bangbang(threshold=50, speed=300, turn=40):
    if sensor.reflection() < threshold:
        robot.drive(speed, turn)
    else:
        robot.drive(speed, -turn)

def one_sensor_proportional(target=50, base_speed=100, kp=1):
    error = sensor.reflection() - target
    correction = error * kp
    robot.drive(base_speed, correction)

def two_sensor_proportional(base_speed=100, kp=1):
    error = left_sensor.reflection() - right_sensor.reflection()
    correction = error * kp
    robot.drive(base_speed, correction)

while True:
    one_sensor_proportional()
    wait(10)