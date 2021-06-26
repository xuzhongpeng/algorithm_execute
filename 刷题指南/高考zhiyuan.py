import requests,time #导入库
import re
#制作请求头

headers={
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

#未来提高代码的效率，没有对输入内容进行判断
major = '计算机' #input("请查询输入专业：")

times = 2020 #input("请输入查询年份(2014~2018)：")

for i in range(32,968,1):#学校id从[32,967),省略前面部分可以节约时间
  url = f'https://api.eol.cn/gkcx/api/?access_token=&local_province_id=52&local_type_id=1&page=1&school_id={i}&signsafe=&size=20&uri=apidata/api/gk/score/special&year='+str(times)
  url = f'https://static-data.eol.cn/www/2.0/schoolspecialindex/{str(times)}/{i}/50/1/7/1.json'
  time.sleep(0.1) #暂停时间模拟人为请求
  res = requests.get(url=url,headers=headers)
  if 'data' in res.json():
    for items in res.json()['data']['item']:
      if('spname' in items): #存在spname才执行，如西南科技大学
        if (re.match( r'计算机|软件|人工智能', items['spname'], re.M|re.I) and 'min_section' in  items and  int(items['min_section']) > 19000 and int(items['min_section']) < 30000):
          id=items['school_id']
          s = requests.get(url=f'https://static-data.eol.cn/www/2.0/school/{id}/info.json',headers=headers)
          info = {}
          school = s.json()
          if 'data' in school:
            info = school['data']
          print(items['school_id'],'\t',info['name'],'\t',info['belong'],'\t',items['spname'],'\t',str(times)+"年",'\t',"平均分：",items['average'],'\t',"最低分：",items['min'],'\t',"最低位次:",items['min_section'],'\t',"录取批次:",items['local_batch_name'],'\n')
print(str(times)+"年全国"+str(major)+"专业录取信息查询完成！") #所有数据遍历完成后才会打印它