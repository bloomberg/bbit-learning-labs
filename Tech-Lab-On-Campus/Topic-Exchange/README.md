# Problem Definition: ✨Topic Exchange✨

##  Instructions
In this section, we will create a [Topic Exchange](../Resources/RabbitMQ.md#topic-exchange). For this lab, the Producer will send messages regarding the current price of a particular stock to the exchange. The Topic Exchange will then route the messages to the appropriate Queues. For instance, a specific Queue may only subscribe to messages regarding stocks from the tech sector, while another may only receive messages regarding stock in the healthcare sector. Lastly, the Consumers will read the messages from the subscribed Queue and then acknowledge and print the information.
One person will focus on the producer section while the other works on the consumer section. Afterwards, you'll exchange solutions verbally or via GitHub. We highly recommend using GitHub for this purpose, working on the same fork, and pushing your solutions. GitHub is widely used across the tech industry. You can find a GitHub file in the resource folder to assist you with this.
> Note: If you are unfamiliar with the concept of a stock please use this resource: [Basic Financial Concepts.](../Resources/Finance.md)

Below are bullet points of the criteria:
1. Producer [Person A]
* Producer Class File
    - Copy your producer solution file into the solution directory.
    - Change the Exchange in your existing producer class from direct to a [Topic Exchange](../Resources/Functions.md#creating-topic-exchange).
* Producer Service File
    - Implement Logic to [read from the command line](../Resources/Python-Basics.md#reading-from-command-line-using-sys) the ticker, price and sector string and save them as variables: ticker, price, sector.
    - Implement Logic to [Create Routing Key](../Resources/RabbitMQ.md#topic-exchange) from the variables. Please consult with your partner and agree on what the binding and routing key should look like first!
    - Implement Logic to Create a message variable from the varaibles. The published message may be a UTF-8 string such as "TSLA is $182.34"

2. Consumer [Person B]
* Consumer Class File
    - Copy your consumer solution file into the solution directory.
    - Change the Exchange in your existing consumer class from direct to a [Topic Exchange](../Resources/Functions.md#creating-topic-exchange).
* Consumer Service File
    - Implement Logic to [read from the command line](../Resources/Python-Basics.md#reading-from-command-line-using-sys) the sector and queue name string and save them as variables: sector, queueName.
    - Implement Logic to [Create Binding Key](../Resources/RabbitMQ.md#topic-exchange) from the variables. When binding the Queue to the exchange ensure that routing key utilizies one of the special cases for binding keys such as \* (star) or # (hash). For instance. "#.Google.#" as a binding key for a Queue will ensure that all messages with a key containing the word Google such as Stock.Google.tech will have their messages routed to that Queue. Please consult with your partner and agree on what the binding and routing key should look like first!
3. Each contributor should then [git push](../Resources/Git-Commands.md#commands-youll-need-for-today) their solutions to the fork.
4. Lastly, follow the `testing instructions below` to send and recieve a message to complete this section.

 > Note: [argparse](https://docs.python.org/3/library/argparse.html) and [sys](https://docs.python.org/3/library/sys.html) are two popular libraries used to read from the command line in python.

## Testing
In order to verify that this excercise was done correctly we will need to test our service.
1. Open up three terminals.
2. In two of the terminals start a consumer service with the consume.py file, one should subscribe to tech stocks and the other to health care stocks.
3. In the third terminal, utilize your publish.py to send three messages: first, a tech stock; second, health; and third, a different sector.
4. Verify that the first and second message went to the appropriate queues only and that the third message did not go to any queue.

Common Issues:
* Ensure that all the Queues have different names so that you are not binding all the keys to one Queue accidentally. One way to do this is by passing in an extra argument which will serve as the name of the Queue.


## Stretch Goal
Allow your consumer to subscribe to specific stock updates and multiple sectors. You can achieve this by creating multiple bindings for the same Queue. Utilize the interface files found in this section to help you.
        
   