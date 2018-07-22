# PYTHON-CGI
basic code of html and cgi, how it work and how html connect with python..
# yum install httpd    (apache)
# systemctl restart httpd
# systemctl status httpd   (to conform apache is running or not)
 
NOTE 1:

1.ALLOW  permission for file excute
2.cd /var/www/html/sample.html
# chmod +x sample.html

3.cd /var/www/cgi-bin/sample.cgi       (extension may be .cgi or .py )
# chmod +x sample.cgi

NOTE 2:

when you want to run a command then it need to ROOT power so 
 1. use always sudo with command 
# permission for apache like root 
# vim /etc/suoers
      IN SUDORES FILE LINE NO 93,1
     
      ## Allow root to run any commands anywhere 
root    ALL=(ALL)       ALL

apache  ALL=(ALL)       NOPASSWD: ALL

NOTE 3:
make sure that these are stop`
# iptable -F
   and
# setenforce 0


                                                                                      THANKS YOU:
                                                                                      PANKAJ PATHAK
                                                                                     # pankajkumarpathak25@gmail.com
