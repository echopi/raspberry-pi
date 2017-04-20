#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time
import commands

def main():

# 需要填自己申请到的yeelink api Key 以及你的数据的url
 apiheaders = {'U-ApiKey': 'ffb6dbee3cdc0ab269117d35e68e1e32', 'content-type': 'application/json'}
 apiurl_cpu = 'http://api.yeelink.net/v1.0/device/351713/sensor/395498/datapoints'
 apiurl_gpu = 'http://api.yeelink.net/v1.0/device/351713/sensor/395497/datapoints'


# 查看GPU温度
 gpu = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
 gpu = float(gpu)
 #print('gpu value:%.2f' % gpu)
 payload_gpu = {'value': gpu}
 r = requests.post(apiurl_gpu, headers=apiheaders, data=json.dumps(payload_gpu))

# 查看CPU温度
 file = open("/sys/class/thermal/thermal_zone0/temp")
 cpu = float(file.read()) / 1000
 file.close()
 payload_cpu = {'value': cpu}
 r = requests.post(apiurl_cpu, headers=apiheaders, data=json.dumps(payload_cpu))
 time.sleep(1)

if __name__ == '__main__':
 main()
