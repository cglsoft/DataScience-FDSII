import sys
import re


# Parser Common Log Format

# http://effbot.org/zone/re-common-log-format.htm


def mapper1():

    p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

    for line in file.readlines():
        m = p.match(line)
        if not m:
            continue
        host, ignore, user, date, request, status, size = m.groups()
        requestSplit = request.split(" ")
        request = requestSplit[1]

file = open('data/access_log_short') 

def main():
	sys.stdin = file
	mapper1()
	sys.stdin = sys.__stdin__

main()