from channels.consumer import SyncConsumer, AsyncConsumer
from time import sleep
import asyncio
# Difference Between Sync an Async method

'''
1] SyncConsumer - In Sync method does not handel multiple request at a time 
                - It will run one by one.
2] AsyncConsumer - In Async method can handel multiple request at a time
                 - It will run side by side.
'''

# Syncconsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Webscocket connect',event)
        self.send({
            "type": "websocket.accept",
        })
        # self.accept()
        
    def websocket_receive(self,event):
        print('Webscocket receive',event['text'])
        for i in range(10):
            self.send({
                "type": "websocket.send",
                'text': f'Massage From Server {i}'
            })
            sleep(1)
    def websocket_disconnect(self,event):
        print('Webscocket disconnect',event)


# Syncconsumer
class MyASyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('Webscocket connect')
        await self.send({
            "type": "websocket.accept",
        })
    async def websocket_receive(self,event):
        print('Webscocket receive')
        for i in range(10):
            await self.send({
                "type": "websocket.send",
                'text': f'Massage From Server {i}'
            })
            await asyncio.sleep(1)
    async def websocket_disconnect(self,event):
        print('Webscocket disconnect')