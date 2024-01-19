# Problem Definition: ✨Consumer✨

##  Instructions
Create a .py file that will contain a class that is setup to be a consumer in the RabbitMQ framework. This class will inherit from the mqConsumerInterface and consume and print a simple UTF-8 string message. 

Below are bullet points of the criteria:
- Your class should be named mqConsumer.
- Your class should inherit from our mqConsumerInterface.
- The class name should be `mqConsumer` & the source file should be called `consumer_sol.py`
- Constructor: Save the three variables needed to instantiate the class.
- Constructor: Call the setupRMQConnection function.
- setupRMQConnection Function: Establish connection to the RabbitMQ service, declare a queue and exchange, bind the binding key to the queue on the exchange and finally set up a callback function for receiving messages
- onMessageCallback: Print the UTF-8 string message and then close the connection.
- startConsuming:  Consumer should start listening for messages from the queue.

###### [Note: Utilize the following resource to help instantiate the Producer Class: [RabbitMQ Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)]

## Testing
In order to verify that the consumer class was properly instantiated, we will use the provided  `consume.py`, and `publish.py` file from the previous section on the producer. Follow the below instructions:
1. In the terminal window, run the `publish.py` file from the producer section using the python interpreter. This will publish a message using RabbitMQ. 
2. In another terminal window, run the `consumer.py` file from the consumer section using the python interpreter. This file will import your newly created class `mqConsumer` from `consumer_sol.py`. "Hello World" should now be displayed on your terminal if you instantiated & implemented the consumer class correctly.
* Note that if you are developing from the terminal in your IDE, inside the second terminal window you will need to step into the rmq_lab Docker container in order to access the python enviroment. We do this by first running the `docker exec -it [containterName\containerID] /bin/bash` command. Using the `docker ps -a` command will show all the running docker containers and their associated I.D and names. Your command could be `docker exec -it tech-lab-on-campus-rmq_lab-1 /bin/bash` or `docker exec -it 8a785d10fd7e /bin/bash`



