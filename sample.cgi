#!/usr/bin/python

import cgi,commands

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
f_no=data.getvalue('first_no')
s_no=data.getvalue('sec_no')
cmd=data.getvalue('cmd')
exc=commands.getoutput('sudo '+cmd)

print "first no :",f_no
print "<br>"
print "second no :",s_no
print "<br>"
print "sum :",int(f_no)+int(s_no)
print "<br>"
print "cmd :",cmd
print "<br>"
print "excute :",exc

