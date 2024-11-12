import os
from dotenv import load_dotenv


class Const:
    """
    상수 관리
    """

    load_dotenv()

    DB_URL = f"postgresql+psycopg2://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"


const = Const()
