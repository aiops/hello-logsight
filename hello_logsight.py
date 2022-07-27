import logging
import sys
import database

file_handler = logging.FileHandler(filename='hello_logsight.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(level=logging.DEBUG, format='%(message)s', handlers=handlers)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error(f"Uncaught exception: {exc_value}")


sys.excepthook = handle_exception


def calculate_total_cost():
    total_cost = 0
    logging.info(f"Starting the process of calculating total cost for a month")
    logging.info(f"Connecting to the database.")
    try:
        db = database.connect()
        logging.info(f"Connection to database is successful")
    except Exception as e:
        logging.error(f"Database connection failed. Reason: {e}")
    logging.info("Starting calculation of the costs")
    while True:
        entry = db.read_entry()
        if entry.isnumeric():
            total_cost += int(entry)
        if not entry:
            break
    logging.info(f"Total cost of operation is: {total_cost}")


if __name__ == '__main__':
    calculate_total_cost()
