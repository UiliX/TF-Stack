from os import getenv

from dotenv import load_dotenv

load_dotenv()

FLASK_SECRET_KEY = getenv(
    "FLASK_SECRET_KEY", "02f65a5c46cf19b06833ad85cc7eab5f3d87e5c91164325f"
)
