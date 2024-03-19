import pika
import os

class myProducer(myProducerInterface):
        rk = ""
        en = ""
        def __init__(self, routing_key: str, exchange_name: str) -> None:
            rk = routing_key
            en = exchange_name
            setupRMQConnection(self)

        def setupRMQConnection(self) -> None:
            con_params = pika.URLParameters(os.environ["AMQP_URL"])
            connection = pika.BlockingConnection(parameters=con_params)
            channel = connection.channel()
            exchange = channel.exchange_declare(exchange="Exchange Name")

        def publicOrder(self, message: str) -> None:
            channel.basic_publish(
                exchange=rn,
                routing_key=rk,
                body=message,
            )
            channel.close()
            connection.close()
