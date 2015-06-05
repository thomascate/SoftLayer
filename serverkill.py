#!/usr/bin/python

import SoftLayer
import yaml

credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)



client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

f = open('kill-file',' r')
	
	 
	client['Virtual_Guest'].deleteObject(i)

close('kill-file')

