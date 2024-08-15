import http.client
import json

def send_discord_webhook(webhook_url, message):
    # Parse the webhook URL to extract the host and path
    url = webhook_url.replace("https://", "")
    host, path = url.split("/", 1)
    path = f"/{path}"

    # Prepare the message data
    data = {
        "content": message
    }
    
    # Convert the data to JSON
    json_data = json.dumps(data)

    # Create a connection to the Discord server
    connection = http.client.HTTPSConnection(host)
    
    # Send the POST request
    headers = {'Content-Type': 'application/json'}
    connection.request("POST", path, body=json_data, headers=headers)
    
    # Get the response
    response = connection.getresponse()
    if response.status == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status}, {response.reason}")

# Your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1273704663736258654/tyiMczEmAa1IU0nOBHkrH0ahK0k-XXjR0w1KchlFxj3DAfxRxPsn7u8iOeTCOPk5VXAb"

# The message you want to send
message = "hello world PIZDA BOT RC_E"

# Send the message
send_discord_webhook(webhook_url, message)
