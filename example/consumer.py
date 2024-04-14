from channels.generic.websocket import WebsocketConsumer
import json

class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']

        # Process the received data and update the page
        self.update_page(data)

    def update_page(self, data):
        self.send(text_data=json.dumps({
            'data': data
        }))