import mysql.connector
from mysql.connector import Error

class DBConnector:
    def __init__(self, host, user, password, database):
        """数据库连接配置"""
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
    
    def execute_query(self, query, params=None):
        """执行SQL查询"""
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()
        except Error as e:
            print(f"Database error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()