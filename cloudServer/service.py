from flask import Flask

app = Flask(__name__)


@app.route('/meeting/<int:meetingId>', methods=['get'])
def addMeeting(meetingId):
    pass


@app.route('/meeting/<int:meetingId>', methods=['post'])
def getMeeting(meetingId):
    pass


@app.route('/user/<string:userId>', methods=['get'])
def getUser(userId):
    pass


@app.route('/user/<string:userId>', methods=['post'])
def addUserInfo(userId):
    pass


@app.route('/user/<string:userId>', methods=['add'])
def addUser(userId):
    pass


@app.route('/wordcloud/<int:meetingId>', methods=['get'])
def getWordCloud(meetingId):
    pass


@app.route('/wordcloud/<int:meetingId>', methods=['post'])
def produceWordCloud(meetingId):
    pass
