import requests


def get_prize_data(category):
    return requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=category).json()
