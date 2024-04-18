import pika
import os
from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key, exchange_name, queue_name):
        # body of constructor
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name

        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:


        # Set-up Connection to RabbitMQ service
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        self.connection = pika.BlockingConnection(parameters=conParams)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create Queue if not already present
        self.channel.queue_declare(queue=self.queue_name)


        # Create the exchange if not already present
        exchange = self.channel.exchange_declare(exchange=self.exchange_name)


        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(exchange=self.exchange_name,
                   queue=self.queue_name,
                   routing_key=self.binding_key)

        # Set-up Callback function for receiving messages

        self.channel.basic_consume(
        self.queue_name, self.on_message_callback, auto_ack=False
        )
        

        #We can then publish data to that exchange using the basic_publish method
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.binding_key,
            body="bodyyyyyy",
        )

    def on_message_callback(self, channel, method_frame, header_frame, body) -> None:
        print(" [*] Waiting for messages. To exit press CTRL+C")

        self.channel.basic_ack(method_frame.delivery_tag, False)
        print(body)


    def startConsuming(self) -> None:
        self.channel.start_consuming()

    def __del__(self) -> None:
        print("Closing RMQ connection on destruction")
        
        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()

        
        pass