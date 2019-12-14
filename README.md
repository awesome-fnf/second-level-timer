# FnF second-level timer
This demo shows how to use [Function Flow(FnF)](https://help.aliyun.com/knowledge_detail/114020.html?spm=5176.cnfnf.0.0.726d7458A1oVa6&aly_as=yQh9IDYv) to implements second level [Function Compute(FC)
 ](https://help.aliyun.com/document_detail/52895.html?spm=5176.137990.1214002.btn3.d680224eD7gHbg&aly_as=lrqI6t1QH) function timer. As the FC time trigger only supports 
minute level.

## Requirements
[FC fun](https://github.com/alibaba/funcraft)

## Code structure
`src/timer.py`: FC function to invoke FnF flow. this function invoked by FC time trigger with minute level timer.

`src/handler.py`: Target FC function to been invoked, you can substitute with your own function use any language runtime of FC.

`src/gen.py`: Don't care about this, just a middleware function.

`template.yml`: Use [Aliyun ROS](https://help.aliyun.com/document_detail/28852.html?spm=a2c4g.11186623.6.542.d32454bcyatnN2) service, orchest all resoucrces, this includes:
  - Ram Role `TimerFCRole-<random-suffix>` and `TimerFnFRole-<random-suffix>`
  - FC service `FnFDemoTimer` with role `TimerFCRole-<random-suffix>`
  - Functions `timer` `timer-gen` `timer-handler`
  - Time Trigger `trigger` for function `timer`
  - FnF flow `FnFSecondLevelTimer-<random-suffix>`

## How to use
You can choose any way:
### 1. FC Application center
The implement has been integrated into [FC Application Center](https://fc.console.aliyun.com/fc/applications/cn-shanghai),
you can go to create directly. <br>
![run](https://img.alicdn.com/tfs/TB1CNC1sGL7gK0jSZFBXXXZZpXa-1385-676.gif)


### 2. Scripts
Also you can use the scripts:
1. Directly fun demo see how it works:<br>
   `./deploy.sh`
   This will invoke `timer-handler` function every seconds
   
2. Create or Update resources:<br>
    ```bash
    Action=create StackName=XXX ./deploy.sh
    Action=update StackId=XXX ./deploy.sh
    ```
  
3. Set target function with your own function:<br>
    ```bash
    ResourceArn={Your Function Arn} Action=update StackId=XXX ./deploy.sh
    ```

4. Set second level duration(default 1s):<br>
    ```bash
    Duration=10 Action=update StackId=XXX ./deploy.sh
    ```

5. Set target function input event:<br>
    ```bash
    Input='{\"name\": \"hello world\"}' Action=update StackId=XXX ./deploy.sh
    ```

6. Set sls Project and Logstore<br>
   ```bash
   Project=XXX Logstore=XXX Action=update StackId=XXX ./deploy.sh
   ```
  
**example**<br>
```bash
Action=create StackName=fnf-timer-demo ResourceArn=XXX Input='{\"name\": \"hello world\"} Duration=5' ./deploy.sh
Action=update StackId=03d2ed3e-XXXX-XXX-b839-80d1c08b41f6 ResourceArn=XXX Input='{\"name\": \"hello world\"}' Duration=10 ./deploy.sh
```

