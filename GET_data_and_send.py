import os
import simplejson as json
import datetime
import urllib2
from datetime import timedelta

temperature = []
humidity = []

X_addresses = ['first webpage of equipment',
               'second webpage of equipment']

X_URL = 'URL to send data to'

tenantid = '***********************************'

deviceid = ['**********************************',
            '**********************************']

Time = datetime.datetime.utcnow()
Time = Time.isoformat()
print Time

for x in range( 0, len( X_addresses ) ):
    firstCmd = os.popen(
        ('wget --user ***** --password ***** {0} --no-check-certificate').format(X_addresses[x])).read()

    f = open( "appAll.json", "r" )
    json_request = f.read()

    data = json.loads( json_request )
    temperature.append( str( data['data']['all'][2]['isens'][0]['val'] ) )
    temperature[x] = temperature[x][:-2:]
    humidity.append( str( data['data']['all'][2]['isens'][1]['val'] ) )
    humidity[x] = humidity[x][:-2:]

    BaseMsg = "text in xml or json with temperature and humidity data"

    BaseMsg = BaseMsg.replace('(','')
    print BaseMsg

    req = urllib2.Request( url=NTI_URL,
                           data=BaseMsg,
                           headers={'Content-Type': 'text/xml'} )
    urllib2.urlopen(req)

    lastCmd = os.popen("rm appAll.json*")
