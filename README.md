# FnF demo
This demo shows how to use [Function Flow(FnF)](https://help.aliyun.com/knowledge_detail/114020.html?spm=5176.cnfnf.0.0.726d7458A1oVa6&aly_as=yQh9IDYv) to implements second level [Function Compute(FC)
 ](https://help.aliyun.com/document_detail/52895.html?spm=5176.137990.1214002.btn3.d680224eD7gHbg&aly_as=lrqI6t1QH) function timer. As the FC time trigger only supports 
minute level.

## Requirements
[FC fun](https://github.com/alibaba/funcraft)

## Code structure
`src/timer.py`: FC function to invoke FnF flow. this function invoked by FC time trigger with minute level timer

`src/handler.py`: Target FC function to been invoked, you can substitute with your own function use any language runtime of FC.

`src/gen.py`: Don't care about this, just a middleware function.

`flow.yml`: FnF flow definition, this will invoke target function

`template.yml`: FC fun template definition to deploy all FC functions and time trigger
``

## How to use
1. Replace `handler.py` to your own target function, which will be invoked every specific seconds

2. Go to [FnF console](https://fnf.console.aliyun.com/fnf/cn-shanghai/flows), create flow with `flow.yml`. for example named flow `demo-timer-seconds`

3. update `template.yml` payload duration and flow_name. For example:
   - every second:<br>
   `{"flow_name": "demo-timer-seconds", "input": {"duration": 1, "data": "hello world"}}`
   - every 5 seconds:<br>
    `{"flow_name": "demo-timer-seconds", "input": {"duration": 5, "data": "hello world"}}`

4. Run `fun deploy` to deploy all functions and time trigger of FC

## Verify
Your `handler.py` corresponding FC function `timer-handler`(defined in template.yml) will be invoked every specific seconds. 
