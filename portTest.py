#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import socket
import commonFunctions as cf
from datetime import datetime

# Defining a target
if len(sys.argv) == 2:
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
    exit(1)

# Add Banner
cf.printMegaBanner("PORT SCANNER")
textList = list()
textList.append("Scanning Target: " + target)
textList.append("Scanning started at:" + str(datetime.now()))
cf.printBanner("-", 50, textList)

try:
    # will scan ports between 1 to 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting program !!!!")
    sys.exit(2)
except socket.gaierror:
    print("\n Hostname could not be resolved !!!!")
    sys.exit(3)
except socket.error:
    print("\n Server is not responding !!!!")
    sys.exit(4)
