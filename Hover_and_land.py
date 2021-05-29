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
# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):

  print ("Basic pre-arm checks")
  # Don't let the user try to arm until autopilot is ready
 
        
  print ("Arming motors")
  # Copter should arm in GUIDED mode
   vehicle.mode = VehicleMode("GUIDED")
  vehicle.armed   = True


  time.sleep(10)  

  print ("Taking off!")
  vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

  # Check that vehicle has reached takeoff altitude
  while True:
    print (" Altitude: ", vehicle.location.global_relative_frame.alt) 
    #Break and return from function just below target altitude.        
    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
      print ("Reached target altitude")
      break
    time.sleep(1)

    
def Land():
##This function ensures that the vehicle has landed (before vechile.close is called)

  print("Landing")
  ##thread_distance.join()
  time.sleep(1)
  vehicle.mode = VehicleMode("LAND")
  while vehicle.armed:
    time.sleep(1)
  vehicle.close()


#----begin programming form here


##-------------------------------------------------------------------------------------------------------------------------------

arm_and_takeoff(2) ##------------ arm and reach 20m alt 

time.sleep(10)

Land()
##-------------------------------------------------------------------------------------------------------------------------------

