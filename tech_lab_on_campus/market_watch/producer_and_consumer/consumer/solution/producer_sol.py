import pika
from mqProducerInterface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, host, queue_name):
        """
        Constructor: Save the two variables needed to instantiate the class
        and initialize the RMQ connection.
        """
        self.host = host
        self.queue_name = queue_name
        
        # Initialize connection and channel placeholders
        self.connection = None
        self.channel = None
        
        # Call the setup function immediately
        self.setupRMQConnection()

    def setupRMQConnection(self):
        """
        Establish connection to the RabbitMQ service.
        """
        # Create a connection to the broker
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

        # Ensure the queue exists
        self.channel.queue_declare(queue=self.queue_name)

    def publishOrder(self, message):
        """
        Publish a simple UTF-8 string message from the parameter.
        Close Channel and Connection afterwards.
        """
        # Ensure the message is sent as a UTF-8 string
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message.encode('utf-8')
        )
        
        print(f" [x] Sent: {message}")

        # Close Channel and Connection
        self.channel.close()
        self.connection.close()