import parametres
from umqtt_simple import MQTTClient


def startMQTT(message):
    print("Connexion au broker MQTT...")
    client = MQTTClient(
        parametres.mqtt_client_id,
        parametres.mqtt_server,
        user=parametres.usermqtt,
        password=parametres.usermdp
    )

    # publication sur le topic
    try:
        client.connect()
        print("Connected au broker MQTT avec succes!")
        client.publish(parametres.MQTT_TOPIC, message)
        client.disconnect()
    except Exception as e:
        print("Erreur lors de la connexion au broker MQTT :", e)