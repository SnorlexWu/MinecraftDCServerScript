This is a python script that will run minecraft server.jar and send messages to Discord channel based on:
1) Server start and shutdown
2) player join and left the server

For this script to work, create another py file in the same directory (any name, but need to change the import) u have this script. Write as follow:
```
jar_path = 'C:\\XX\\XX\\XX\\XX\\server.jar' #This is the path to your server.jar
java_path = 'C:\\XX\\Java\\jdk-21\\bin\\java.exe' #This is the path where u install ur java, this is to make sure it runs the selected java version if u have multiple version 
discord_channel = "https://discord.com/api/v9/channels/############/messages" 
discord_account = "YOUR_DISCORD_TOKEN" 
```
For getting Discord channel and account please refer to :

https://www.youtube.com/watch?v=g0jsaTIWz5I&t=218s&ab_channel=CodeBear
