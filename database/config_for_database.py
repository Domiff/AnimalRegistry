import os

from dotenv import load_dotenv


load_dotenv()


data_dict = {
    "host": os.getenv("HOST"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("DATABASE"),
    "port": int(os.getenv("PORT")),
}
