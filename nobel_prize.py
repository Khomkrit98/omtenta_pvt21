# import sys
import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här:
# https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Fält: fysik, kemi, litteratur, ekonomi, fred, medicin.
Ange Q för att avsluta programmet
Ange H för att  skriva ut Hjälp texten
"""

fields = {"fysik": "phy",
          "kemi": "che",
          "litteratur": "lit",
          "ekonomi": "eco",
          "fred": "pea",
          "medicin": "med"}


# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input TODO
#  15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med
#  till apiet och vi får då alla priser det året


def main():
    print(HELP_STRING)
    while True:
        # TODO 5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        user_input = input(">")
        if user_input.upper() == "Q":
            break
        if user_input.upper() == "H":
            print(HELP_STRING)
        years, field = user_input.split()
        category = fields[field]

        category = {"nobelPrizeYear": int(years), "nobelPrizeCategory": category}

        data_from_api = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=category).json()
        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------
        print_prize(data_from_api)
        # TODO 15p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde


def print_prize(res):
    for prize in res["nobelPrizes"]:
        prize_amount = prize["prizeAmount"]
        # idagpeng = prize["prizeAmountAdjusted"]
        print(f"{prize['categoryFullName']['se']} prissumma {prize_amount} SEK")

        for recipient in prize["laureates"]:
            print(recipient['knownName']['en'])
            print(recipient['motivation']['en'])
            # andel = recipient['portion']


if __name__ == '__main__':
    main()
