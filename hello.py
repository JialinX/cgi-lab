#!/usr/bin/env python3
import os
import json
import sys
import templates

# http://localhost:8080/hello.py?sponsor=raycon&canadians=none

'''
# Make your CGI script serve the environment back as JSON.

print('Content-Type: application/json')

print()
#environment variables
print(json.dumps(dict(os.environ), indent = 2))
#print(list(os.environ.keys()))


# print('Content-Type: text/plain')
# print()
# print('Hello!')
'''
print('Content-Type: text/html')
print()
print(
"""
<!doctype html>
<html>
<body>
<h1> Hello, I am HTML
</h1>
<body>
</html>
"""
)
# Modify your CGI script to report the values of the query parameters in the HTML.

print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

for parameter in os.environ['QUERY_STRING'].split('&'):
	(name, value) = parameter.split('=')
	print(f"<li><em>{name}</em>={value}</li>")

# Modify your CGI script to report the user’s browser in the HTML.

print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")


# Modify your CGI script to contain a login form that POSTs to itself. 
print(templates.login_page())


# Modify your CGI script to report the values of the POSTed data in the HTML.

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")


# Modify your CGI script to set a cookie if the login is correct.
# Modify your CGI script so it displays a secret message if the cookie says the user is logged in. 
# Those above two work will be done in login.py
