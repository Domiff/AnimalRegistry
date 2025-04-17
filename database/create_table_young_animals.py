import pymysql

from config_for_database import data_dict
from database.data_for_young_animals import select_query_pets, select_query_pack_animals
from logging_for_database.logging_for_database import logger_info, logger_error


def create_table_young_animals():
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
                query = ("CREATE TABLE IF NOT EXISTS YoungAnimals ("
                         "name varchar(42), "
                         "type varchar(10), "
                         "date_birth date, "
                         "commands varchar(42), "
                         "age_in_month int(50)"
                         ")"
                         )
                cursor.execute(query)
                connection.commit()
                logger_info.info("Table created successfully")

            with connection.cursor() as cursor:
                query_pets = ("INSERT INTO YoungAnimals (name, type, date_birth, commands)"
                              f"{select_query_pets}")
                cursor.execute(query_pets)

                query_pack_animals = ("INSERT INTO YoungAnimals (name, type, date_birth, commands)"
                                      f"{select_query_pack_animals}")
                cursor.execute(query_pack_animals)

                logger_info("Successfully inserted")
                connection.commit()
            with connection.cursor() as cursor:
                query_age = ("UPDATE YoungAnimals "
                             "SET age_in_month = TIMESTAMPDIFF(MONTH, date_birth, CURDATE())")
                cursor.execute(query_age)

                logger_info("Successfully updated")
                connection.commit()
        except pymysql.err.OperationalError:
            logger_error.error("Connection failed")

    except Exception as e:
        logger_error.error("Connection failed", e)
