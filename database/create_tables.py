import pymysql

from config_for_database import data_dict
from logging_for_database.logging_for_database import logger_info, logger_error


def create_tables():
    try:
        connection = pymysql.connect(host=data_dict["host"],
                                     user=data_dict["user"],
                                     password=data_dict["password"],
                                     db=data_dict["database"],
                                     port=data_dict["port"],
                                     cursorclass=pymysql.cursors.DictCursor)
        logger_info.info("Connection established")
        try:
            with connection.cursor() as cursor:
                query_for_pets = ("CREATE TABLE IF NOT EXISTS Pets ("
                                                    "name varchar(42), "
                                                    "type varchar(10), "
                                                    "date_birth date, "
                                                    "commands varchar(42)"
                                                    ")"
                                  )

                query_for_animal_pack = ("CREATE TABLE IF NOT EXISTS PackAnimals ("
                                                    "name varchar(42), "
                                                    "type varchar(10), "
                                                    "date_birth date, "
                                                    "commands varchar(42)"
                                                    ")"
                                  )


                cursor.execute(query_for_pets)
                cursor.execute(query_for_animal_pack)

                logger_info.info("Table created successfully")
        except pymysql.err.OperationalError:
            logger_error.error("Connection failed")

    except Exception as e:
        logger_error.error("Connection failed", e)
