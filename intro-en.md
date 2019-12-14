## Description

Application provide a second-level time trigger for FC function.


## How to use

After deploy finished, the function specified in `ResourceArn` will be invoked every specified seconds.

![run](https://img.alicdn.com/tfs/TB1CNC1sGL7gK0jSZFBXXXZZpXa-1385-676.gif)

## Framework

Use FnF to implement invoke FC function.<br>
Execution process as below: <br>
1. FC time trigger will invoke function `timer` in minute-level.<br>
2. Function `timer` start execute flow by FnF sdk.<br>
3. FnF flow task step will invoke function `timer-gen`, to generate trigger timestamp sequence.<br>
4. Finally, FnF parallel foreach step will generate a timer task for each timestamp in sequence, to parallel invoke function `timer-hander`.

Framework:
![framework](https://img.alicdn.com/tfs/TB1YgGssF67gK0jSZPfXXahhFXa-1846-1244.jpg)
