import pika
import os
import sys
from solution import mqConsumerInterface
Class mqConsumer(mqConsumerInterface):
  def __init__(self, binding_key: str, exchange_name: str, queue_name: str):
    self.binding_key = binding_key
    self.exchange_name = exchange_name
    self.queue_name = queue_name
    self.setupRMQConnection()
  
  def setupRMQConnection(self):
    con_params = pika.URLParameters(os.environ["AMQP_URL"])
    self.connection = pika.BlockingConnection(parameters=con_params)
    self.channel = connection.channel()
    self.channel.queue_declare(queue= self.queue_name)
    exchange = channel.exchange_declare(exchange= self.exchange_name)
    self.channel.queue_bind(queue= self.queue_name, routing_key= self.binding_key, exchange= self.exchange_name,)
    self.channel.basic_consume(self.queue_name, on_message_callback, auto_ack=False)

  def on_message_callback(self, channel, method_frame, header_frame, body):
    self.channel = channel
    self.channel.basic_ack(method_frame.delivery_tag, False)
    #Print message (The message is contained in the body parameter variable)
    print(body)

    self.channel.close()
    self.connection.close()

  def startConsuming(self):
    print("[*] Waiting for messages. To exit press CTRL+C")
    self.channel.start_consuming()

  def __del__(self) ->:
    # Print "Closing RMQ connection on destruction"
    print("Closing RMQ connection on destruction")
    # Close Channel
    self.channel.close()
    self.connection.close()
        
        
