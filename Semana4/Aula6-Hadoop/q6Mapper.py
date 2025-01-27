#!/usr/bin/python -O
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

for line in sys.stdin:
    data = line.strip().split("GET ")
    
    if (len(data) > 1):
        docname = data[1].split(" ")[0]
        # Only process /assets/js/the-associates.js
        if (docname != '/assets/js/the-associates.js'):
            continue

        print("{0}\t{1}".format(docname, 1))


"""
# Local Test
file = open('data/access_log_short')   

# This function allows you to test the mapper with the provided test string
def main():
	sys.stdin = file
	mapper1()
	sys.stdin = sys.__stdin__


main()

"""
