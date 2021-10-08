# EOL
End of line script for VGUs
This is a python script that should be ran before programming a VGU for a customer.

This script does:

    Deletes the override.xml
    Deletes wpa_supplicant.conf
    Erases path data
    Pulls HASP

How to run:

    Apply power to the VGU, connect over Putty.
    Once the VGU has been initialized, plug a flash drive with the EOL.py script into the VGU.
    Next, run the script as root.
        su
        root password
        mkdir usb - Ensure you are in the /home/seegrid directory first.
        mount /dev/sdc1 usb for non refresh VGUs
        mount /dev/sda1 usb for refresh VGUs
        python usb/EOL.py 
        Press y when prompted.
