# Rabbit MQ On Campus Lab

## Background

The idea of this lab is to offer exposure to the RabbitMQ messaging framework, providing a basic understanding of the technology and the producer consumer relationship. During the lab you will apply your learning to create small system to setup information update on securities on interest. 

## Key Learning Items

- Python CS Concepts
    - Classes & OOP
    - Importing & Exporting Modules
    - Inheritance 
- Rabbit MQ Concepts
    - Producers
    - Consumers
    - Exchanges
- Financial Concepts
    - Tickers
    - Industry Sectors
- Docker

## Setting Up Our Environment
For this project, we're going to leverage the use of Docker to create a helpful development environment for all of the engineers. [Docker](https://docs.docker.com/desktop/) is a tool used to integrate software dependencies and allow developers to quickly spin up software builds in portable lightweight containers which provide consistent environments, ensuring applications run the same way across various platforms. Here are the steps to check that the environment is running correctly:

1. Clone the repo into your working directory.
```sh
git clone git@github.com:bloomberg/bbit-learning-labs.git
```

2. Navigate to the 'Tech-Lab-On-Campus' folder.
```sh
cd bbit-learning-labs/Tech-Lab-On-Campus
```

3. Confirm that Docker and Docker Compose are working on your system.
```sh
docker -v && docker-compose -v
```
* If this works correctly, you will have the versions of Docker and Docker Compose printed to the terminal.
* Note: If you encounter an error at this step navigate to advanced settings on your  Docker Desktop and ensure that `System (requires password)` is selected. This tab can be found by clicking on the gear icon in the top right corner.

4. Utilize Docker to generate and execute a functional image of the project directly from the terminal within your chosen Integrated Development Environment (IDE). Whether you opt for developing the project in Jupyter Notebook or your preferred IDE, follow the steps outlined below to ensure a smooth setup and execution process:

A) Jupyter Notebook
* In the terminal window of your IDE run:
    ```sh
    docker-compose up
    ```
* In the output lines produced by the command, you will find three links providing access to the server hosting your Jupyter Notebook. Click on any one of these links to open and interact with the notebook. The links should resemble the following:
    ```
    rmq_lab-1   |     To access the server, open this file in a browser:
    rmq_lab-1   |         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-1-open.html
    rmq_lab-1   |     Or copy and paste one of these URLs:
    rmq_lab-1   |         http://d572024fabe2:8888/lab?token=4a07fca9cd4a66eba129533a6272f5f5443fdf3f0b7c0e5e
    rmq_lab-1   |         http://127.0.0.1:8888/lab?token=4a07fca9cd4a66eba129533a6272f5f5443fdf3f0b7c0e5e
    ```
    
B) IDE  
* In the terminal window of your IDE run:
    ```sh
    docker-compose up -d && docker-compose exec rmq_lab /bin/bash
    ```
* `docker-compose up -d` : Starts our rabbitmq and python service in detached mode (-d), running them in the background.
* `docker-compose exec rmq_lab /bin/bash` : This command will open an interactive Bash shell inside the rmq_lab service container. Once you are inside the container you can run Python scripts.

* Note: If you encounter an error such as `unix:///Users/userName/.docker/run/docker.sock. Is the docker daemon running?`, please ensure that your Docker application is running.

5. Log Into the RabbitMQ Website.
* From your desktop, open Docker Desktop Dashboard.
* Find the Rabbitmq container and click on the URL under Port(s) for the U.I. This should open up the RabbitMQ website on your default browser.
* Login username and password should be "guest"
* Alternative:  Click on one of the generated URLs in your terminal, such as "http://localhost:15672/", once your docker container is up and running.

6. You are now ready to start the lab. Begin by navigating to the producer folder and reading the "README.md" file. Each of the three units will contain a readme file which will give you the necessary instructions to complete the lab and test your solution. The order in which the lab should be completed as well as information regarding rabbitmq can be found below.

## Unit Ordering List

1. Producer 
2. Consumer 
3. Market Watch


# Concepts

### What is Rabbit MQ?

RabbitMQ is a lightweight, language agnostic & open source messaging software that implements the [AMQP (Advanced Message Queuing Protocol)](https://www.amqp.org/about/what). It works as a message broker that supports various types of asynchronous messaging features and routing types. Using RabbitMQ you can configure your message to get from a source to destinations in a variety of ways.

Within this lab we'll focus on setting up a basic producer-consumer framework within rabbitMQ. This is just the beginning and there are many more ways rabbitMQ can be used! For more learning opportunities check out the official rabbitMQ [Getting Started](https://www.rabbitmq.com/getstarted.html) page.

### What is a Producer?

A producer is a entity (object, application, etc) that creates & sends information to be distributed. In RabbitMQ producers send these messages to an exchange. You can have multiple producers which depending on the exchange will send data to 0 to N queues. For this lab we'll focus on using a single producer. Producers send messages to exchanges along with the routing key associated with that message. At a high level this routing key tells the rabbitMQ framework that the producer would like to send the associated message to queues that match a given regex string. The replication & matching of the routing key is dependant on the type of exchange (explained below). A more concrete example is, we may have a message intended for a particular set of schools that are all in the US. My routing key in that scenario would be "US" which would signal this particular message should go to queues designated as US.

### What is a Consumer?

A consumer is an entity (object, application, etc.) receiving information from a queue. In RabbitMQ you can have multiple queues, each with the potential for various consumers. In this lab we'll focus on setting up a queue with a single consumer.

### Exchanges

Exchanges are the mechanism that tells RabbitMQ how messages should be directed to a queue. You can think of an exchange like different delivery services. Delivery service **Direct Delivery!** may deliver messages to queues/locations based on particular addresses "123 My Address Road, NY, NY, 10022". This would be an example of a **direct exchange** where messages are sent to queues that have a *binding key* that exactly matches the message's *routing key*. Other exchanges also exist such as the **fanout exchange** which will replicate incoming messages to all queues bound to the exchange. An excellent example of a fanout exchange would be a chat room where an incoming message is sent to all users within the chatroom. Typically, a producer needs to be made aware of the queues or consumers attached to queues. A producer is concerned with what exchange it wants to send its message to, the distribution method of that exchange, and the routing key of the message it wants to send.

Within Python using pika an exchange can be declared similar to the following:

```python
#Build our connection to the RMQ Connection.
#The AMPQ_URL is a string which tells pika the package the URL of our AMPQ service in this scenario RabbitMQ.
conParams = pika.URLParameters(os.environ['AMQP_URL'])
connection = pika.BlockingConnection(parameters=conParams)
channel = connection.channel()
channel.exchange_declare('Test Exchange')

#We can then publish data to that exchange using the basic_publish method
channel.basic_publish('Test Exchange', 'Test_route', 'Hi',...)
```

### Topic Exchange
A **topic exchange** route messages to one or many queues based on matching between a message routing key and the pattern that was used to bind a queue to an exchange.

Messages sent to a topic exchange must use a routing and binding key that are a list of words separated by dots (ex. `some.routing.key`). Topic exchanges are similar to **direct exchanges** in logic; a message sent with a particular routing key will be delivered to all the queues that are bound with a matching binding key.
- Using a `*` symbol in your binding key will substitute it with __exactly 1 word__
- Using a `#` symbol in your binding key will substitute it with __0 or more words__

With Python and pika, an exchange can be declared similar to the following:
```py
# We'll first set up the connection and channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the topic exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# Set the routing key and publish a message with that topic exchange:
routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(f" [x] Sent {routing_key}:{message}")
```

# Basic Financial Concepts

### What is a Stock?

A stock like **APPL**, is a financial instrument representing a **fractional ownership stake in a corporation** such as Google or Costco. **A unit of stock is called a "share."** "Shares"respective values are proportional to the total monetary worth of a company. 

Note that stocks for a given company are identified by a combination of letters and symbols rather than the company name; this is called its **ticker symbol.** For example, the ticker symbol for Apple is **APPL**.

### What is a Position?
A position represents **how much of a particular stock is owned by an individual or financial firm.** Simply put, it lets you know how much of a financial asset you own.

For example, you could have a position like this:

A position of **2,000** shares of **MSFT**!

### What is a Portfolio?

A portfolio represents a **collection of all the investments an individual or entity owns.** These financial investments can be any combination of any financial assets such as  **stocks, bonds,cash**, etc.

For example, I could have a portfolio which contains the positions:

**10** shares of **MSFT USD**  and **10** shares of **AAPL USD**

Hypothetically, if a stock of MSFT is worth $50 each and a stock of AAPL is worth $20 each, then the total value of the portfolio above would be $70.
