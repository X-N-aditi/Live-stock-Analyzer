import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class stockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("🔌 WebSocket connected!")
        await self.channel_layer.group_add("stocks", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        logger.info("🔌 WebSocket disconnected!")
        await self.channel_layer.group_discard("stocks", self.channel_name)

    async def send_stock_update(self, event):
        logger.info(f"📦 Sending stock update: {event['data']}")
        await self.send(text_data=json.dumps(event["data"]))



