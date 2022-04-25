# -*- coding: utf-8 -*-

import requests
from datetime import datetime
dpeer_time = datetime.strptime('2022-12-24 00:00:00','%Y-%m-%d %H:%M:%S')
today_time = datetime.now()

img_url = ["https://s1.ax1x.com/2022/04/26/LTfiUH.png"]

requests.get(url=f'https://cqhttp.tooziya.com/send_private_msg?access_token=515618@QQ.com&user_id=1501311105&message=同桌 加油鸭！o>_<o 距离考研还有{(dpeer_time-today_time).days}天16时00分00秒了[CQ:image,file={img_url[0]}]')


