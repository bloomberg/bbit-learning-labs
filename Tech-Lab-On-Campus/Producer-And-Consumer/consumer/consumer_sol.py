#import pika
#import os

from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:
        #inherit from class mqConsumerInterface:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        setRMQ = setupRMQConnection() 

    def setupRMQConnection(self, setRMQ) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)
        
        # Establish Channel
        self.channel = self.connection.channel()
        
        self.channel.queue_declare(queue=self.queue_name, durable=True)


        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(
            queue= self.queue_name,
            routing_key= self.binding_key,
            exchange=self.exchange_name,
        )
        
    # Set-up Callback function for receiving messages
    #def on_message_callback(self, channel, method_frame, header_frame, body):
        #self.channel.basic_ack(method_frame.delivery_tag, False)

    def startConsuming(self):
        self.channel.start_consuming()
        self.channel.exchange_declare(
            exchange=self.exchange_name#, exchange_type="topic"
        )
        #message = json.loads(JsonMessageObject)

    
   # def __del__(self):
        #self.channel.close()
        #self.connection.close()

    
        

#mqConsumer(mqConsumerInterface)


#setRMQ = setupRMQConnection()     

#Channel ch = conn.createChannel();
#ch.exchangeBind("destination", "source", "routingKey");

#x = mqConsumer("Key", "Exchange_Name:", "Queue_Name")
#x.printname()