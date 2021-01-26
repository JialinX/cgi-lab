#!/usr/bin/env python3
import cgi
import cgitb
import secret, templates
import os
from http.cookies import SimpleCookie
cgitb.enable()

storage = cgi.FieldStorage()
username = storage.getfirst("username")
password = storage.getfirst("password")


print("Content-Type: text/html")
cookie = SimpleCookie(os.environ['HTTP_COOKIE'])
if cookie.get('username'):
	cookie_username = cookie.get('username').value
else:
	cookie_username = None
if cookie.get('username'):
	cookie_password = cookie.get('password').value
else:
	cookie_password = None
if cookie_username == secret.username and cookie_password == secret.password:
	username = cookie_username
	password = cookie_password

if username == secret.username and password == secret.password:
	print("Set-Cookie: username=",username)
	print("Set-Cookie: password=",password)

	print(templates.secret_page(username,password))
else:
	print(templates.after_login_incorrect())
