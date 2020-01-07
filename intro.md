## 应用简介

提供函数计算的秒级别定时触发器，通过部署本应用来实现秒级触发函数的执行。


## 调用示例

应用参数说明：<br>
- ResourceArn: 可自定义的被秒级定时触发的目标函数 Arn
- Input: 可自定义的触发目标函数时的输入，会作为 payload 字段传给目标函数。比如输入 YOUR_INPUT，目标函数会接受到如下输入：
    ```json
    {
     "triggerName":"trigger",
     "triggerTime":"2019-12-12T09:56:05Z",
     "payload": "YOUR_INPUT"
    }
    ```
- Duration: 设定的秒级触发间隔，最好能被 60s 整除，比如 1， 2， 5 等
- Project: 日志服务 sls 的 project
- Logstore: 日志服务 sls 的 logstore

应用部署后，`ResourceArn` 参数中指定的函数会被自动定时触发

![run](https://img.alicdn.com/tfs/TB1OmK9thz1gK0jSZSgXXavwpXa-1385-676.gif)


## 工作原理

借助于 FnF 提供的 [task 任务步骤](https://help.aliyun.com/document_detail/122494.html?spm=a2c4g.11186623.6.572.55fd4d68fJF4H4)、[wait 等待步骤](https://help.aliyun.com/document_detail/122495.html?spm=a2c4g.11186623.6.573.b959114bng035d) 和 [foreach 并行循环步骤](https://help.aliyun.com/document_detail/122499.html?spm=a2c4g.11186623.6.577.3fad57c6DAIV6z)，很方便的实现对 FC 函数定时调用。<br>
执行流程：<br>
1. FC 定时触发器分钟级别触发 `timer` 函数<br>
2. `timer` 函数使用 FnF SDK 执行工作流<br>
3. 工作流中 task 步骤调用 `timer-gen` 函数生成秒级触发时间戳序列<br>
4. 并行循环 foreach 步骤为序列中每个时间戳生成并行定时任务来调用目标函数 `timer-hander`

框架图：
![framework](https://img.alicdn.com/tfs/TB1oYolsGL7gK0jSZFBXXXZZpXa-1478-1002.jpg)

更详细的信息请参考：[秒级定时触发器](https://yq.aliyun.com/articles/739119?msgid=18722108)

