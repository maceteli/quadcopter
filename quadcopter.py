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
    
def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
       print(" Waiting for vehicle to initialise...")
       time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
        
    time.sleep(1)
    # Confirm vehicle armed before attempting to take off
    if(vehicle.armed == True):
        print("vehicle armed successful")
        print("Taking off!")
        vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude
        # Check that vehicle has reached takeoff altitude
        while True:
            print (" Altitude: ", vehicle.location.global_relative_frame.alt) 
            #Break and return from function just below target altitude.        
            if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
              print ("Reached target altitude")
              break
            time.sleep(1)
        
    else:
        print("vehicle armed unsuccesful")
        vechile.close()
        
def Land():
##This function ensures that the vehicle has landed (before vechile.close is called)

  print("Landing")
  ##thread_distance.join()
  time.sleep(1)
  vehicle.mode = VehicleMode("LAND")
  while vehicle.armed:
    time.sleep(1)
  vehicle.close()   

arm_and_takeoff(3)

vehicle.airspeed = 0.5


print("Travelling to waypoint 1 ...")
point1 = LocationGlobalRelative(7.606651, 5.306836)
vehicle.simple_goto(point1)

# sleep so we can see the change in map
time.sleep(5)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

time.sleep(5)
# Close vehicle object before exiting script
Land()

