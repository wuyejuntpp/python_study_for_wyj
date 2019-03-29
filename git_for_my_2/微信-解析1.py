import requests
import time
def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    print('得到金山词霸每天一句源码：%s'%r.json())
    contents = r.json()['content']
    print('获取源码中的每天一句:%s'%(r.json()['note']))
    print('获取源码中的每天一句:%s'%(r.json()['translation'][5:]))
    translation = r.json()['translation']
    return contents, translation


#获取北京天气
def getweather():
    url='http://wthrcdn.etouch.cn/WeatherApi?city=杭州'
    weather=requests.get(url).content#获取返回的文本
    return weather
wea=getweather()

#xml转json
import xmltodict
import json
def xml_2_json(xml):
    xml_=xmltodict.parse(xml,encoding='utf-8')
    json_str=json.dumps(xml_,indent=4)
    return json_str

#api返回数据XML格式转json字符串后转字典
xmljson=xml_2_json(wea)
print(type(xmljson))
num_kong=xmljson.replace('null','"kong"')
# print(eval(num_kong))

# print(eval(num_kong)['resp']['forecast'])
list=eval(num_kong)['resp']['forecast']['weather']
for i in range(len(list)):
    print(str(list[i]).replace('high','最高温度'))

    # print(str(i).replace('low','最低温度'))
# print([i for i in list ])
print(eval(num_kong)['resp']['zhishus']['zhishu'][0])



