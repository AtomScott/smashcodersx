import requests
import pandas as pd

from bs4 import BeautifulSoup as bs

class User():
    def __init__(self, user_id):
        res = requests.get(f"https://atcoder.jp/users/{user_id}/history/json")

        self.user_id = user_id
        self.data = pd.DataFrame(res.json())
        self.rating = self.data.NewRating.iloc[-1]
        self.color = [
            'Grey',
            'Brown'
            'Green',
            'Sky',
            'Blue',
            'Yellow',
            'Orange',
            'Red'
        ][self.rating // 400] if self.rating < 3200 else 'Red'
        
        self.emoji = [
            ':rice:',
            ':chestnut:',
            ':broccoli:',
            ':cup_with_straw:',
            ':candy:',
            ':lemon:',
            ':tangerine:',
            ':tomato:'
        ][self.rating // 400] if self.rating < 3200 else 'Red'

    @property
    def info(self):
        msg = f'{self.emoji} User: {self.user_id}, rating: {self.rating}'
        return msg

if __name__ == '__main__':
    print(get_user_rating('ajs'))