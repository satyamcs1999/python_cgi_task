#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/plain")
print()

form = cgi.FieldStorage()

cname = form.getvalue("d1")

cmd = "sudo docker ps -a | grep {} ".format(cname)
output = subprocess.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status == 0:
    print("Container status retrieved successfully")
    print(out)
else:
    print("Error retrieving Container status")

