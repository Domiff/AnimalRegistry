import logging


logger_info = logging.getLogger('info_logging_for_database')
logger_error = logging.getLogger('error_logging_for_database')


logger_info.setLevel(logging.DEBUG)
file_handler_info = logging.FileHandler('../logs/info_logger_for_database.log')
file_handler_info.setLevel(logging.DEBUG)

logger_error.setLevel(logging.ERROR)
file_handler_error = logging.FileHandler('../logs/error_logger_for_database.log')
file_handler_error.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler_info.setFormatter(formatter)
file_handler_error.setFormatter(formatter)

logger_info.addHandler(file_handler_info)
logger_error.addHandler(file_handler_error)
