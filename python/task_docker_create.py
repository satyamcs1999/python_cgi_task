#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/plain")
print()

form = cgi.FieldStorage()

cname = form.getvalue("d1")
cimage = form.getvalue("d2")

cmd = "sudo docker run -dit --name {0} {1}".format(cname,cimage)
output = subprocess.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status == 0:
    print("Container {0} launched successfully".format(cname))
else:
    print("Error launching Container: {0}".format(cname))

