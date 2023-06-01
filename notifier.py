import logging
import psycopg2
import select
from datetime import datetime

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s] %(message)s"))
logging.getLogger().setLevel("INFO")
logging.getLogger().addHandler(console_handler)
_logger = logging.getLogger(__name__)

conn = psycopg2.connect(host="172.17.0.1", port=5432, dbname="foo", user="foo", password="foo", connect_timeout=5)        
curs = conn.cursor()
payload = datetime.now().time().strftime("%M:%S")
curs.execute(f"""NOTIFY foo, '{payload}';""")
curs.close()
conn.commit()
conn.close()