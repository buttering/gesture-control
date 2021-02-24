import sqlite3
import config.databaseConfig as dc


# 如果数据库文件不存在，会自动被创建
class databaseUtil:
    # 下面两个增加语句必须同时调用，以保证完整性
    __insert_device_cmd = '''
        INSERT INTO device 
        VALUES(?,?,datetime());
    '''

    __insert_count_cmd = '''
        INSERT INTO count (deviceId)
        VALUES (?);
    '''

    __update_count_cmd = '''
        UPDATE count SET
        {} = ?
        WHERE deviceId = ?;
    '''

    # 字段自动加1
    __update_count_increment_cmd = '''
        UPDATE count SET
        {} = {} + 1
        WHERE deviceId = ?;
    '''

    __select_device_cmd = '''
        SELECT deviceId, password FROM device WHERE deviceId = ?;
    '''

    __select_counts_cmd = '''
        SELECT click, panleft, panright, enlarge, narrow, grasp, cwr, ccwr, cus1, cus2 
        FROM count 
        WHERE deviceId = ?;
    '''

    __select_count_cmd = '''
        SELECT {} FROM count WHERE deviceId = ?;
    '''

    def __init__(self):
        conn = sqlite3.connect(dc.databaseName)
        create_device_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS device(
                deviceId CHAR(50) PRIMARY KEY NOT NULL,
                password CHAR(50),
                attachtime NUMERIC);
        '''
        create_count_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS count(
                deviceId CHAR(50) PRIMARY KEY NOT NULL,
                click INT DEFAULT 0,
                panleft INT DEFAULT 0,
                panright INT DEFAULT 0,
                enlarge INT DEFAULT 0,
                narrow INT DEFAULT 0,
                grasp INT DEFAULT 0,
                cwr INT DEFAULT 0,
                ccwr INT DEFAULT 0,
                cus1 INT DEFAULT 0,
                cus2 INT DEFAULT 0);
        '''
        conn.execute(create_device_tb_cmd)
        conn.execute(create_count_tb_cmd)
        conn.commit()
        conn.close()



    def insert_device(self, device_id: str, password: str):
        conn = sqlite3.connect(dc.databaseName)
        cur = conn.cursor()
        cur.execute(self.__insert_device_cmd, (device_id, password))
        cur.execute(self.__insert_count_cmd, (device_id,))
        conn.commit()
        conn.close()

    def select_device(self, device_id, cur):
        conn = sqlite3.connect(dc.databaseName)
        cur = conn.cursor()
        cur.execute(self.__select_device_cmd, (device_id,))
        result = cur.fetchone()
        conn.commit()
        conn.close()
        return result

    def update_count(self, device_id, gesture: str):
        conn = sqlite3.connect(dc.databaseName)
        cur = conn.cursor()
        # gesture_count = self.select_count(device_id, gesture)[0]
        # cur.execute(self.__update_count_cmd.format(gesture), (gesture_count + 1, device_id))
        cur.execute(self.__update_count_increment_cmd.format(gesture, gesture), (device_id, ))
        conn.commit()
        conn.close()

    def select_counts(self, deviceId: str):
        conn = sqlite3.connect(dc.databaseName)
        cur = conn.cursor()
        cur.execute(self.__select_counts_cmd, (deviceId,))
        result = cur.fetchone()
        conn.close()
        return result

    def select_count(self, deviceId: str, gesture: str):
        conn = sqlite3.connect(dc.databaseName)
        cur = conn.cursor()
        cur.execute(self.__select_count_cmd.format(gesture), (deviceId,))
        # BUG:返回的不是值的数字，而是键的字符串(已解决)
        result = cur.fetchone()
        conn.close()
        return result


if __name__ == '__main__':
    databaseUtil = databaseUtil()
    # databaseUtil.insert_device("ABc","ASD")
    # result = databaseUtil.select_device("ABD")
    databaseUtil.update_count('ABD', 'panright')
    result = databaseUtil.select_count('ABD', 'panright')
    print(result)
