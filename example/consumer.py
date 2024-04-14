# consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Handle incoming message from Raspberry Pi
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Process message (you can add your custom logic here)
        response_message = f"Received message from Raspberry Pi: {message}"

        # Send response back to Raspberry Pi
        await self.send(text_data=json.dumps({
            'message': response_message
        }))
