# import sys
# from dataclasses import field

# import pprint

from Iterations.tentamen_2021.omtenta_pvt21.nobel_prize_api import get_prize_data

HELP_STRING = """
Ange ett år och fält.
Exempelvis: 1965 fysik.
Fält: fysik, kemi, litteratur, ekonomi, fred, medicin.
Ange Q för att avsluta programmet.
Ange H för att skriva ut hjälp texten igen.
"""

feild = {"fysik": "phy",
         "kemi": "che",
         "litteratur": "lit",
         "ekonomi": "eco",
         "fred": "pea",
         "medicin": "med"}


def get_user_input() -> list:
    return input(">").split()


def main():
    print(HELP_STRING)
    while True:
        user_input = get_user_input()
        if 'q' in user_input:
            break

        years = user_input[0]
        if len(user_input) == 1:
            years = user_input[0]
            category = {"nobelPrizeYear": int(years)}
        else:
            field = user_input[1]
            category = feild[field]
            category = {"nobelPrizeYear": int(years), "nobelPrizeCategory": category}

        data_from_api = get_prize_data(category)
        # pprint.pprint(data_from_api)
        print_prize(data_from_api)
        # TODO 15p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera
        #  mottagare, skriv ut både i dåtidens pengar och dagens värde Skriv ut med tre decimalers precision. exempel
        #  534515.123 Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i
        #  dåtidens penningvärde


def print_prize(res):
    for prize in res["nobelPrizes"]:
        prize_amount = prize["prizeAmount"]
        # idagpeng = prize["prizeAmountAdjusted"]
        print(f"{prize['categoryFullName']['se']} prissumma {prize_amount} SEK")

        for recipient in prize["laureates"]:
            print(recipient['knownName']['en'])
            print(recipient['motivation']['en'])
            print("-" * 130)
            # andel = recipient['portion']
            print("\n")


if __name__ == '__main__':
    main()
