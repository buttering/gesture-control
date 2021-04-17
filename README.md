# gesture-control
Gesture control system for software innovation competition

# 手势对应操作
**以下手势需要获取焦点后可执行**

手势|ppt|图片|会议软件|系统任务视图|视频
-|-|-|-|-|-
点击|进入任务视图|进入任务视图|进入任务视图|进入选中的进程，切换为对应软件的手势模式|进入任务视图
向左平移|切换下一个动画|切换下一张|-|在任务视图中切换到上一进程|-
向右平移|返回上一个动画|切换上一张|-|在任务视图中切换到下一进程|-
缩放（放大）|转到最后一页|放大|放大系统音量|-|放大音量
缩放（缩小）|转到第一页|缩小|减小系统音量|-|减小音量
抓取|获取截图|复制到剪切板|获取截图|-|播放\暂停
旋转（顺时针）|屏幕变黑/还原|顺时针旋转|-|-|-
旋转（逆时针）|屏幕变黑/还原|逆时针旋转|-|-|-
待添加手势1|-|-|-|-|-
待添加手势2|-|-|-|-|-

**以下为全局手势，任何人无需获取焦点即可执行**
- 点赞
- 点踩
# 网络接口（tcp）
此部分描述客户端之间的网络通信接口，即控制者与操作者的接口

格式：json字符串格式，使用tcp/ip协议传输
### 操作接口
- 描述：摄像头检测到对应动作后，根据手势完成相应操作
- 字段：
```json
{
  "interface": "gesture",
  "info": {
    "gesturename": <gestureName>,
    "deviceid": <deviceId>
    }
}
```

- gestureName对应值：

手势|值
-|-
点击|click
向左平移|panLeft
向右平移|panRight
缩放（放大）|enlarge
缩放（缩小）|narrow
抓取|grasp
旋转（顺时针）|cwr
旋转（逆时针）|ccwr
点赞 | like
点踩 | unlike
待添加手势1|cus1
待添加手势2|cus2

### 获取焦点接口
- 描述：当检测到特定手势（pulling hand in），获取对系统的控制权，忽略其他人的操作请求
- 字段
```json
{
  "interface": "controlFocus",
  "info": {
    "deviceid": <deviceId>
  }
}
```
deviceId为设备的唯一标识符

### 设备注册接口
- 描述：客户端注册到服务器，以支持客户端对服务端的操作
- 字段
```json
{
  "interface": "attach",
  "info": {
    "deviceid": <deviceId>
  }
}
```
TODO:身份鉴权

# 网络接口（http）
此部分描述客户端与云端服务器之间的网络通信接口

格式：使用restful风格，采用http协议
统一响应格式：
```json
{
    "code":状态响应码
    "msg":响应信息
    "data":返回数据
}
```

### https://zhaxzhax/meeting/{meetingId}
#### -get: 获得某次会议的记录，包括会议信息和手势信息
- return

```json
{
    "meetingid":会议id标识,
    "begin": 会议开始时间,
    "end":会议结束时间,
    "author": 主持人,
    "gesture": [
        {
            "userid": 用户id（会议中每个与会者对应一条记录）,
            "click": 点击次数,
            "panleft": 左移次数,
            "panreight": 右移次数,
            "enlarge":放大次数,
            "narrow":缩小次数,
            "grasp":抓取次数,
            "cwr":顺时针旋转次数,
            "ccwr":逆时针旋转次数,
            "like":点赞次数,
            "unlike":点踩次数,
            "focus":获取焦点次数 
        }
    ]
}
```

#### -post：提交某次会议的记录

- 请求体：
```json
{
    "meetingid":会议id标识,
    "begin": 会议开始时间,
    "end":会议结束时间,
    "author": 主持人,
    "gesture": [
        {
            "userid": 用户id（会议中每个与会者对应一条记录）,
            "click":  点击次数,
            "panleft": 左移次数,
            "panreight": 右移次数,
            "enlarge":放大次数,
            "narrow":缩小次数,
            "grasp":抓取次数,
            "cwr":顺时针旋转次数,
            "ccwr":逆时针旋转次数,
            "like":点赞次数,
            "unlike":点踩次数,
            "focus":获取焦点次数 
        }
    ]
}
```

### https://zhaxzhax/user/{userid}
#### -add：新增用户
- 请求体：
```json
{
    password：密码
}
```
#### -get:获取用户信息
#### -post：修改用户信息

### https://zhaxzhax/wordcloud/{meetingid}
#### -get：获得某次会议的词云图
- return:
图片的字节码
  
#### -post：上传某次会议的文本信息
- 请求体:
utf-8格式的会议记录文本

# 图形界面与核心功能的接口
## 有三个类：recogilizer、controller和manager
## recogilizer:
### 负责识别相关的工作
- start():开始识别
- setOnStateChangedListener():设置状态改变监听器，当手势状态更改时会回调该监听器。
- close():关闭识别，关闭识别后仍可以用start()在次开始。
## 关于手势与动作的映射：
manager将手势转化为动作，然后通过网络发送给另一个manager，这个manager在接收到动作后，使用controller.runAction()执行相应动作。
## controller:
- runAction(action):执行动作action
- 这里的action用来表示如左移，放大，旋转等动作
### controller抽象了命令实现的细节，使得在不同系统上只需改变controller的代码就可以实现相同的动作，其次，在改变了controller的代码后，无需修改其他代码。
## manager:
- addOnStateChangedListener():添加状态改变监听器。
- get...():获取...信息。
### manager负责管理会议，可向其询问会议信息，信息有两种获取方法：
- 设置监听器，监听状态的改变
- 直接使用对应的get()方法
有些信息只实现这两种接口的一种以优化性能。
## manager:
- connect(meetingID):加入meetingID标识的会议
- createMeeting(): 创建一个会议，返回meetingID。
### 暂时只考虑一台机器只处于一个会议下。
