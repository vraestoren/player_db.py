# player_db.py
Web-API for [playerdb.co](https://playerdb.co/) JSON powered player fetching and caching service

## Example
```python3
from player_db import PlayerDb

player_db = PlayerDb()
steam_account = player_db.steam_account_lookup(steam_id="")
print(steam_account)
```
