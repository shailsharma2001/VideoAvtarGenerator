# news_api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('NEWS_API_KEY')

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self, query, num_news):
        url = f'https://newsapi.org/v2/everything?q={query}&from=2023-12-31&sortBy=popularity&pageSize={num_news}&language=en&apiKey={self.api_key}'
        #url = f'https://newsapi.org/v2/everything?q={query}&from=2023-12-31&sortBy=popularity&pageSize={num_news}&language=en&apiKey=f6e0fc9caa194e6f9f162fbd949d8628'
        #url= f'https://newsapi.org/v2/everything?q=apple&from=2024-01-03&to=2024-01-03&sortBy=popularity&apiKey={self.api_key}'
        #url= 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f6e0fc9caa194e6f9f162fbd949d8628'

        print('news URL='+url)
        
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            print(news_data)
            return news_data.get("articles", [])
        else:
            print("No news data:")
            return []

    def get_news_descriptions(self, query, num_news):
        news = self.get_news(query, num_news)
        desc_list = [news_item['description'] for news_item in news]
        return desc_list

    def get_news_string(self, query, num_news):
        desc_list = self.get_news_descriptions(query, num_news)
        desc_string = ". ".join(desc_list)
        return desc_string
