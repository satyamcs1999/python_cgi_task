#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/plain")
print()

form = cgi.FieldStorage()

iname = form.getvalue("d1")

cmd = "sudo docker rmi -f {} ".format(iname)
output = subprocess.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status == 0:
    print("Docker Image {0} removed successfully".format(iname))
else:
    print("Error removing Docker Image: {0}".format(iname))

