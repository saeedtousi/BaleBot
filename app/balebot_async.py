
import aiohttp
import asyncio
import logging
import os

class BaleBot:
    BASE_URL = "https://tapi.bale.ai/bot"

    def __init__(self, token: str):
        self.token = token
        self.session = None
        self.offset = 0
        logging.basicConfig(level=logging.INFO)

    async def init_session(self):
        if not self.session or self.session.closed:
            self.session = aiohttp.ClientSession()

    # ----------------------------- BASE REQUESTS -----------------------------
    async def _get(self, method: str, params=None):
        url = f"{self.BASE_URL}{self.token}/{method}"
        async with self.session.get(url, params=params) as resp:
            return await resp.json()

    async def _post(self, method: str, payload=None):
        url = f"{self.BASE_URL}{self.token}/{method}"
        async with self.session.post(url, json=payload) as resp:
            return await resp.json()

    # ----------------------------- BASIC METHODS -----------------------------
    async def get_updates(self):
        params = {'offset': self.offset, 'timeout': 30}
        data = await self._get("getUpdates", params)
        return data.get("result", [])

    async def send_message(self, chat_id: int, text: str, reply_markup=None):
        payload = {"chat_id": chat_id, "text": text}
        if reply_markup:
            payload["reply_markup"] = reply_markup
        return await self._post("sendMessage", payload)

    async def forward_message(self, chat_id: int, from_chat_id: int, message_id: int):
        payload = {"chat_id": chat_id, "from_chat_id": from_chat_id, "message_id": message_id}
        return await self._post("forwardMessage", payload)

    async def delete_message(self, chat_id: int, message_id: int):
        payload = {"chat_id": chat_id, "message_id": message_id}
        return await self._post("deleteMessage", payload)

    async def get_me(self):
        return await self._get("getMe")

    async def get_chat(self, chat_id: int):
        return await self._get("getChat", {"chat_id": chat_id})

    # ------------------------- MEDIA METHODS --------------------------
    async def send_photo(self, chat_id: int, photo: str, caption: str = None):
        payload = {"chat_id": chat_id, "photo": photo}
        if caption:
            payload["caption"] = caption
        return await self._post("sendPhoto", payload)

    async def send_document(self, chat_id: int, document: str, caption: str = None):
        payload = {"chat_id": chat_id, "document": document}
        if caption:
            payload["caption"] = caption
        return await self._post("sendDocument", payload)

    async def send_audio(self, chat_id: int, audio: str, caption: str = None):
        payload = {"chat_id": chat_id, "audio": audio}
        if caption:
            payload["caption"] = caption
        return await self._post("sendAudio", payload)

    async def send_voice(self, chat_id: int, voice: str, caption: str = None):
        payload = {"chat_id": chat_id, "voice": voice}
        if caption:
            payload["caption"] = caption
        return await self._post("sendVoice", payload)

    async def send_video(self, chat_id: int, video: str, caption: str = None):
        payload = {"chat_id": chat_id, "video": video}
        if caption:
            payload["caption"] = caption
        return await self._post("sendVideo", payload)

    async def send_location(self, chat_id: int, latitude: float, longitude: float):
        payload = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude}
        return await self._post("sendLocation", payload)

    # -------------------------- KEYBOARD & BUTTON --------------------------
    @staticmethod
    def make_inline_keyboard(buttons: list):
        """
        نمونه buttons:
        [
          [{"text": "پگاه وب‌سایت", "url": "https://pegah.ir"}],
          [{"text": "💬 ارتباط با ما", "callback_data": "contact"}]
        ]
        """
        return {"inline_keyboard": buttons}

    @staticmethod
    def make_reply_keyboard(buttons: list, resize=True, one_time=False):
        """
        نمونه:
        [
          ["گزینه ۱", "گزینه ۲"],
          ["لغو"]
        ]
        """
        return {"keyboard": buttons, "resize_keyboard": resize, "one_time_keyboard": one_time}

    # ---------------------------- POLLING LOOP ----------------------------
    async def handle_update(self, update):
        msg = update.get("message")
        if not msg:
            return

        chat_id = msg["chat"]["id"]
        text_in = msg.get("text", "")
        logging.info(f"📩 Received {text_in} from {chat_id}")

        reply = f"پیامت رسید ✅\nمتنت: {text_in}"
        keyboard = self.make_inline_keyboard([[{"text": "پگاه", "url": "https://pegah.ir"}]])
        await self.send_message(chat_id, reply, reply_markup=keyboard)

    async def long_polling(self):
        await self.init_session()
        logging.info("🤖 BaleBot polling started.")
        while True:
            try:
                updates = await self.get_updates()
                for update in updates:
                    self.offset = update["update_id"] + 1
                    await self.handle_update(update)
            except Exception as e:
                logging.error(f"❌ Polling error: {e}")
                await asyncio.sleep(3)

    async def close(self):
        if self.session:
            await self.session.close()


# 🏁 اجرای مستقیم
if __name__ == "__main__":
    TOKEN = "728945469:6xB8TWaE5QTC4iqc3QwN8MjzPhEqQhUxoohJ6"

    async def main():
        bot = BaleBot(TOKEN)
        await bot.long_polling()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("⏹ Bot stopped.")
