import paho.mqtt.client as mqtt #import the client1
broker_address="10.100.10.200"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
#client.subscribe("test")
client.publish("topic_unique_name","1")#publish
client.disconnect()