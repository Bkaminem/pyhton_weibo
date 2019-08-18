# -*-coding:utf-8-*-

import traceback
import mysql.connector
from bs4 import BeautifulSoup
import random
import time
import requests
import re
import os
import csv

base_path = os.path.abspath('.')
csv_path = os.path.join(base_path, 'ht.csv')

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
    ]#用户代理
    UA = random.choice(user_agents)
    header = {'User-Agent': UA}
    sql1 = mysql.connector.connect(user='root', password='960120', host='localhost', database='weibo')
    cur = sql1.cursor()#sql游标


    def get_yonghu_info(self):
        num_num = 0
        name = input("请输入话题:")
        try:
            for i in range(1,100):
                url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23'+name+'%23&page={}'.format(i+1)
                print(url1)
                req = requests.get(url1, cookies = weibo.cookie, headers = self.header)
                time.sleep(3)
                target = BeautifulSoup(req.text, 'lxml').find_all('div', class_ ='c' )
                print(len(target))
                num_col = r'\d+'#抓取数字
                if len(target) > 5:
                    for j in range(4, len(target) - 2):
                        num_div = target[j].find_all('div')
                        print(len(num_div))
                        if len(num_div) == 3:
                            user_name = num_div[0].find('a', class_='nk').get_text()
                            print(user_name)
                            link = 'https://weibo.com/' + num_div[0].find('a', class_='nk')['href'][17:]

                            content = num_div[2].get_text().split('  ')[0].split('//@')[0]
                            content = content.encode('gbk', 'ignore')
                            content = str(content.decode('gbk', 'ignore')[6:])
                            all_num = num_div[2].find_all('a')
                            if all_num[-1].get_text() == '收藏':
                                num_zan = int(re.findall(num_col, all_num[-4].get_text())[0])
                                num_forw = int(re.findall(num_col, all_num[-3].get_text())[0])
                                num_comm = int(re.findall(num_col, all_num[-2].get_text())[0])
                            else:
                                num_zan = int(re.findall(num_col, all_num[-5].get_text())[0])
                                num_forw = int(re.findall(num_col, all_num[-4].get_text())[0])
                                num_comm = int(re.findall(num_col, all_num[-3].get_text())[0])
                            print(num_zan)
                            print(num_forw)
                            print(num_comm)
                            print(content)

                            cur_time = num_div[2].find('span', class_ = 'ct').get_text().split(' ')
                            if cur_time[0]:
                                post_time = str(cur_time[0])
                            zf = 1 #抓取情况
                            picture =0
                        elif len(num_div) == 1:
                            user_name = num_div[0].find('a', class_='nk').get_text()
                            print(user_name)
                            link = 'https://weibo.com/' + num_div[0].find('a', class_='nk')['href'][17:]
                            content = num_div[0].find('span', class_='ctt').get_text()
                            content = content.encode('gbk', 'ignore')
                            content = str(content.decode('gbk', 'ignore'))
                            all_num = num_div[0].find_all('a')
                            if all_num[-1].get_text() == '收藏':
                                num_zan = int(re.findall(num_col, all_num[-4].get_text())[0])
                                num_forw = int(re.findall(num_col, all_num[-3].get_text())[0])
                                num_comm = int(re.findall(num_col, all_num[-2].get_text())[0])
                            else:
                                num_zan = int(re.findall(num_col, all_num[-5].get_text())[0])
                                num_forw = int(re.findall(num_col, all_num[-4].get_text())[0])
                                num_comm = int(re.findall(num_col, all_num[-3].get_text())[0])
                            print(num_zan)
                            print(num_forw)
                            print(num_comm)
                            print(content)
                            cur_time = num_div[0].find('span', class_='ct').get_text().split(' ')
                            if cur_time[0]:
                                post_time = str(cur_time[0])
                            zf = 0 #抓取情况
                        else:
                            user_name = num_div[0].find('a', class_ = 'nk').get_text()
                            print(user_name)
                            link = 'https://weibo.com/' + num_div[0].find('a', class_='nk')['href'][17:]

                            content_d = num_div[1].find_all('span')
                            if len(content_d) >= 2:

                                content = num_div[1].get_text().split('  ')[0].split('//@')[0]
                                content = content.encode('gbk', 'ignore')
                                content = str(content.decode('gbk', 'ignore')[5:])
                                all_num = num_div[1].find_all('a')
                                if all_num[-1].get_text() == '收藏':
                                    num_zan = int(re.findall(num_col, all_num[-4].get_text())[0])
                                    num_forw = int(re.findall(num_col, all_num[-3].get_text())[0])
                                    num_comm = int(re.findall(num_col, all_num[-2].get_text())[0])
                                else:
                                    num_zan = int(re.findall(num_col, all_num[-5].get_text())[0])
                                    num_forw = int(re.findall(num_col, all_num[-4].get_text())[0])
                                    num_comm = int(re.findall(num_col, all_num[-3].get_text())[0])
                                print(num_zan)
                                print(num_forw)
                                print(num_comm)
                                print(content)
                                picture = 0
                                zf = 0

                            else:
                                zf = 0
                                content_zf = num_div[0].find('span', class_ = 'ctt').get_text()
                                content = content_zf.encode('gbk', 'ignore')
                                content = str(content.decode('gbk', 'ignore'))
                                all_num = num_div[1].find_all('a')
                                if all_num[-1].get_text() == '收藏':
                                    num_zan = int(re.findall(num_col, all_num[-4].get_text())[0])
                                    num_forw = int(re.findall(num_col, all_num[-3].get_text())[0])
                                    num_comm = int(re.findall(num_col, all_num[-2].get_text())[0])
                                else:
                                    num_zan = int(re.findall(num_col, all_num[-5].get_text())[0])
                                    num_forw = int(re.findall(num_col, all_num[-4].get_text())[0])
                                    num_comm = int(re.findall(num_col, all_num[-3].get_text())[0])

                            cur_time = num_div[1].find('span', class_='ct').get_text().split(' ')
                            if cur_time[0]:
                                post_time = str(cur_time[0])
                            zf = 0
                            num_num = num_num+1
                        sql = 'INSERT INTO ht (`user_name`, `content`, `post_time`,`zf`, `num_zan`, `num_forw`, `num_comm`, `link`)\
                                                             VALUES (%(user_name)s, %(content)s, %(post_time)s, %(zf)s, %(num_zan)s, %(num_forw)s, %(num_comm)s, %(link)s)'
                        value = {
                            'user_name': user_name,
                            'content': content,
                            'post_time': post_time,
                            'zf': zf,
                            'num_zan': num_zan,
                            'num_forw': num_forw,
                            'num_comm': num_comm,
                            'link': link
                        }
                        self.cur.execute(sql, value)
                        self.sql1.commit()
                        f_csv.writerow([str(num_num), str(user_name), str(content), str(post_time), str(zf), str(num_zan), str(num_forw,), str(num_comm), str(link)])
                        num_num = num_num + 1
        except Exception as e:
            print("Error: ", e)
            traceback.print_exc()

    def start(self):
        weibo.get_yonghu_info(self)



if __name__ == '__main__':

    wb = weibo()
    wb.start()





















