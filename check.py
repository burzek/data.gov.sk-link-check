#!/usr/bin/env python

# check dataset links at data.gov.sk
import urllib2
import urllib
import json
import os

#some colors
OK = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

#make the HTTP request
response = urllib2.urlopen('http://data.gov.sk/api/1/rest/dataset')
assert response.code == 200
        

#use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
        
#for all datasets get url, load metadata and check with curl
for ds_name in response_dict:
  response = urllib2.urlopen('http://data.gov.sk/api/1/rest/dataset/' + ds_name)
  ds_metadata = json.loads(response.read())
  url =  ds_metadata['resources'][0]['url']
    
  ret = os.system("curl -X GET --output /dev/null --silent --head --fail \"" + url + "\"")
  errorCode = (ret & int('0xff00', 16)) >> 8	#special return code from os.system, see python docs
    
  #print msg
  if (errorCode <>0):
    print (FAIL + "ERR (" + str(errorCode) + ")" + ENDC + " pre dataset:" + ds_name + ", url=" + url)
  else:
    print (OK + "OK" + ENDC + " pre dataset:" + ds_name)
