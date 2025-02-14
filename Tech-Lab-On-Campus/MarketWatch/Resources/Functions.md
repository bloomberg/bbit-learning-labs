# Functions

## Required Libraries
```sh
import pika
import os
```

## Connecting to RabbitMQ service
```sh
con_params = pika.URLParameters(os.environ["AMQP_URL"])
connection = pika.BlockingConnection(parameters=con_params)
```

## Establishing Channel
```sh
channel = connection.channel()
```

## Creating An Exchange
```sh
exchange = channel.exchange_declare(exchange="Exchange Name")
```

## Publishing To An Exchange
```sh
channel.basic_publish(
    exchange="Exchange Name",
    routing_key="Routing Key",
    body="Message",
)
```

## Declaring Queue
```sh
channel.queue_declare(queue="Queue Name")
```

## Binding Queue To Exchange
```sh
channel.queue_bind(
    queue= "Queue Name",
    routing_key= "Routing Key",
    exchange="Exchange Name",
)
```

## Setup Callback Function For Queue
```sh
channel.basic_consume(
    "Queue Name", Function Name, auto_ack=False
)
```

## Acknowledge Message
```sh
channel.basic_ack(method_frame.delivery_tag, False)
```

## Closing Channel and Connection
```sh
channel.close()
connection.close()
```

## Start Consuming Message
```sh
channel.start_consuming()
```

## Creating Topic Exchange
```sh
channel.exchange_declare(
    exchange="Exchange Name", exchange_type="topic"
)
```

## De-Serialize JSON message object
```sh
message = json.loads(JsonMessageObject)
```

