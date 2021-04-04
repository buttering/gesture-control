class controller:
    # 根据文本内容，调用云计算处理，生成单词数量的字典，再生成词云图，储存于数据库中
    def produceWordCloud(self, recordText: str):
        recordDict = recordText  # TODO：调用hadoop将其转化为单词及其对应数量的字典
