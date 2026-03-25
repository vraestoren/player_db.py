# <img src="https://playerdb.co/assets/images/logo.svg" width="50" style="vertical-align:middle;" /> playerdb.py

> Web-API for [PlayerDB](https://playerdb.co) look up player profiles for Minecraft, Steam, and Xbox accounts.

## Quick Start
```python
from playerdb import PlayerDb

db = PlayerDb()
print(db.minecraft_account_lookup("Notch"))
```

---

## Methods

| Method | Description |
|--------|-------------|
| `minecraft_account_lookup(username)` | Look up a Minecraft account by username |
| `steam_account_lookup(steam_id)` | Look up a Steam account by ID |
| `xbox_account_lookup(username)` | Look up an Xbox account by username |
