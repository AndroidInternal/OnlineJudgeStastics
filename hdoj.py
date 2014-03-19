import re
import urllib2
import urllib
import cookielib
import datetime 
import time
import string

def get_num(line):
    num = ""
    for i in line:
        if i >= '0' and i <= '9':
            num += i
    return num
def get_pro(user):
    data = urllib2.urlopen('http://acm.hdu.edu.cn/userstatus.php?user=' + user)
    for line in data:
        if 'Problems Solved' in line:
            return get_num(line)

data = open('user.config', 'r').read().split('\n')
for user in data:
  print user.split('=')[ 2 ] + ' has solved ' + get_pro(user.split('=')[ 1 ]) + ' problems at HDOJ!'

