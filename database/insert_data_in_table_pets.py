import pymysql

from config_for_database import data_dict
from logging_for_database.logging_for_database import logger_info, logger_error
from data_for_pets import (pattern_for_pets,
                           query_for_bob,
                           query_for_dak,
                           query_for_gak,
                           query_for_sam,
                           query_for_mike,
                           query_for_chris
                           )


def insert_data_into_table_pets():
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
                cursor.execute(pattern_for_pets, query_for_bob)
                cursor.execute(pattern_for_pets, query_for_dak)
                cursor.execute(pattern_for_pets, query_for_gak)
                cursor.execute(pattern_for_pets, query_for_sam)
                cursor.execute(pattern_for_pets, query_for_mike)
                cursor.execute(pattern_for_pets, query_for_chris)

                connection.commit()
                logger_info.success("Data inserted")
        except pymysql.err.OperationalError:
            logger_error.error("Connection failed")

    except pymysql.err.OperationalError as e:
        logger_error.error("Database does not exist", exc_info=e)
