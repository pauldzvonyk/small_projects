# api key: f0c72477f947461a8ca2500ea41ee7df
import requests


class NewsFeed:
    """Representing multiple news titles and relative urls as string
    """
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = 'f0c72477f947461a8ca2500ea41ee7df'

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''

        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'
        return email_body


if __name__ == "__main__":
    news = NewsFeed(interest='chess', from_date='2023/12/14', to_date='2023/12/17')
    print(news.get())




