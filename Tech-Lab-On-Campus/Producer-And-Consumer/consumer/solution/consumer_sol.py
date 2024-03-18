import pika 
import os 

class mqConsumer:
    def __init__(self, binding_key: str, exchange_name: str, 
    queue_name: str) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.setupRMQConnection()
    def setupRMQConnection(self) -> None:
        con_params=pika.URLparameters(os.environ ["AMQP_URL"])
        self.connection=pika.BlockingConnection
        parameters=con_params
        
        self.channel = self.connection.channel()
    
        self.channel.queue_declare(queue=self.queue_name)
        
        self.channel.exchange_declare(exchange=self.exchange_name)
        
        self.channel.queue_bind(queue=self.queue_name, routing_key=self.binding_key, exchange=self.exchange_name)
        
        self.channel.basic_consume(self.queue_name, self.on_message_callback, auto_ack=False)

    def on_message_callback(self, channel, method_frame, body) -> None:
        self.channel.basic_ack(method_frame.delivery_tag, False)
        print(body)
    def startConsuming(self) -> None:
        print("[*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

    def __del__(self) -> None:
        print("Closing RMQ connection on destruction")
        self.channel.close()
        self.connection.close()

        
