import sqlite3


class DatabaseUtil:

    __databaseName = 'GesturefControl-CloudServer'

    __insert_wordcloud_cmd = '''
        INSERT INTO wordcloud (meetingid, wordcloudsvg)
        VALUES (?,?);
    '''

    __select_wordcloud_cmd = '''
        SELECT wordcloudsvg FROM wordcloud WHERE meetingid = ?;
    '''

    def __init__(self):
        conn = sqlite3.connect(self.__databaseName)
        create_wordcloud_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS wordcloud(
                meetingid VARCHAR(25) PRIMARY KEY NOT NULL,
                wordcloudsvg TEXT);
        '''

        conn.execute(create_wordcloud_tb_cmd)
        conn.commit()
        conn.close()


    def insert_wordcloud(self, meetingId: str, svg: str):
        conn = sqlite3.connect(self.__databaseName)
        cur = conn.cursor()
        cur.execute(self.__insert_wordcloud_cmd, (meetingId, svg))
        conn.commit()
        conn.close()

    def select_wordcloud(self, meetingId: str)-> str:
        conn = sqlite3.connect(self.__databaseName)
        cur = conn.cursor()
        cur.execute(self.__select_wordcloud_cmd, (meetingId,))
        result = cur.fetchone()[0]
        conn.close()
        return result




if __name__ == '__main__':
    databaseUtil = DatabaseUtil()
    # databaseUtil.insert_wordcloud('123123', '1234454')
    resule = databaseUtil.select_wordcloud('1')
    print(resule)