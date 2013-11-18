#!/usr/bin/env python
import urllib2
import urllib
import json
import os

# Make the HTTP request.
response = urllib2.urlopen('http://data.gov.sk/api/1/rest/dataset')
assert response.code == 200
        
# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
        

for ds_name in response_dict:
  response = urllib2.urlopen('http://data.gov.sk/api/1/rest/dataset/' + ds_name)
  ds_metadata = json.loads(response.read())
  url =  ds_metadata['resources'][0]['url']
    
  ret = os.system("curl -X GET --output /dev/null --silent --head --fail \"" + url + "\"")
  errorCode = (ret & int('0xff00', 16)) >> 8
    
  if (errorCode <>0):
    print ("Chyba pre dataset:" + ds_name + ", url=" + url + ", kod chyby:" + str(errorCode))
  else:
    print ("OK pre dataset:" + ds_name)
