from wordcloud import WordCloud
import csv
import matplotlib.pyplot as plt
from imageio import imread
import jieba.analyse


class WordCloudGenerator:

    text_path = r'各位加油队-A12基于手势识别的会议控制系统-数据库设计文档.txt'
    mask_path = r'院徽透明.png'

    def cut_word(self):
        with open(self.text_path, 'r', encoding='utf-8') as file:
            file = file.read()
            cut_text = " ".join(jieba.cut(file))
        return cut_text

    # 统计词频
    '''
    csv文件格式
    <词> <次数>
    '''
    def read_csv_to_dict(self) -> dict:
        dic = {}
        with open(self.csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for columns in reader:
                dic[columns[0]] = int(columns[1])
        return dic

    def analysis_content(self, words):

        wc = WordCloud(
            # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
            font_path='SourceHanSansCN-Normal.ttf',
            # 设置了背景，宽高
            background_color="white",
            width=1000,
            height=880,


        ).generate(words)
        wc.to_file('wordCloud.png')
        #
        # plt.imshow(wc)
        # plt.axis('off')
        # plt.show()

    # 根据字典生成svg格式词云图
    def analysis_content_from_dict(self, frequency: dict):
        wc = WordCloud(
            # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
            font_path='wordCloud/SourceHanSansCN-Normal.ttf',
            # 设置了背景，宽高
            background_color="white",
            width=1000,
            height=880,
        ).generate_from_frequencies(frequency)

        svg = wc.to_svg()
        return svg

if __name__ == '__main__':

    wordcloud = WordCloudGenerator()
    wordStr = wordcloud.cut_word()
    wordcloud.analysis_content(wordStr)
    #
    # dic = {
    #     'q23':11,
    #     'sdfs':34,
    #     'sdfdf':35
    # }
    #
    # wordcloud.analysis_content_from_dict(dic)