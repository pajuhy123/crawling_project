# parser.py
import time
import logging
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")
import django
django.setup()

###########
from blog.models import CrawlingData
###########
#data = requests.get("url")  
#print(data.encoding) // 키 값 알아내는 법,,//키==싸이트의 인코딩 방식
encoding_map = {'437': 'cp437',
 '646': 'ascii',
 '850': 'cp850',
 '852': 'cp852',
 '855': 'cp855',
 '857': 'cp857',
 '860': 'cp860',
 '861': 'cp861',
 '862': 'cp862',
 '863': 'cp863',
 '865': 'cp865',
 '866': 'cp866',
 '869': 'cp869',
 '8859': 'latin_1',
 '932': 'cp932',
 '936': 'gbk',
 '949': 'cp949',
 '950': 'cp950',
 'CP-GR': 'cp869',
 'CP-IS': 'cp861',
 'EBCDIC-CP-BE': 'cp500',
 'EBCDIC-CP-CH': 'cp500',
 'EBCDIC-CP-HE': 'cp424',
 'IBM037': 'cp037',
 'IBM039': 'cp037',
 'IBM424': 'cp424',
 'IBM437': 'cp437',
 'IBM500': 'cp500',
 'IBM775': 'cp775',
 'IBM850': 'cp850',
 'IBM852': 'cp852',
 'IBM855': 'cp855',
 'IBM857': 'cp857',
 'IBM860': 'cp860',
 'IBM861': 'cp861',
 'IBM862': 'cp862',
 'IBM863': 'cp863',
 'IBM864': 'cp864',
 'IBM865': 'cp865',
 'IBM866': 'cp866',
 'IBM869': 'cp869',
 'L1': 'latin_1',
 'L2': 'iso8859_2',
 'L3': 'iso8859_3',
 'L4': 'iso8859_4',
 'L5': 'iso8859_9',
 'L6': 'iso8859_10',
 'L8': 'iso8859_14',
 'U16': 'utf_16',
 'U7': 'utf_7',
 'U8': 'utf_8',
 'UTF': 'utf_8',
 'UTF-16BE': 'utf_16_be',
 'UTF-16LE': 'utf_16_le',
 'arabic': 'iso8859_6',
 'big5-hkscs': 'big5hkscs',
 'big5-tw': 'big5',
 'chinese': 'gb2312',
 'cp1361': 'johab',
 'cp154': 'ptcp154',
 'cp819': 'latin_1',
 'cp936': 'gbk',
 'csbig5': 'big5',
 'csiso2022jp': 'iso2022_jp',
 'csiso2022kr': 'iso2022_kr',
 'csiso58gb231280': 'gb2312',
 'csptcp154': 'ptcp154',
 'csshiftjis': 'shift_jis',
 'cyrillic': 'iso8859_5',
 'cyrillic-asian': 'ptcp154',
 'euc-cn': 'gb2312',
 'euccn': 'gb2312',
 'eucgb2312-cn': 'gb2312',
 'eucjis2004': 'euc_jis_2004',
 'eucjisx0213': 'euc_jisx0213',
 'eucjp': 'euc_jp',
 'euckr': 'euc_kr',
 'gb18030-2000': 'gb18030',
 'gb2312-1980': 'gb2312',
 'gb2312-80': 'gb2312',
 'greek': 'iso8859_7',
 'greek8': 'iso8859_7',
 'hebrew': 'iso8859_8',
 'hkscs': 'big5hkscs',
 'hz-gb': 'hz',
 'hz-gb-2312': 'hz',
 'hzgb': 'hz',
 'ibm1026': 'cp1026',
 'ibm1140': 'cp1140',
 'iso-2022-jp': 'iso2022_jp',
 'iso-2022-jp-1': 'iso2022_jp_1',
 'iso-2022-jp-2': 'iso2022_jp_2',
 'iso-2022-jp-2004': 'iso2022_jp_2004',
 'iso-2022-jp-3': 'iso2022_jp_3',
 'iso-2022-jp-ext': 'iso2022_jp_ext',
 'iso-2022-kr': 'iso2022_kr',
 'iso-8859-1': 'latin_1',
 'iso-8859-10': 'iso8859_10',
 'iso-8859-13': 'iso8859_13',
 'iso-8859-14': 'iso8859_14',
 'iso-8859-15': 'iso8859_15',
 'iso-8859-2': 'iso8859_2',
 'iso-8859-3': 'iso8859_3',
 'iso-8859-4': 'iso8859_4',
 'iso-8859-5': 'iso8859_5',
 'iso-8859-6': 'iso8859_6',
 'iso-8859-7': 'iso8859_7',
 'iso-8859-8': 'iso8859_8',
 'iso-8859-9': 'iso8859_9',
 'iso-ir-58': 'gb2312',
 'iso2022jp': 'iso2022_jp',
 'iso2022jp-1': 'iso2022_jp_1',
 'iso2022jp-2': 'iso2022_jp_2',
 'iso2022jp-2004': 'iso2022_jp_2004',
 'iso2022jp-3': 'iso2022_jp_3',
 'iso2022jp-ext': 'iso2022_jp_ext',
 'iso2022kr': 'iso2022_kr',
 'iso8859-1': 'latin_1',
 'jisx0213': 'euc_jis_2004',
 'korean': 'euc_kr',
 'ks_c-5601': 'euc_kr',
 'ks_c-5601-1987': 'euc_kr',
 'ks_x-1001': 'euc_kr',
 'ksc5601': 'euc_kr',
 'ksx1001': 'euc_kr',
 'latin': 'latin_1',
 'latin1': 'latin_1',
 'latin2': 'iso8859_2',
 'latin3': 'iso8859_3',
 'latin4': 'iso8859_4',
 'latin5': 'iso8859_9',
 'latin6': 'iso8859_10',
 'latin8': 'iso8859_14',
 'maccentraleurope': 'mac_latin2',
 'maccyrillic': 'mac_cyrillic',
 'macgreek': 'mac_greek',
 'maciceland': 'mac_iceland',
 'maclatin2': 'mac_latin2',
 'macroman': 'mac_roman',
 'macturkish': 'mac_turkish',
 'ms-kanji': 'cp932',
 'ms1361': 'johab',
 'ms932': 'cp932',
 'ms936': 'gbk',
 'ms949': 'cp949',
 'ms950': 'cp950',
 'mskanji': 'cp932',
 'pt154': 'ptcp154',
 's_jis': 'shift_jis',
 's_jisx0213': 'shift_jisx0213',
 'shiftjis': 'shift_jis',
 'shiftjis2004': 'shift_jis_2004',
 'shiftjisx0213': 'shift_jisx0213',
 'sjis': 'shift_jis',
 'sjis2004': 'shift_jis_2004',
 'sjis_2004': 'shift_jis_2004',
 'sjisx0213': 'shift_jisx0213',
 'u-jis': 'euc_jp',
 'uhc': 'cp949',
 'ujis': 'euc_jp',
 'us-ascii': 'ascii',
 'utf16': 'utf_16',
 'utf8': 'utf_8',
 'windows-1250': 'cp1250',
 'windows-1251': 'cp1251',
 'windows-1252': 'cp1252',
 'windows-1253': 'cp1253',
 'windows-1254': 'cp1254',
 'windows-1255': 'cp1255',
 'windows-1257': 'cp1257',
 'windows-1258': 'cp1258',
 'windows1256': 'cp1256',

}

def delete():
    a=CrawlingData.objects.all()
    a.delete()

def parse():
    ## 설정
    data={
               0 : { },#instiz
               1  : { },#clien
               2 :  { },#fmkorea
               3 : { },#ou
               4 : { },#pan
               5 : { }, #slr
               6 : { }, #mlb
               7 : { },#inben
               8 : { },#ruri
               9 : { },#utde
              10 : { },#bobe
               11 : { },#ygosu
               12 : { },#drip
               13 : { },#theqoo
               14 : { },#dogge
               15 : { }, #namsung
               16 : { }, #flash1
               17 : { }, #flash2
               18 : { }, #dream1
               19 : { }, #dream2
               20 : { }, #bobe2
               21 : { },#fomos1
               22 : { },#fomos2
               23 : { },#ilbe
    }
    #instiz
    req = requests.get('http://www.instiz.net/bbs/list.php?id=pt&srd=1&srt=3&k=&stype=&stype2=&stype3=').text
    soup_instiz = BeautifulSoup(req, 'html.parser')
    #clien
    req = requests.get('https://www.clien.net/service/group/board_all?od=T33').text
    soup_clien = BeautifulSoup(req, 'html.parser')
    #fmkorea
    req = requests.get('http://www.fmkorea.com/index.php?mid=best&listStyle=list&page=1').text
    soup_fmkorea = BeautifulSoup(req, 'html.parser')
    #ou
    req = requests.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest').text
    soup_ou = BeautifulSoup(req, 'html.parser')
    #pan
    req = requests.get('http://pann.nate.com/talk/ranking').text
    soup_pan = BeautifulSoup(req, 'html.parser')
    #slr
    req = requests.get('http://www.slrclub.com/bbs/zboard.php?id=best_article&category=1&setsearch=category').text
    soup_slr = BeautifulSoup(req, 'html.parser')
    #mlb
    req = requests.get('http://mlbpark.donga.com/mp/best.php?b=bullpen&m=view').text
    soup_mlb = BeautifulSoup(req, 'html.parser')
    #inben
    req = requests.get('http://www.inven.co.kr/board/powerbbs.php?come_idx=2097&query=list&my=chu&category=%EC%9C%A0%EB%A8%B8&sort=PID&name=&subject=&content=&keyword=&orderby=&iskin=webzine').text
    soup_inben = BeautifulSoup(req, 'html.parser')
    #ruri
    req = requests.get('http://bbs.ruliweb.com/best/selection').text
    soup_ruri = BeautifulSoup(req, 'html.parser')
    #utde
    req = requests.get('http://web.humoruniv.com/board/humor/list.html?table=pds&st=day').text.encode(encoding_map['iso-8859-1'])
    soup_utde = BeautifulSoup(req, 'html.parser')
    #bobe
    req = requests.get('http://www.bobaedream.co.kr/list?code=best').text.encode(encoding_map['iso-8859-1'])
    soup_bobe = BeautifulSoup(req, 'html.parser')
    #ygosu
    req = requests.get('http://www.ygosu.com/community/real_article').text
    soup_ygosu = BeautifulSoup(req, 'html.parser')
    #drip
    req = requests.get('http://www.dogdrip.net/index.php?mid=dogdrip&page=1&sort_index=voted_count&order_type=desc').text
    soup_drip = BeautifulSoup(req, 'html.parser')
    #theqoo
    req = requests.get('http://theqoo.net/tbest?filter_mode=normal').text
    soup_theqoo = BeautifulSoup(req, 'html.parser')
    #dogge
    req = requests.get('http://dkbnews.donga.com/Board?p=1&tcode=bbs_dkbnews&s=date&key=&query=').text
    soup_dogge = BeautifulSoup(req, 'html.parser')
    #namsung
    req1= requests.get('http://nsbu.co.kr/bbs/board.php?bo_table=ggolit').text
    soup_namsung1 = BeautifulSoup(req1, 'html.parser')
    req2 = requests.get('http://nsbu.co.kr/bbs/board.php?bo_table=celeb').text
    soup_namsung2 = BeautifulSoup(req2, 'html.parser')
    #flash1
    req1= requests.get('http://flash24.dreamx.com/g4/bbs/board.php?bo_table=star&page=2&page=1').text.encode(encoding_map['iso-8859-1'])
    soup_flash1 = BeautifulSoup(req1, 'html.parser')
    #flash2
    req2 = requests.get('http://flash24.dreamx.com/g4/bbs/board.php?bo_table=photo').text.encode(encoding_map['iso-8859-1'])
    soup_flash2 = BeautifulSoup(req2, 'html.parser')
    #dream1
    req1= requests.get('http://newsbbs.dreamx.com/list.do?bid=cnt_star&is_image=Y').text
    soup_dream1 = BeautifulSoup(req1, 'html.parser')
    #dream2
    req2 = requests.get('http://newsbbs.dreamx.com/list.do?bid=cnt_humor&is_image=Y').text
    soup_dream2 = BeautifulSoup(req2, 'html.parser')
    #bobe2
    req1= requests.get('http://www.bobaedream.co.kr/list?code=girl&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=Subject&s_key=&level_no=&vdate=&type=list&page=1')
    req1 =req1.text.encode(encoding_map['iso-8859-1'])
    soup_bobe2 = BeautifulSoup(req1, 'html.parser')
    #fomos1
    req1= requests.get('http://www.fomos.kr/talk/article_list?bbs_id=5').text
    soup_fomos1 = BeautifulSoup(req1, 'html.parser')
    req2 = requests.get('http://www.fomos.kr/talk/article_list?bbs_id=6').text
    soup_fomos2 = BeautifulSoup(req2, 'html.parser')
    #fomos2
    req1= requests.get('http://www.fomos.kr/talk/article_list?bbs_id=3').text
    soup_fomos3 = BeautifulSoup(req1, 'html.parser')
    req2 = requests.get('http://www.fomos.kr/talk/article_list?bbs_id=4').text
    soup_fomos4 = BeautifulSoup(req2, 'html.parser')
    #ilbe
    req1= requests.get('http://www.ilbe.com/ilbe').text
    soup_ilbe = BeautifulSoup(req1, 'html.parser')

    
    ## json에 저장
    #instiz
    for title in soup_instiz.select('#subject a'): 
                    a = title.get('href')
                    b=a.replace(".." , "instiz.net")
                    data[0][title.text] = b
    #clien
    n=0
    for title in soup_clien.select('.list-title .list-subject'): 
        if n == 0:
            n+=1
            continue
        else:
            a = title.get('href')
            if not a==None:
                    a='clien.net' + a
                    str=" ".join(title.text.strip().split())
                    data[1][str] = a
    #fmkorea
    for title in soup_fmkorea.select('.hx'): 
                    a = title.get('href')
                    data[2][title.text.strip()] = a
    #ou
    for title in soup_ou.select('.subject a'): 
                    a = title.get('href')
                    a='todayhumor.co.kr' + a
                    data[3][title.text] = a
    #pan
    for title in soup_pan.select('dt a'): 
                    a = title.get('href')
                    data[4][title.text] = a
    #slr
    for title in soup_slr.select('.sbj a'): 
                    a = title.get('href')
                    a='slrclub.com'+a
                    data[5][title.text] = a
    #mlb
    for title in soup_mlb.select('.t_left a'): 
                    a = title.get('href')
                    data[6][title.text] = a
    #inben
    for title in soup_inben.select('a.sj_ln'): 
                    a = title.get('href')
                    data[7][title.text] = a
    #ruri
    for title in soup_ruri.select('.subject a'): 
                    a = title.get('href')
                    data[8][title.text] = a
     #utde
    for title in soup_utde.select('a.brn3, a.brn2, a.brn1'): 
                    a = title.get('href')
                    a='web.humoruniv.com/board/humor/'+a
                    str=" ".join(title.text.strip().split())
                    data[9][str] = a
    #bobe
    for title in soup_bobe.select('a.bsubject'): 
                    a = title.get('href')
                    a='bobaedream.co.kr'+a
                    data[10][title.text] = a
    #ygosu
    for title in soup_ygosu.select('.tit a'): 
                    a = title.get('href')
                    data[11][title.text] = a
     #drip
    n=0
    for title in soup_drip.select('td.title a'): 
                if n == 0:
                      n+=1
                      continue
                else:
                     a = title.get('href')
                     data[12][title.text.strip()] = a
    #theqoo
    j=0 
    n=1
    x=1
    m=2
    for title in soup_theqoo.select('td.title a'): 
            if j < 8 :
                     j+=1
                     continue
            else:
                    if  n == m:
                            a=title.get('href')
                            a='theqoo.net'+a.replace('_comment','') 
                            n+=1
                            x+=1
                            m=2*x
                            data[13][title.text] = a
                            continue
                    else:
                            n+=1
                            continue
    #dogge
    for title in soup_dogge.select('.txt a'): 
                    a = title.get('href')
                    a ='http://dkbnews.donga.com/Board'+a
                    data[14][title.text.strip()] = a
    #namsung
    n=0
    for title in soup_namsung1.select('.list-subject a'): 
                    if n < 10:
                        a = title.get('href')
                        n+=1
                        data[15][title.text.strip()]=a
                    else:
                          break                   
    for title in soup_namsung2.select('.list-subject a'): 
                     if n < 19:
                        a = title.get('href')
                        n+=1
                        data[15][title.text.strip()]=a
                     else:
                          break
    #flash1
    n=0
    for title in soup_flash1.select('.subject a'): 
                    if n == 0:
                        n+=1
                        continue
                    else:
                        a = title.get('href')
                        a = a.replace('..','flash24.dreamx.com/g4')
                        data[16][title.text]=a
     #flash2
    n=0
    for title in soup_flash2.select('.subject a'): 
                    if n == 0:
                        n+=1
                        continue
                    else:
                        a = title.get('href')
                        a = a.replace('..','flash24.dreamx.com/g4')
                        data[17][title.text]=a
    #dream1
    n=1
    x=1
    m=2
    for title in soup_dream1.select('.bbs_list_list a'): 
                        if  n == m:
                                a=title.get('href')
                                a='newsbbs.dreamx.com'+a
                                n+=1
                                x+=1
                                m=2*x
                                data[18][title.text.strip()]=a
                                continue
                        else:
                                n+=1
                                continue
    #dream2
    n=1
    x=1
    m=2
    for title in soup_dream2.select('.bbs_list_list a'): 
                        if  n == m:
                                a=title.get('href')
                                a='newsbbs.dreamx.com'+a
                                n+=1
                                x+=1
                                m=2*x
                                data[19][title.text.strip()]=a
                                continue
                        else:
                                n+=1
                                continue
    #bobe2
    for title in soup_bobe2.select('.pl14 a.bsubject'): 
                    a=title.get('href')
                    a='bobaedream.co.kr'+a
                    data[20][title.text.strip()]=a
    #fomos1
    n=0
    for title in soup_fomos1.select('.ranking a'): 
                        if n < 10:
                                n+=1
                                a=title.get('href')
                                a='www.fomos.kr'+a
                                data[21][title.text.strip()]=a
                        else:
                                break
    n=0
    for title in soup_fomos2.select('.ranking a'): 
                        if n < 10:
                                n+=1
                                a=title.get('href')
                                a='www.fomos.kr'+a
                                data[21][title.text.strip()]=a
                        else:
                                break
    #fomos2
    n=0
    for title in soup_fomos3.select('.ranking a'): 
                        if n < 10:
                                n+=1
                                a=title.get('href')
                                a='www.fomos.kr'+a
                                data[22][title.text.strip()]=a
                        else:
                                break
    n=0
    for title in soup_fomos4.select('.ranking a'): 
                        if n < 10:
                                n+=1
                                a=title.get('href')
                                a='www.fomos.kr'+a
                                data[22][title.text.strip()]=a
                        else:
                                break
     #ilbe
    n=0
    for title in soup_ilbe.select('.title a'): 
                    if n == 0:
                            n+=1
                            continue
                    else:
                            a=title.get('href')
                            data[23][title.text.strip()]=a


     #한꺼번에 DB 에  insert 하기 위한 함수
    
    def allsave(x):
            crawling = CrawlingData()
            list = [
                       [crawling.instiz, crawling.link_instiz], [crawling.clien, crawling.link_clien], [crawling.fmkorea, crawling.link_fmkorea],
                       [crawling.ou, crawling.link_ou] ,[crawling.pan, crawling.link_pan],[crawling.slr, crawling.link_slr],[crawling.mlb, crawling.link_mlb],
                       [crawling.inben, crawling.link_inben],[crawling.ruri, crawling.link_ruri],[crawling.utde, crawling.link_utde],[crawling.bobe, crawling.link_bobe],
                       [crawling.ygosu, crawling.link_ygosu],[crawling.drip, crawling.link_drip],[crawling.theqoo, crawling.link_theqoo],
                       [crawling.dogge, crawling.link_dogge],[crawling.namsung, crawling.link_namsung],[crawling.flash1, crawling.link_flash1],
                       [crawling.flash2, crawling.link_flash2],[crawling.dream1, crawling.link_dream1],[crawling.dream2, crawling.link_dream2],
                       [crawling.bobe2, crawling.link_bobe2],[crawling.fomos1, crawling.link_fomos1], [crawling.fomos2, crawling.link_fomos2],
                       [crawling.ilbe, crawling.link_ilbe]
                   ]
            for  i in range(len(data)):
                    n=0
                    for t,l in data[i].items():
                        if n == x:
                            list[i][0],list[i][1]= t,l
                            break
                        else:
                            n+=1
                            continue
            
            CrawlingData(instiz=list[0][0],link_instiz=list[0][1], clien=list[1][0],link_clien=list[1][1], fmkorea=list[2][0],link_fmkorea=list[2][1],
                                  ou=list[3][0],link_ou=list[3][1], pan=list[4][0],link_pan=list[4][1], slr=list[5][0],link_slr=list[5][1], mlb=list[6][0],link_mlb=list[6][1],
                                  inben=list[7][0],link_inben=list[7][1], ruri=list[8][0],link_ruri=list[8][1], utde=list[9][0],link_utde=list[9][1],
                                  bobe=list[10][0],link_bobe=list[10][1], ygosu=list[11][0],link_ygosu=list[11][1], drip=list[12][0],link_drip=list[12][1],
                                  theqoo=list[13][0],link_theqoo=list[13][1], dogge=list[14][0],link_dogge=list[14][1], namsung=list[15][0],link_namsung=list[15][1],
                                  flash1=list[16][0],link_flash1=list[16][1], flash2=list[17][0],link_flash2=list[17][1], dream1=list[18][0],link_dream1=list[18][1],
                                  dream2=list[19][0],link_dream2=list[19][1], bobe2=list[20][0],link_bobe2=list[20][1], fomos1=list[21][0],link_fomos1=list[21][1],
                                  fomos2=list[22][0],link_fomos2=list[22][1], ilbe=list[23][0],link_ilbe=list[23][1],
                                    ).save() 
            
       ##DB에 저장
    for x in range(len(data[0])):
                    allsave(x)
                    
                    
    
while True:
    print('start parsing')
    delete()
    parse()
    print('parsing ends')
    print('sleep in 1 hour')
    time.sleep(3600) 