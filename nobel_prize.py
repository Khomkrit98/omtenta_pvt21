# import sys
import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Fält: fysik, kemi, litteratur, ekonomi, fred, medicin.
Ange Q för att avsluta programmet
Ange H för att  skriva ut Hjälp texten
"""

cat = {"fysik": "phy",
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
        thy_command = input(">")
        if thy_command.upper() == "Q":
            break
        if thy_command.upper() == "H":
            print(HELP_STRING)
        a, b = thy_command.split()
        c = cat[b]

        c = {"nobelPrizeYear": int(a), "nobelPrizeCategory": c}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------
        print_prize(res)
        # TODO 15p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde


def print_prize(res):
    for p in res["nobelPrizes"]:
        peng = p["prizeAmount"]
        idagpeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")

        for m in p["laureates"]:
            print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']


if __name__ == '__main__':
    main()
