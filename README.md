# gesture-control
Gesture control system for software innovation competition

# 手势对应操作

手势|ppt|图片|腾讯会议|系统任务视图
-|-|-|-|-
点击|进入任务视图|进入任务视图|进入任务视图|进入选中的进程，切换为对应软件的手势模式
向左平移|切换下一个动画|切换上一张|-|在任务视图中切换到上一进程
向右平移|返回上一个动画|切换下一张|-|在任务视图中切换到下一进程
缩放（放大）|转到最后一页|放大|放大系统音量|-
缩放（缩小）|转到第一页|缩小|减小系统音量|-
抓取|获取截图|复制到剪切板|获取截图|-
旋转（顺时针）|屏幕变黑/还原|顺时针旋转|-|-
旋转（逆时针）|屏幕变黑/还原|顺时针旋转|-|-
待添加手势1|-|-|-|-
待添加手势2|-|-|-|-

# 网络接口
- 格式：json字符串格式，使用tcp/ip协议传输
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
向左平移|panleft
向右平移|panright
缩放（放大）|enlarge
缩放（缩小）|narrow
抓取|grasp
旋转（顺时针）|cwr
旋转（逆时针）|ccwr
待添加手势1|cus1
待添加手势2|cus2

### 获取焦点接口
- 描述：获取对系统的控制权，忽略其他人的操作请求
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