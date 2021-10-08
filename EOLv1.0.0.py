import os
import subprocess



#Delete Override.xml
override = raw_input("Delete Override.xml? y/n : ")
if override == "y":
	os.remove('/home/seegrid/Paths/Override.xml')
	print "deleted"

#Delete routes
routes = raw_input("Delete all route data? y/n : ")
if routes == "y":
	subprocess.call(["/home/seegrid/trunk/util/vsm/vsm-remote.sh","system.clear"])
	print "deleted"

#Delete WPA Supplicant
WPA = raw_input("Delete WPA Supplicant.conf? y/n : ")
if WPA == "y":
        os.remove ('/etc/wpa_supplicant/wpa_supplicant.conf')
        print "deleted"

#pull HASP
HASP = raw_input("Pull HASP? y/n : ")
if HASP == "y":
        subprocess.call("/home/seegrid/trunk/bin/pull-machine-id")
        print "deleted"
        