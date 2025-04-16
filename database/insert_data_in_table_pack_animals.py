import pymysql

from config_for_database import data_dict
from logging_for_database.logging_for_database import logger_info, logger_error
from data_for_pack_animal import (pattern_for_pack_animals,
                                  query_for_dave,
                                  query_for_zorro,
                                  query_for_bak,
                                  query_for_mia,
                                  query_for_kora,
                                  query_for_seli
                                  )


def insert_data_into_table_pack_animal():
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
                cursor.execute(pattern_for_pack_animals, query_for_bak)
                cursor.execute(pattern_for_pack_animals, query_for_seli)
                cursor.execute(pattern_for_pack_animals, query_for_zorro)
                cursor.execute(pattern_for_pack_animals, query_for_dave)
                cursor.execute(pattern_for_pack_animals, query_for_mia)
                cursor.execute(pattern_for_pack_animals, query_for_kora)

                connection.commit()
        except pymysql.err.OperationalError:
            logger_error.error("Connection failed")

    except pymysql.err.OperationalError:
        logger_error.error("Database does not exist")
