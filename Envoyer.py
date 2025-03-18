from umqtt_simple import MQTTClient

class MqttConnection:
    def __init__(self, broker, identite, topic, user, password):
        self.broker= broker
        self.identite= identite
        self.topic= topic
        self.user= user
        self.password= password

    def startMQTT(self,temp):
        print("Connexion au broker MQTT...")
        client = MQTTClient(
            self.identite,
            self.broker,
            self.user,
            self.password
        )

        # publication sur le topic
        try:
            client.connect()
            print("Connected au broker MQTT avec succes!")
            client.publish(self.topic, temp)
            client.disconnect()
        except Exception as e:
            print("Erreur lors de la connexion au broker MQTT :", e)