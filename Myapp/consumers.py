from channels.consumer import SyncConsumer, AsyncConsumer


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
        self.send({
            "type": event
        })
    def websocket_disconnect(self,event):
        print('Webscocket disconnect',event)


# Syncconsumer
class MyASyncConsumer(AsyncConsumer):
    async def webscocket_connect(self,event):
        print('Webscocket connect')
    async def webscocket_receive(self,event):
        print('Webscocket receive')
    async def webscocket_disconnect(self,event):
        print('Webscocket disconnect')