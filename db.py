import config
import pymysql

def connect():
    connection = pymysql.connect(
        host=config.values["DB_HOST"],
        user=config.values["DB_USER"],
        password=config.values["DB_PASS"],
        database=config.values["DB_NAME"],
        port=config.values["DB_PORT"],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection
