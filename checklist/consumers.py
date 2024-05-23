import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import WebsocketConsumer


from helpers import done_worker, cook_info_bulk_worker

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


users = []


class Consumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'chat_group'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data):

        sync_to_async(print(text_data))
        data = json.loads(text_data)
        print(data)
        if data['type'] == 'done' or data['type'] == 'waiter_task_error':
            result = ''
            if data['role'] != 'hot_streak' or data['role'] != 'cold_streak':
                result = done_worker(data['status'], data['role'], data['task_id'], data['shift'], data.get('comment', ''))
            # self.send(text_data=result)
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'chat.message',
                    "message": result
                }
            )
        if data['type'] == 'cook_info_bulk':
            result = cook_info_bulk_worker(data)

            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'chat.message',
                    "message": result
                }
            )
        if data['type'] == 'create_dynamic_task':
            pass

    def chat_message(self, event):
        message_type = event.get('type')

        if message_type == 'chat.message':
            message = event.get('message')
            self.send(text_data=message)
        else:
            raise ValueError("No handler for message type %s" % message_type)
        