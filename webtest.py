import requests
from bs4 import BeautifulSoup

# URL der Website mit den Fragen und Antworten
url = "https://www.oeamtc.at/fuehrerschein/oeamtc/index.php"

# HTML-Seite abrufen
response = requests.get(url)
html_content = response.text

# BeautifulSoup verwenden, um den HTML-Code zu analysieren
soup = BeautifulSoup(html_content, 'html.parser')

# Hier die Logik implementieren, um die richtige Antwort(en) zu finden
# Annahme: Die richtige Antwort ist in einem bestimmten HTML-Element oder Attribut

# Beispiel:
right_answer = soup.find('span', {'class': 'right-answer'})

# Hier die ausgewählten Antworten aus dem Seitenquelltext extrahieren
# Annahme: Die ausgewählten Antworten sind in Checkboxen mit einer bestimmten Klasse

# Beispiel:

# Hier die Logik implementieren, um die ausgewählten Antworten mit der richtigen Antwort zu vergleichen
# Beispiel:
print(soup.prettify())
print(right_answer)

# Hier kannst du dann die Seite mit den markierten Antworten zurückgeben oder anderweitig anzeigen
# Beispiel:

