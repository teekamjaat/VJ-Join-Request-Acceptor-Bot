from os import environ

API_ID = int(environ.get("API_ID", "22349465"))
API_HASH = environ.get("API_HASH", "3732e079c4125690226d8e7b4e028ca4")
BOT_TOKEN = environ.get("BOT_TOKEN", "7497272339:AAEVO9dW3yBlqluX1ecU6GOmXimjVFWoqUk")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001786924542"))
ADMINS = int(environ.get("ADMINS", "5469498838"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "tjbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
