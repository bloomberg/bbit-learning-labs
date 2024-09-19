# Below are bullet points of the criteria:
# - In the `solution` directory, create a file named `producer_sol.py`
# - Write your code in the `producer_sol.py` file
# - Create a class named `mqProducer`
# - Your class should [inherit](../../Resources/Python-Basics.md#creating-an-interface) from our mqProducerInterface.
# - Constructor: [Save the two variables](../../Resources/Python-Basics.md#saving-a-instance-variable-and-calling-the-variable) needed to instantiate the class.
# - Constructor: Call the setupRMQConnection function.
# - setupRMQConnection Function: Establish connection to the RabbitMQ service.
# - publishOrder:  Publish a simple UTF-8 string message from the parameter.
# - publishOrder:  Close Channel and Connection.  

import pika
import os
import producer_interface

class mqProducer(producer_interface):
    
    def __init__(self, routing_key, exchange_name):
        self.rk = routing_key
        self.en = exchange_name

        self.setupRMQConnection()

        pass

    def setupRMQConnection(self):
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)
    
        self.channel = self.connection.channel()

        self.exchange = self.channel.exchange_declare(exchange=self.en)

        pass

    def publishOrder(self, message):
        self.channel.basic_publish(
            exchange=self.en,
            routing_key=self.rk,
            body=message,
        )

        self.channel.close()
    
        self.connection.close()

        pass





    