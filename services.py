import os

def all_envs():

	return os.popen('env').read()

def create_env(name, value):

	os.popen('export '+name+'='+value)
	return name+'='+value

def running_software():

	return os.popen('ps -ef').read()

