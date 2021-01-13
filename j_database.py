import psycopg2
class Database():
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database="",
                user="",
                password="",
                host="",
                port=""
            )
            self.cursor = self.connection.cursor()
            print("connected")
        except:
            print("Cannot Connect")
    def get_list(self, user_id):
        self.connection = psycopg2.connect(
            database="",
            user="",
            password="",
            host="",
            port=""
        )
        self.cursor = self.connection.cursor()
        print("connected")
        info_command = "select name, todo from juan"
        self.cursor.execute(info_command)
        rows = self.cursor.fetchall()
        for i in rows:
            if user_id == i[0]:
                return i[1]
        self.cursor.close()
        self.connection.close()
    def query(self,user_id):
        self.connection = psycopg2.connect(
            database="",
            user="",
            password="",
            host="",
            port=""
        )
        self.cursor = self.connection.cursor()
        print("connected")
        query_command = "select name, todo from juan"
        self.cursor.execute(query_command)
        rows = self.cursor.fetchall()
        for con in rows:
            if str(user_id) == con[0]:
                return con[1], True
        self.cursor.close()
        self.connection.close()
    def update(self, name, content):
        self.connection = psycopg2.connect(
            database="",
            user="",
            password="",
            host="",
            port=""
        )
        self.cursor = self.connection.cursor()
        self.name = name
        self.content = content
        update_command = "update juan set todo = '" + content + "' where name = '" + name +"'"
        self.cursor.execute(update_command)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("update success")
    def insert(self, name, content):
        self.connection = psycopg2.connect(
            database="",
            user="",
            password="",
            host="",
            port=""
        )
        self.cursor = self.connection.cursor()
        self.name = name
        self.content = content
        insert_command = "insert into juan (name, todo) values('"+ self.name + "', '" + self.content + "')"
        self.cursor.execute(insert_command)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("success")
    def delete(self, name):
        self.connection = psycopg2.connect(
            database="",
            user="",
            password="",
            host="",
            port=""
        )
        self.cursor = self.connection.cursor()
        self.name = name
        print(self.name)
        delete_command = "delete from juan where name = '" + self.name + "'"
        self.cursor.execute(delete_command)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
