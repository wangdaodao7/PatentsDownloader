import requests
from bs4 import BeautifulSoup
import lxml
from config import *


base_url = 'http://g.wanfangdata.com.cn/search/searchList.do?searchType=patent&pageSize=50&page={page_nums}&searchWord={patants_keywords}&order=correlation&showType=detail&isCheck=check&isHit=&isHitUnit=&firstAuthor=false&rangeParame=all'

#获取专利号,传入的参数为关键词， 页码数
def get_id(patant_keywords, page_nums):
    response = requests.get(base_url.format(
        patants_keywords=KEY_WORDS, page_nums=1))
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.select('.share_summary')
    patants_id = list(set([i.get('onclick').split('=')[2].split("'")[
                      0] for i in soup.select('.stitle')]))
    return patants_id
