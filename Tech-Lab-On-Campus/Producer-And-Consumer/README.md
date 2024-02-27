# Problem Definition: ✨Producer And Consumer✨

##  Instructions

In this section, you will collaborate with a partner to instantiate the producer and consumer classes. One person will focus on the producer section while the other works on the consumer section. Afterwards, you'll exchange solutions verbally or via GitHub. We highly recommend using GitHub for this purpose, working on the same fork, and pushing your solutions. GitHub is widely used across the tech industry. You can find a GitHub file in the resource folder to assist you with this.

Below are bullet points of the criteria:
- First ensure that each contributor is working from and has `cloned the same fork` of the BBIT-LEARNING-LABS repository.
- Second ensure that each contributor has been `added as a collaborator to the fork.`
- One person completes the `producer section.`
- One person completes the `consumer section.`
- Each contributor should then [git push](../Resources/Git-Commands.md#commands-youll-need-for-today) their solutions to the fork.
- Lastly, follow the `testing instructions below` to send and recieve a message to complete this section.

   
`IMPORTANT!!!` Please utlize the [Functions.md](../Resources/Functions.md) file as it contains almost all the functions you will need for this lab. Also, other helpful information can be found under the Resources folder for Python, Git, and RabbitMQ details.

## Testing
In order to verify that the consumer and producer class was properly instantiated, we will use the provided  `consume.py`, and `publish.py` file from producer and consumer folder. Follow the below instructions:
1. In the terminal window, run the `consume.py` file from the consumer sectio using the python interpreter.
2. In another terminal window, run the `publish.py` file from the producer section using the python interpreter. This will publish a message using RabbitMQ. 
3. Return to the first terminal window with the consumer running. "Success! Producer And Consumer Section Complete." should now be displayed on your terminal if you instantiated & implemented the consumer class correctly.
* Note that if you are developing from the terminal in your IDE, inside the second terminal window you will need to step into the rmq_lab Docker container in order to access the python enviroment. We do this by first running the `docker exec -it [containterName\containerID] /bin/bash` command. Using the `docker ps -a` command will show all the running docker containers and their associated I.D and names. Your command could be `docker exec -it tech-lab-on-campus-rmq_lab-1 /bin/bash` or `docker exec -it 8a785d10fd7e /bin/bash`

