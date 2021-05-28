from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    # Connect to the Vehicle
    print ('Connecting to vehicle: %s' % args.connect)
    vehicle = connect(args.connect, wait_ready=True)
    return vehicle
    
vehicle = connectMyCopter()