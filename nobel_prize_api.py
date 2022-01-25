import requests


def get_prize_data(category: dict) -> dict:
    """returns a dictionary containing data about the nobel prize awarded a specific year
    category {'year':1965, 'nobelPrizeCategory':phy"""
    return requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=category).json()
