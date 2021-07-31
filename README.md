# Robotics

## 環境

- python 3.6.8



## 使用方式



**資料夾結構**

```shell
project/
├─ actions/
│  ├─ bird.csv
│  ├─ bottle.csv
│  ├─ bowl.csv
│  ├─ cake.csv
│  ├─ car.csv
│  ├─ cat.csv
│  ├─ human.csv
│  ├─ knife.csv
│  ├─ reset.csv
├─ main.py
```



**範例程式**

這隻程式會撥放在``actions\car.csv``裡面得內容，將機器人動作輸出至``COM1``

```python
from robotics.concrete.command import RoboticsCommandFactory
from robotics.framework.action import CSVAction, Action
from robotics.concrete.robot import RoboticsRobot


def getActionFromName(name: str) -> Action:
    return CSVAction('actions/{name}.csv'.format(name=name), RoboticsCommandFactory())


if __name__ == '__main__':
    bot = RoboticsRobot('COM1')
    bot.doAction(getActionFromName("car"))
    bot.close()
```



``actions\car.csv``內容如下

第一行的各元素分別代表

- **id** : robotic馬達的id
- **pos** :要移動到的位置
- **speed** :馬達速度
- **delay** :暫停n秒



csv檔也可以使用**微軟的excel編輯**

```
id,pos,speed,delay
1,2000,50,
6,1990,50,
2,2048,50,
7,2048,50,
3,838,50,
8,208,50,
4,512,50,
9,450,50,
,,,3
1,2982,50,
6,1000,50,
2,2048,50,
7,2048,50,
3,838,50,
8,208,50,
4,512,50,
9,450,50,
,,,3
1,2982,50,
6,1000,50,
2,2300,50,
7,1800,50,
3,838,50,
8,208,50,
4,512,50,
9,450,50,
,,,0.75
1,3182,50,
6,1200,50,
2,2300,50,
7,1800,50,
3,838,50,
8,208,50,
4,512,50,
9,450,50,
,,,0.75
1,2782,50,
6,800,50,
2,2300,50,
7,1800,50,
3,834,50,
8,205,50,
4,512,50,
9,450,50,
,,,0.75
1,3182,50,
6,1200,50,
2,2300,50,
7,1800,50,
3,838,50,
8,208,50,
4,512,50,
9,450,50,
,,,0.75
1,2782,50,
6,800,50,
2,2300,50,
7,1800,50,
3,834,50,
8,205,50,
4,512,50,
9,450,50,
,,,0.75
1,2982,50,
6,1000,50,
2,2048,50,
7,2048,50,
3,838,50,
8,208,50,
4,512,50,
9,450,50,
,,,0.75
1,2000,50,
6,1990,50,
2,2048,50,
7,2048,50,
3,838,50,
8,208,50,
4,512,50,
```