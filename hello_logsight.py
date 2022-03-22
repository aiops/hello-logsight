import logging
import sys

file_handler = logging.FileHandler(filename='hello_logsight.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(level=logging.DEBUG, format='%(message)s', handlers=handlers)

# Set HEARTBEAT to False => COMMIT => PUSH
HEARTBEAT = True
EXTERNAL = True


def enable_external_services(username):
    if HEARTBEAT:
        logging.info(f"External services are available for user: {username}")
    else:
        raise ConnectionError('external service unavailable')


def hello_logsight_user(username="anonymous"):
    logging.info(f"New user registered: {username}")
    logging.info(f"User {username} requests access to logsight GitHub Actions")
    logging.info(f"Enable AI-powered log analytics using CI/CD workflows")
    logging.info(f"Creating new user")

    with open("database.txt", "w") as db:
        logging.info("Writing transaction to database")
        db.write(username)
        logging.info("Transaction completed")

    logging.info(f"User successfully added to database: {username}")

    if EXTERNAL:
        try:
            logging.info(f"Connecting to external services for user: {username}")
            enable_external_services(username)
        except ConnectionError as e:
            logging.info("Connection failed due to timeout: %s", str(e))


if __name__ == '__main__':
    hello_logsight_user("john_miller")
