#!/usr/bin/python
import os
import services
from flask import Flask
app = Flask(__name__)

@app.route("/")
def iniConnection():

	return "Connected port"
@app.route("/conf/env")
def do_all_envs():
	return services.all_envs()

@app.route("/env/<name>/<value>")
def do_create_env(name, value):
	return services.create_env(name, value)

@app.route("/list/running")
def do_running_software():
	return services.running_software()

if __name__ == '__main__':
	app.run(host='localhost', port=8081)
