import time
import sys
from azure.servicebus import ServiceBusService

from twilio.rest import TwilioRestClient

#key_name = "sendRule"
#key_value = "9SWS0sNEBQMfTmuBHlxFwUHBFMSBgmJ77/ICSRm9HK4="

#sbs = ServiceBusService("pimessage-ns",shared_access_key_name=key_name, shared_access_key_value=key_value)

#while(True):
#	print('sending...')
#	sbs.send_event('pimessage', '{ "DeviceId": "smokerpi", "Temperature": "37.0" }')
#	print('sent!')
#	time.sleep(10)

infile = open("tempOutput.txt", "r")
temp = infile.readline().rstrip()
#print('received temp of: ' + temp)
temp = int(temp)
client = TwilioRestClient(account = 'AC5e63bbdefc2e7374af34ce71e9d252d7', token = '76910c3c9f315d9e39c914581101b969')

client.messages.create(to='+14171234567',from_='19182382589',body = temp )
time.sleep(1)
