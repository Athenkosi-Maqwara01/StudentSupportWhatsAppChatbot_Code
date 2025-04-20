import time

class WhatsAppIntegration:
    def __init__(self, api_key: str, phone_number_id: str, webhook_url: str):
        self._api_key = api_key
        self._phone_number_id = phone_number_id
        self._webhook_url = webhook_url
        self._log = []

    def send_message(self, to: str, message: str) -> bool:
        attempt = 0
        while attempt < 3:
            try:
                self._log_api("Sending message", to, message)
                time.sleep(1)  # Simulate network
                return True
            except Exception:
                attempt += 1
                time.sleep(2)
        return False

    def receive_message(self, data: dict) -> dict:
        self._log_api("Message received", data.get("from"), data.get("message"))
        return data

    def send_media(self, to: str, media_url: str, media_type: str):
        self._log_api("Sending media", to, f"{media_type}: {media_url}")

    def verify_webhook(self, token: str) -> bool:
        return token == "expected_token"

    def _log_api(self, action: str, target: str, payload: str):
        log_entry = f"{action} -> {target}: {payload}"
        print(f"[LOG] {log_entry}")
        self._log.append(log_entry)
