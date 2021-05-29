from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()

# Connect to the Vehicle
print ('Connecting to vehicle: %s' % args.connect)
vehicle = connect('udp:127.0.0.1:14551')
    
def arm_and_takeoff():
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
       print(" Waiting for vehicle to initialise...")
       time.sleep(10)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
        
    time.sleep(10)
    # Confirm vehicle armed before attempting to take off
    if(vehicle.armed == true):
        print("vehicle armed successful")
        print("vehicle disarming")
        vehicle.armed = False
        
    else:
        print("vehicle armed unsuccesful")
    


arm_and_takeoff()

time.sleep(10)
# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

