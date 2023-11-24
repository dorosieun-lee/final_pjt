from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re as ree
from selenium import webdriver
import json
from django.http import JsonResponse 

# Create your views here.
def mainpage_info(request):
    # https://m.stock.naver.com/investment/news/mainnews 여기서 경제 뉴스 기사 제목, 링크, 이미지, 신문사, 날짜 최신 10개 가져오기
    url = "https://m.stock.naver.com/investment/news/mainnews"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    pattern = ree.compile(r'^NewsList_item_')
    data = soup.find_all(class_ = pattern)
    news_data = []
    for item in data[:10]:
        link = item.find('a').get('href')
        title = item.find('strong').text
        content = item.find('p').text
        img_link = item.find('img').get('src')
        time = item.find('time').text
        cite = item.find('cite').text
        news_data.append({'link': link,
                        'img_link': img_link,
                        'title': title,
                        'content': content,
                        'time': time,
                        'cite': cite})

    # https://m.stock.naver.com/marketindex/home/major/exchange/bond 여기서 미국 USD, 국제 금, WTI 정보 가져오기
    url = "https://m.stock.naver.com/marketindex/home/major/exchange/bond"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    pattern = ree.compile(r'^MainListItem_link')
    data = soup.find_all(class_ = pattern)
    index_data = []
    for item in data:
        name = item.find('strong').text
        pattern = ree.compile(r'^MainListItem_price')
        value = item.find(class_ = pattern).text
        pattern = ree.compile(r'^Fluctuation_fluctuation_')
        tmp = item.find_all(class_=pattern)
        fluctuation = {'value': tmp[0].text, 'percent': tmp[1].text[:-1]}
        index_data.append({'name': name,
                            'value': value,
                            'fluctuation': fluctuation})

    final_data = {'news_data': news_data, 'index_data': index_data}
    return JsonResponse(final_data, status=200)


def kospi_info(request):
    # https://m.stock.naver.com/domestic/index/KOSPI/total 여기서 코스피 지수 가져오기 -> 동적 페이지
    max_retries = 3  # 최대 재시도 횟수 설정

    for attempt in range(max_retries):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("headless") # 브라우저 창 뜨지 않게 하는 옵션
            driver = webdriver.Chrome(options=options)

            url = "https://m.stock.naver.com/domestic/index/KOSPI/total"
            driver.get(url)

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            pattern = ree.compile(r'^GraphMain_price_')
            price = soup.find(class_=pattern)

            pattern = ree.compile(r'^VGap_gap_')
            tmp = soup.select('.VGap_gap__i0BuQ')
            fluctuation = {'value': tmp[0].get_text()[0:len(tmp[0].get_text()) // 2], 'percent': tmp[1].get_text()[:-1]}
            index_data = {'name': '코스피', 
                        'value': price.text, 
                        'fluctuation': fluctuation}

            driver.quit()
            break  # 성공하면 반복문 종료
        except IndexError:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed. Retrying...")
                continue
            else:
                print("Max retries reached. Unable to fetch data.")

    return JsonResponse(index_data, status=200)
