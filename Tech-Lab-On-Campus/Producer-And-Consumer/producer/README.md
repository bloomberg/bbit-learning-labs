# Problem Definition: ✨Producer✨

##  Instructions
Create a ".py" file that will contain a class set up to be a producer in the RabbitMQ framework. This class will inherit from the mqProducerInterface and should publish a simple UTF-8 string message. 

Below are bullet points of the criteria:
- In the `solution` directory, create a file named `producer_sol.py`
- Write your code in the `producer_sol.py` file
- Create a class named `mqProducer`
- Your class should [inherit](../../Resources/Python-Basics.md#creating-an-interface) from our mqProducerInterface.
- Constructor: [Save the two variables](../../Resources/Python-Basics.md#saving-a-instance-variable-and-calling-the-variable) needed to instantiate the class.
- Constructor: Call the setupRMQConnection function.
- setupRMQConnection Function: Establish connection to the RabbitMQ service.
- publishOrder:  Publish a simple UTF-8 string message from the parameter.
- publishOrder:  Close Channel and Connection.  

## Testing
To test your producer class, we'll use Docker to set up a container running RabbitMQ. We'll then create a testing container where you can run the test code provided. To validate the messages are being sent, you'll utilize the RabbitMQ container's management web application.
1. Log Into the RabbitMQ website.
* The login URL for the management web application will be http://localhost:15672/
* Login username and password should be "guest"
3. Send your message
* To test your implementation you can run `publish.py`. It will import your newly created class from the source file `producer_sol.py` in the `solution` directory.
4. Check Message Rates
* Return to the RabbitMQ website.
* Look Under the Overview Tab for message rates to verify that a message was sent. Your message rate should look like the image below.

![alt text](../../../data/Images/message_rate.jpeg)
