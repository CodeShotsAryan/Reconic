# Will add configuration later
import os
from dotenv import load_dotenv
load_dotenv()

class settings:
    DATABASE_URL : str = os.getenv("DATABASE_URL")


settings = settings()
