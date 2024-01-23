import requests
import json

class IVBData:
    def __init__(self):
        self.stops_data = {}

    def get_stops_data(self):
        # Holen der Haltestellen und Speichern in einer Datei
        response = requests.get("https://smartinfo.ivb.at/api/JSON/STOPS")
        stops = response.json()

        # Speichern der Haltestellen in einer Datei
        with open("stops_data.json", "w") as file:
            json.dump(stops, file)

        # Speichern der relevanten Informationen in einem Dictionary
        self.stops_data = {stop["stop"]["uid"]: stop["stop"]["name"] for stop in stops}

    def search_stop(self, search_term):
        # Eine kleine konsolenbasierte Suche über die Haltestellennamen
        result = {uid: name for uid, name in self.stops_data.items() if search_term.lower() in name.lower()}
        return result

    def get_departure_times(self, stop_name):
        # Abfragen der Abfahrtszeiten für eine Haltestelle
        stop_id = next((uid for uid, name in self.stops_data.items() if name.lower() == stop_name.lower()), None)

        if stop_id:
            url = f"https://smartinfo.ivb.at/api/JSON/PASSAGE?stopID={stop_id}"
            response = requests.get(url)
            departure_times = response.json()

            # Ausgabe der relevanten Informationen
            print(f"\nAbfahrtszeiten für Haltestelle {stop_name}:")
            for passage in departure_times[:3]:
                info = passage["smartinfo"]
                print(f"  Linie {info['pnum']} Richtung {info['direction']}: {info['time']}")
        else:
            print(f"\nHaltestelle {stop_name} nicht gefunden.")

    def run(self):
        self.get_stops_data()

        # Suche nach Haltestellen
        search_term = input("Geben Sie einen Suchbegriff für Haltestellen ein: ")
        search_results = self.search_stop(search_term)

        if search_results:
            print("\nGefundene Haltestellen:")
            for uid, name in search_results.items():
                print(f"  Haltestelle ID: {uid}, Name: {name}")

            # Eingabe für Abfahrtszeiten
            stop_name = input("\nGeben Sie den genauen Haltestellennamen für Abfahrtszeiten ein: ")
            self.get_departure_times(stop_name)
        else:
            print("Keine passenden Haltestellen gefunden.")

# Instanz der Klasse erstellen und die Anwendung ausführen
ivb_app = IVBData()
ivb_app.run()

