import pika
from mqConsumerInterface import mqConsumerInterface


class mqConsumer(mqConsumerInterface):
    def __init__(self, queue_name, exchange_name, binding_key):
        # Save required variables
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.binding_key = binding_key

        self.connection = None
        self.channel = None

        # Setup RabbitMQ connection
        self.setupRMQConnection()

    def setupRMQConnection(self):
        # Establish connection to RabbitMQ
        parameters = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        # Declare exchange
        self.channel.exchange_declare(
            exchange=self.exchange_name,
            exchange_type='direct',
            durable=True
        )

        # Declare queue
        self.channel.queue_declare(
            queue=self.queue_name,
            durable=True
        )

        # Bind queue to exchange with binding key
        self.channel.queue_bind(
            exchange=self.exchange_name,
            queue=self.queue_name,
            routing_key=self.binding_key
        )

        # Setup consumer callback
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.onMessageCallback,
            auto_ack=True
        )

    def onMessageCallback(self, ch, method, properties, body):
        # Print UTF-8 message
        message = body.decode('utf-8')
        print(message)

        # Close connection after receiving message
        if self.connection and not self.connection.is_closed:
            self.connection.close()

    def startConsuming(self):
        # Start listening for messages
        self.channel.start_consuming()

    def __del__(self):
        # Clean up resources
        try:
            if self.channel and self.channel.is_open:
                self.channel.close()
            if self.connection and self.connection.is_open:
                self.connection.close()
        except Exception:
            pass
