#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Modified example to send PMTK command
#-----------------------------------------------------------------------------

from __future__ import print_function
from time import sleep
import sys
import qwiic_titan_gps

def run_example():
    print("SparkFun GPS Breakout - XA1110!")
    qwiicGPS = qwiic_titan_gps.QwiicTitanGps()

    if qwiicGPS.connected is False:
        print("Could not connect to to the SparkFun GPS Unit. Double check that\
              it's wired correctly.", file=sys.stderr)
        return

    qwiicGPS.begin()

    # Construct the PMTK command
    pmtk_command = "$PMTK353,1,0,0,0,0*2A\r\n"

    # Send the PMTK command
    if qwiicGPS.send_pmtk_packet(pmtk_command):
        print("PMTK command sent successfully!")
    else:
        print("Failed to send PMTK command.")

    while True:
        if qwiicGPS.get_nmea_data() is True:
            for k, v in qwiicGPS.gnss_messages.items():
                print(k, ":", v)

        sleep(1)

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending example.")
        sys.exit(0)
