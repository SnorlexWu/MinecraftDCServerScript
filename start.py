import subprocess
import os
import time
import requests
from credentials import jar_path ,java_path,discord_channel,discord_account


os.chdir(os.path.dirname(jar_path))

# Start the server
process = subprocess.Popen(
    [java_path, '-jar', 'current.jar'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Monitor the output
server_running = False

# Loop to read output lines
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())
        if "[Server thread/INFO]: Done" in output:
            server_running = True
            # Send Discord notification
            url = discord_channel
            payload = {
                "content": "Server Status:      Minecraft server Ngo Lon is running"
            }
            headers = {
                "Authorization": discord_account  # Replace with your token
            }
            res = requests.post(url, json=payload, headers=headers)
            print("Discord notification sent:", res.status_code, res.content)
    
    # Check for player join
    if "joined the game" in output:
        player_name = output.split(" joined the game")[0].split(": ")[-1]  # Extract player name
        join_message = f"Notification:      {player_name} has joined the server."
        res = requests.post(url, json={"content": join_message}, headers=headers)
        print("Join notification sent:", res.status_code, res.content)

    # Check for player leave
    if "left the game" in output:
        player_name = output.split(" left the game")[0].split(": ")[-1]  # Extract player name
        leave_message = f"Notification:     {player_name} has left the server."
        res = requests.post(url, json={"content": leave_message}, headers=headers)
        print("Leave notification sent:", res.status_code, res.content)

# Wait for the Java process to exit
process.wait()  # This will block until the process is terminated

# Once the process is done, send a shutdown notification
if not server_running:
    shutdown_message = "Server Status :     Server Ngo Lon Failed to start"
else:
    shutdown_message = "Server Status:      Server Ngo Lon has stopped"

# Send shutdown notification
url = discord_channel
payload = {
    "content": shutdown_message
}
headers = {
    "Authorization": discord_account  
}
res = requests.post(url, json=payload, headers=headers)
print("Shutdown notification sent:", res.status_code, res.content)

