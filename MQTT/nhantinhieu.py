import paho.mqtt.client as mqtt
import pygame
MQTT_BROKER_HOSTNAME = '10.100.10.200'
MQTT_TOPIC = 'topic_unique_name'


def on_message(client, userdata, message):
    #print("%s %s" % (message.topic, str(message.payload)))
    #print(str(message.payload.decode("utf-8")))
    trigger = str(message.payload.decode("utf-8"))
    #print(trigger)
    if trigger == "1":
        print("CO NGUOI DOT NHAP!")
        #playsound("alert.wav")
        pygame.mixer.init()
        pygame.mixer.music.load("alert.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    else:
        print("OK")


if __name__ == "__main__":
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_BROKER_HOSTNAME, 1883, 60)
    mqtt_client.subscribe(MQTT_TOPIC, 0)

    mqtt_client.loop_forever()
