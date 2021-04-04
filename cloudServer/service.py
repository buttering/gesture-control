from flask import Flask
import controller

app = Flask(__name__)
conroller = controller.Controller()

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
    conroller.getWordCloud(meetingId)


@app.route('/wordcloud/<int:meetingId>', methods=['post'])
def produceWordCloud(meetingId):
    pass
