from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
    ) -> None:
        mqConsumerInterface.__init__(self,binding_key,exchange_name,queue_name)
    
    def setupRMQConnection(self) -> None:
        return super().setupRMQConnection()
    def on_message_callback(self, channel, method_frame, header_frame, body) -> None:
        return super().on_message_callback(channel, method_frame, header_frame, body)
    def startConsuming(self) -> None:
        return super().startConsuming()
    def __del__(self) -> None:
        return super().__del__()