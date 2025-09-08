"""
Web scraping of football matches of diferent leages with Pandas
"""
import pandas as pd
#reads csv data from the link on website
df_premier25 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2526/E0.csv')
df_premier25.rename(columns={'AvgCAHH':'average_hourly_household', 'AvgCAHA':'average_hourly_audience'}, inplace=True)

"""
Web scraping. Predicting World Cup Winner
"""
from bs4 import BeautifulSoup
import requests
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
        1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
        2018]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate, br, zstd","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Language": "en-US;q=0.6,en;q=0.5"}

def get_matches(year):
    URL = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(URL,headers=headers)
    soup = BeautifulSoup(response.content, "lxml")



    #the list of matches
    matches = soup.find_all('div',class_='footballbox')
    # for match in matches:
    #     print(match.find('th',class_='fhome').get_text())
    #     print(match.find('th',class_='fscore').get_text())
    #     print(match.find('th',class_='faway').get_text())
        
    columns = ["Country","Score","Guests"]
    data = []
    for match in matches:
        home = match.find('th',class_='fhome').get_text()
        score =match.find('th',class_='fscore').get_text()
        away = match.find('th',class_='faway').get_text()
        data.append([home,score,away])
    df_football = pd.DataFrame(data = data  ,columns=columns)
    df_football['Year'] = year
    return df_football

def main():
    fifa = [get_matches(year) for year in years]
    df_concat_fifa = pd.concat(fifa,ignore_index=True)
    #index=False wont export indexes to csv
    df_concat_fifa.to_csv('fifa_data.csv', index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    main()