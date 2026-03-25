from requests import Session

class PlayerDb:
    def __init__(self) -> None:
        self.api = "https://playerdb.co/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }

    def _get(self, endpoint: str) -> dict:
        return self.session.get(f"{self.api}{endpoint}").json()

    def minecraft_account_lookup(self, username: str) -> dict:
        return self._get(f"/player/minecraft/{username}")

    def steam_account_lookup(self, steam_id: str) -> dict:
        return self._get(f"/player/steam/{steam_id}")

    def xbox_account_lookup(self, username: str) -> dict:
        return self._get(f"/player/xbox/{username}")
