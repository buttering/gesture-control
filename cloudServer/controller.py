import dao
from cloudServer.wordCloud import wordCloud

class Controller:


    # 根据文本内容，调用云计算处理，生成单词数量的字典，再生成词云图，储存于数据库中
    def produceWordCloud(self, meetingId: str, recordText: str):
        recordDict = recordText  # TODO：调用hadoop将其转化为单词及其对应数量的字典
        dic = {
            'q23': 11,
            'sdfs': 34,
            'sdfdf': 35
        }
        svg = wordCloud.WordCloudGenerator().analysis_content_from_dict(dic)
        dao.DatabaseUtil().insert_wordcloud(meetingId, svg)

    # 根据会议id获得对应svg格式词云图
    def getWordCloud(self, meetingId: str):
        return dao.DatabaseUtil().select_wordcloud(meetingId)

if __name__ == '__main__':
    controller = Controller()
    controller.produceWordCloud('1',None)