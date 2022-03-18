import logging
import sys
file_handler = logging.FileHandler(filename='logs.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(level=logging.DEBUG, format='%(message)s', handlers=handlers)


HEARTBEAT = True
EXTERNAL = True

def enable_external_services(username):
    if HEARTBEAT:
        logging.info("External services are available and can be initialized.")
    else:
        logging.warning("Services are not responding. HTTP connection error.")
        raise Exception


def hello_logsight_user(username="logsight.ai User"):
    logging.info(f"A new logsight.ai user with username: {username} is registered")
    logging.info(f"{username} wants to use logsight GitHub Actions")
    logging.info(f"This will enable him to provide AI-powered log analytics in his own workflows")
    logging.info(f"First let's create a user and write it to the database")

    with open("database.txt", "w") as db:
        logging.info("Writing to the database")
        # Writing data to a file
        db.write(username + "\n")

    logging.info(f"User with username: {username} was successfully added to the database")

    if EXTERNAL:
        try:
            enable_external_services(username)
        except Exception as e:
            logging.info("Service failed with connection timeout")


if __name__ == '__main__':
    hello_logsight_user("logsight")
