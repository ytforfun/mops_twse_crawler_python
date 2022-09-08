import sqlite3


class MyDB:
    def __init__(self, db_name, reset=False):
        self.conn = sqlite3.connect(db_name)
        self.SQL = MySQL()
        if reset:
            self.reset()

    def reset(self):
        cur = self.conn.cursor()
        cur.executescript(self.SQL.create_data())

    def insert_data(self, year, input_data):
        cur = self.conn.cursor()
        cur.executescript(self.SQL.insert_data(year, input_data))
        self.conn.commit()

    def disconnect(self):
        self.conn.close()

    def check_year(self, year):
        cur = self.conn.cursor()
        cur.execute(self.SQL.check_year(year))
        if cur.fetchall():
            return 1
        return 0


class MySQL:
    def __init__(self):
        pass

    @staticmethod
    def create_data() -> str:
        return f"""
            DROP TABLE IF EXISTS data;
            create table IF NOT EXISTS data(
                id integer primary key AUTOINCREMENT, 
                year integer,
                industry, 
                stock_id integer, 
                name, 
                total_salary integer, 
                total_employee integer, 
                avg_salary integer,
                med_salary integer
            )
            """

    @staticmethod
    def insert_data(year: int, t: list) -> str:
        return f"""
            insert into data (year, industry, stock_id, name, total_salary, total_employee, avg_salary, med_salary)
            values ({int(year)}, '{t[0]}', {int(t[1])}, '{t[2]}', {int(t[3])}, 
                    {int(t[4])}, {int(t[5])}, {int(t[7])});
            """

    @staticmethod
    def check_year(y: int) -> str:
        return f"""
            select year from data where year = {y}
            """


if __name__ == '__main__':
    db = MyDB('default.db', reset=False)
