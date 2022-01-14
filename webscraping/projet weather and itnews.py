import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EA%B4%91%EC%A3%BC%EB%82%A0%EC%94%A8&tqi=hO0VpsprvTVssUcTdRRssssst2R-470926"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도","") 
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text() 
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text() 
    rain_rate = soup.find("dd", attrs={"class":"desc"}).get_text() 

    rest = soup.find("li", attrs={"class":"item_today level2"}).get_text().strip()
   
    print()
    print(cast)
    print("현재{} ( {} / {})".format(curr_temp, min_temp, max_temp))
    print("현재 강수확률 {}".format(rain_rate))
    print()
    print("{}".format(rest))
    print()
  
def scrape_it_news():
    print("[IT 뉴스]")
    print()
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find_all("a")[1].get_text().strip()
        link = news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()


if __name__ == "__main__":
    scrape_weather() #오늘의 날씨정보 가져오기
    scrape_it_news() #실시간 IT뉴스정보 가져오기

