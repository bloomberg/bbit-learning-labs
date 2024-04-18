from consumer_interface import mqConsumerInterface
import pika
import os

class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key, exchange_name, queue_name):
        # body of constructor
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name

    def setupRMQConnection(self):


        # Set-up Connection to RabbitMQ service
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        connection = pika.BlockingConnection(parameters=conParams)

        # Establish Channel
        channel = connection.channel()

        # Create Queue if not already present
        channel.queue_declare(queue='Test Queue')


        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange="Test Exchange")


        # Bind Binding Key to Queue on the exchange
        channel.queue_bind(exchange='Test Exchange',
                   queue='Test Queue',
                   routing_key='Routing Key')

        # Set-up Callback function for receiving messages

        channel.basic_consume(
        "Test Queue", Function Name, auto_ack=False
        )
        

        #We can then publish data to that exchange using the basic_publish method
        channel.basic_publish(
            exchange="Test Exchange",
            routing_key="Routing Key",
            body="Message",
        )

    def on_message_callback(self, channel, method_frame, header_frame, body):
        channel.basic_ack(method_frame.delivery_tag, False)
        print(body)


    def startConsuming(self) -> None:
        connections.close()

