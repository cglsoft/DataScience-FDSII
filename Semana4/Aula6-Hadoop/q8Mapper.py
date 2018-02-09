#!/usr/bin/python
# Lesson 6 : Project - Quiz 8 Most Popular - 

"""
The logfile is in Common Log Format:

10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

%h %l %u %t \"%r\" %>s %b

Where:

    %h is the IP address of the client
    %l is identity of the client, or "-" if it's unavailable
    %u is username of the client, or "-" if it's unavailable
    %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
    %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
    %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
    %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

"""


import sys
import re


parserCLF = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

for line in sys.stdin:
    clfLine = parserCLF.match(line)
    if not clfLine:
        continue

    host, ignore, user, date, request, status, size = clfLine.groups()

    requestSplit = request.split(" ")
    request = requestSplit[1]

    request = request.replace( "http://www.the-associates.co.uk", "" )
    
    print("{0}\t{1}".format(request, 1))
            
    # if (len(data) > 1):
    #    data[1] = data[1].replace( "http://www.the-associates.co.uk", "" )
    #    docname = data[1].split(" ")[0]