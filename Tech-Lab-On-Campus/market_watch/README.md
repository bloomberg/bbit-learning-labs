# Problem Definition: ✨Topic Exchange✨

##  Instructions
In this section, we will create a [Topic Exchange](../README.md#topic-exchange). For this lab, the Producer will send messages regarding the current price of a particular stock to the exchange. The Topic Exchange will then route the messages to the appropriate Queues. For instance, a specific Queue may only subscribe to messages regarding tech stocks, while another may only receive messages regarding stock in the healthcare sector. Lastly, the Consumers will read the messages from the subscribed Queue and then acknowledge and print the information.

Below are bullet points of the criteria:

1. Create a Producer class
    - You can reuse your existing producer class from module one with a few modifications
    - When instantiating the exchange, ensure it is a topic exchange `exchange_type='topic'`.
    - The routing key used for publishing a message may look like this: `Stock.[Ticker].[Sector]` Eg. Stock.TSLA.tech
- The published message may be a UTF-8 string such as "TSLA $182.34", or one may send a Stock Object containing the stock price and ticker. If the provided Stock object is utilized, call the serialize() method to serialize the object before transmission. EG. body=stock.serialize().

2. Create a Consumer class
    - You can reuse your existing consumer class from module two with a few modifications.
    - When binding the Queue to the exchange ensure that routing key utilizies one of the special cases for binding keys such as \* (star) or # (hash). For instance. "#.Google.#" as a binding key for a Queue will ensure that all messages with a key containing the word Google such as Stock.Google.tech will have their messages routed to that Queue. 
    - If the received message is the serialized stock object, then you must deserialize [message=json.loads(body)]
    the object which will return a dict object which you must then use to extract the ticker and price before printing the message.
    - **Stretch Goal:** Allow your consumer to subscribe to specific stock updates and multiple sectors. You can achieve this by creating multiple bindings for the same Queue.

3. Create a producer python application.
    * This service should read arguments from the command line, instantiate your producer class, and send the appropriate messages to the exchange.
    * Example: The following command should send a Stock object or string, such as "MRNA price is $1334.40" to the exchange with this routing key: Stock.MRNA.health
        
        `python3 producer.py -t  MRNA -p 1334 -s health`
        
    * The example above uses [argparse](https://docs.python.org/3/library/argparse.html) to read the arguments from the command line, but you could use any library such as the [sys](https://docs.python.org/3/library/sys.html)
    
4. Create a consumer python application.
    *   This service should read arguments from the command line, instantiate the consumer class, create a queue with the appropriate binding key. The consumer will acknowledge and print messages from the queue.
    * Example: The following command should create a consumer who prints messages from a Queue that receives only tech stocks-related messages such as  "NVDA price is $208.34"  
        
        `$ python3 consumer.py -s tech`
        
###### [Note: Utilize the following resource to help instantiate the [Topic Exchange](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)]

## Testing
In order to verify that this excercise was done correctly we will need to test our service.
1. Open up three terminals.
2. In two of the terminals start a consumer service, one should subscribe to tech stocks and the other to health care stocks.
3. In the third terminal, utilize your producer service to send three messages: first, a tech stock; second, health; and third, a different sector.
4. Verify that the first and second message went to the appropriate queues only and that the third message did not go to any queue.

Common Issues:
* Ensure that all the producers and consumers are bound to the same exchange. Check this by verifying that they all use the same exact exchange name [exchange="Exchange Name"].
* Ensure that all the Queues have different names so that you are not binding all the keys to one Queue accidentally. One way to do this is by passing in an extra argument which will serve as the name of the Queue.