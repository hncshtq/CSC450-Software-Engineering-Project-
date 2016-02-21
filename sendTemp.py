import time
import sys
from azure.servicebus import ServiceBusService

infile = open("tempOutput.txt", "r")
temp = infile.readline().rstrip()
#print('received temp of: ' + temp)
temp = int(temp)

key_name = "sendRule"
key_value = "9SWS0sNEBQMfTmuBHlxFwUHBFMSBgmJ77/ICSRm9HK4="

sbs = ServiceBusService("pimessage-ns",shared_access_key_name=key_name, shared_access_key_value=key_value)
if temp > 65 or temp < 30:
#    print('sending temp of:' + temp)
    sbs.send_event('pimessage', '{ "DeviceId": "smokerpi", "Temperature": temp }')
    print('sent!')
    print ('got here')
else:
    print('temp was in normal range')
