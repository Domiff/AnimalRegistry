import pymysql

from config_for_database import data_dict
from logging_for_database.logging_for_database import logger_info, logger_error



def delete_data():
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
                query = ("DELETE FROM PackAnimals WHERE type = %s")
                data = "camel"
                cursor.execute(query, (data,))
                connection.commit()

                logger_info.info("Data deleted successfully")
        except pymysql.err.OperationalError:
            logger_error.error("Connection failed")

    except Exception as e:
        logger_error.error("Connection failed", exc_info=e)
