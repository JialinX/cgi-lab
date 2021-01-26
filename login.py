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
cookie_sername = cookie.get('username').value
cookie_password = cookie.get('password').value

if cookie_sername == secret.username and cookie_password == secret.password:
	username = cookie_sername
	password = cookie_password

if username == secret.username and password == secret.password:
	print("Set-Cookie: username=",username)
	print("Set-Cookie: password=",password)

	print(templates.secret_page(username,password))
else:
	print(templates.after_login_incorrect())
