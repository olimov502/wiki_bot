import sqlite3



class Database:
    def __init__(self,path_to_db='main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql, parameters: tuple = None, fetchone= False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    @staticmethod
    def format_args(sql, parameters:dict):
        sql+= "AND".join([
            f""
            f"{item}= ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self,id:int, name:str, email: str=None, language: str="uz"):
        # SQL_EXAMPLE= "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1 , 'JOHN', 'JOHN@gmail.com')"

        sql = """
        INSERT INTO myfiles_teacher(id, Name, email, language) VALUES(?,?,?,?)
        """
        self.execute(sql,parameters=(id,name, email, language), commit=True)

    def select_all_users(self):
        sql="""
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        #SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_teacher WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT (*) FROM Users;", fetchone=True)

    def update_user_email(self,email,id):
        sql= f"""
        UPDATE myfiles_teacher SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE ", commit=True)



    def user_qoshish(self, ismi:str,username:str,tg_id:int,vaqt:None):
        # SQL_EXAMPLE= "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1 , 'JOHN', 'JOHN@gmail.com')"

        sql = """
        INSERT INTO wiki_user(ismi,username,tg_id,vaqt) VALUES(?,?,?,?)
        """
        self.execute(sql, parameters=(ismi, username, tg_id, vaqt), commit=True)

def logger(statement):
    print(f"""
-------------------------------------------------
Executing:
{statement}
-------------------------------------------------
""")

