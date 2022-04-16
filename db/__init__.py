import sqlite3

class DB:
    """Создание рабочего пространства"""
    def __init__(self,db_name,work,obj=None):
        self.bot = work
        self.db = sqlite3.connect(db_name)
        self.cur = self.db.cursor()
        self.obj = obj
        self.members = [None]
        if self.obj != None:
            obj['db']=self.db,
            obj['cur']=self.cur

    """Загрузка профиля пользователя"""
    def load_member(self,member):
        chall = self.cur.execute(f"SELECT * FROM users WHERE id=?",(str(member.name),)).fetchall()
        if chall == []:
            add = (member.name, member.name, f'<@{member.id}>')
            self.cur.execute(f"INSERT INTO users (id, nickname, mention, money) VALUES (?,?,?, 100)", add)
            self.db.commit()
            return_list = None
            return return_list
        else:
            if member.id not in self.members:
                return_list = [chall[0][2],chall[0][3]]
                return return_list

    """Работа с профилями"""
    def check(self,member,type):
        if type == 1:
            chall = self.cur.execute(f"SELECT * FROM users WHERE id=?", (str(member.name),)).fetchall()
            if chall == []:
                return False
            else:
                return True

    """Взаимодействие с квестами"""
    def quest_add(self):
        pass

    def end_quest(self):
        pass

    def quest_get(self,_id):
        chall = self.cur.execute(f'SELECT * FROM new_quest WHERE id=?',_id)
        if chall == []:
            pass

    def check_quest(self,member):
        pass

    def get_quests(self,member):
        chall = self.cur.execute(f"SELECT * FROM quest WHERE id=?",(str(member.name),)).fetchall()
        if chall == []:
            return_list = None
            return return_list
        else:
            return_list = chall
            return return_list

    def get_quest(self,member,quest):
        chall = self.cur.execute(f"SELECT * FROM quest WHERE id=? AND name=?",
                                 (str(member.name),str(quest))).fetchall()
        if chall == []:
            return_list = None
            return return_list
        else:
            return_list = chall
            return return_list

    """Удаление рабочего пространства"""
    def __del__(self):
        self.db.close()
        if self.obj != None:
            self.obj['db']=None
            self.obj['cur']=None
        return '[db] Closed'