import pymysql

from config_for_database import data_dict
from logging_for_database.logging_for_database import logger_info, logger_error


def create_table_for_all_animals():
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
                query_for_create_tables = ("CREATE TABLE IF NOT EXISTS AllAnimals ("
                                           "name varchar(42), "
                                           "type varchar(10), "
                                           "date_birth date, "
                                           "commands varchar(42),"
                                           "relation varchar(42)"
                                           ")"
                                           )
                cursor.execute(query_for_create_tables)
                logger_info.info("Table created successfully")

                connection.commit()

            with connection.cursor() as cursor:
                query = ("INSERT INTO AllAnimals (name, type, date_birth, commands, relation) "
                         "SELECT name, type, date_birth, commands, 'pets' AS relation FROM Pets "
                         "UNION ALL "
                         "SELECT name, type, date_birth, commands, 'pack_animals' AS relation FROM PackAnimals "
                         )
                cursor.execute(query)
                connection.commit()
        except pymysql.err.OperationalError:
            logger_error.error("Connection failed")
    except Exception as e:
        logger_error.error("Connection failed", exc_info=e)
