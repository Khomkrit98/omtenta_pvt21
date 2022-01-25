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


def print_prize(res):
    for prize in res["nobelPrizes"]:
        prize_amount = prize["prizeAmount"]
        prize_amount_adjusted = prize["prizeAmountAdjusted"]
        print(
            f"{prize['categoryFullName']['se']} "
            f"prissumma {prize_amount} SEK justerad för inflation {prize_amount_adjusted}")

        for recipient in prize["laureates"]:
            portion = 1 / len(prize['laureates'])
            print(recipient['knownName']['en'])
            print(recipient['motivation']['en'])
            print(f"{prize_amount * portion:.3f} justerat för inflation {prize_amount_adjusted * portion:.3f}")
            print("-" * 130)
            # andel = recipient['portion']
            print("\n")


if __name__ == '__main__':
    main()
