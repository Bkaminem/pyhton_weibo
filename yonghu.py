# -*-coding:utf-8-*-

import os
import traceback
import mysql.connector
from bs4 import BeautifulSoup
import random
import time
import re
import requests
import csv

base_path = os.path.abspath('.')
csv_path = os.path.join(base_path, 'yonghu.csv')

f = open(csv_path, 'w+', newline='', encoding='utf_8_sig')
f_csv = csv.writer(f)



class weibo:
    cookie = {
        "SCF=AuYoiaeWZU78gUdL23SGUTUOytB_aRHky72OM8kyd8wTOuiPov1HnLdn-z2ub2T8WxLJ8ovpYHVMCjZpRxMO5_Q.; _T_WM=3f3c47fe7d1c002dfc8de20cc094495c; SUB=_2A2539SRmDeRhGeVM7loV9CzEwjmIHXVVFkwurDV6PUJbkdAKLUvDkW1NTLEyK32oY98eySdWQOCBa8dXw8p5pmWK; SUHB=0WGc23r-bIKb_c; SSOLoginState=1525765174": '',
    }
    user_agents = [
        "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    ]#用户代理浏览器标识
    UA = random.choice(user_agents)
    header = {'User-Agent': UA}
    sql1 = mysql.connector.connect(user='root', password='960120', host='localhost', database='weibo')
    cur = sql1.cursor()#sql游标




    def get_yonghu_info(self):
        num_num = 1
        name = input("请输入博主ID:")
        try:

                print(name)
                url1 = 'http://weibo.cn/u/%s' % name
                req = requests.get(url1, cookies=self.cookie, headers=self.header)
                num = BeautifulSoup(req.text, 'lxml').find('div', class_='pa', id='pagelist').find_all('input')
                user_name = BeautifulSoup(req.text, 'lxml').find('div', class_='ut').find('span', class_='ctt').get_text().split(' ')[0]
                print(user_name)
                num = int(num[0]['value'])
                print(num)

                num_col = r'\d+'
                for n in range(1, num+1):
                    url2 = 'http://weibo.cn/u/%s?page=%s' % (name, n)
                    print(url2)
                    req2 = requests.get(url2, cookies=self.cookie, headers=self.header)
                    time.sleep(3)
                    target = BeautifulSoup(req2.text, 'lxml').find_all('div', class_='c')
                    if len(target) > 3:#3条为非个人微博内容div
                        for i in range(1, len(target)-2):
                            num_div = target[i].find_all('div')
                            print(len(num_div))
                            if len(num_div) == 3:
                                continue
                            elif len(num_div) ==1:
                                content = num_div[0].find('span',class_='ctt').get_text()
                                content = content.encode('gbk', 'ignore')
                                content = str(content.decode('gbk', 'ignore'))
                                all_num = num_div[0].find_all('a')
                                num_zan = int(re.findall(num_col,all_num[-4].get_text() )[0])
                                num_forw = int(re.findall(num_col,all_num[-3].get_text() )[0])
                                try:
                                    num_comm = int(re.findall(num_col,all_num[-2].get_text() )[0])
                                except:
                                    num_comm = 0
                                print(num_zan)
                                print(num_forw)
                                print(num_comm)
                                print(content)
                                cur_time = num_div[0].find('span', class_='ct').get_text().split(' ')
                                if cur_time[0]:
                                    post_time = str(cur_time[0])

                            else:
                                content_d = num_div[1].find_all('span')
                                if len(content_d) >=2:
                                    continue
                                else:
                                    content = num_div[0].find('span', class_ = 'ctt').get_text()
                                    content = content.encode('gbk', 'ignore')
                                    content = str(content.decode('gbk', 'ignore'))
                                    all_num = num_div[1].find_all('a')
                                    num_zan = int(re.findall(num_col, all_num[-4].get_text())[0])
                                    num_forw = int(re.findall(num_col, all_num[-3].get_text())[0])
                                    try:
                                        num_comm = int(re.findall(num_col, all_num[-2].get_text())[0])
                                    except:
                                        num_comm = 0
                                    print(num_zan)
                                    print(num_forw)
                                    print(num_comm)
                                    print(content)
                                cur_time = num_div[1].find('span', class_='ct').get_text().split(' ')
                                if cur_time[0]:
                                    post_time = str(cur_time[0])

                            sql = 'INSERT INTO yonghu (`user_id`, `user_name`, `content`, `num_zan`,`num_forw`,\
                                        `num_comm`,`post_time`) VALUES ( %(user_id)s, %(user_name)s, %(content)s, %(num_zan)s,\
                                         %(num_forw)s, %(num_comm)s, %(post_time)s)'
                            value = {
                                    'user_id': name,
                                    'user_name': user_name,
                                    'content': content,
                                    'num_zan': num_zan,
                                    'num_forw': num_forw,
                                    'num_comm': num_comm,
                                    'post_time': post_time
                                    }
                            self.cur.execute(sql, value)
                            self.sql1.commit()
                            f_csv.writerow([str(num_num), str(name), str(user_name), str(content), str(num_zan), str(num_forw), str(num_comm), str(post_time)])
                            num_num = num_num + 1
        except Exception as e:
            print("Error: ", e)
            traceback.print_exc()
            f.close()


    def start(self):
        weibo.get_yonghu_info(self)

if __name__ == '__main__':
    wb = weibo()
    wb.start()











