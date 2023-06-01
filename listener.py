import logging
import psycopg2
import select
import time

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s] %(message)s"))
logging.getLogger().setLevel("INFO")
logging.getLogger().addHandler(console_handler)
_logger = logging.getLogger(__name__)

conn = psycopg2.connect(host="172.17.0.1", port=5432, dbname="foo", user="foo", password="foo", connect_timeout=5)        
conn.autocommit = True
curs = conn.cursor()
curs.execute("LISTEN foo;")
while 1:    
    if select.select([conn],[],[],15) == ([],[],[]):
        _logger.info("Timeout")
    else:
        conn.poll()
        _logger.info(f"len(notifies) == {len(conn.notifies)}")
        notifications = []        
        while conn.notifies:
            notifications.append(conn.notifies.pop(0))
        _logger.info(notifications)

        _logger.info("blocking for 5 seconds")
        time.sleep(5)
        _logger.info("continue")
conn.close()