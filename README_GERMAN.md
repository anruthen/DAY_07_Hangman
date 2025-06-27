# Tag 7 – Hangman-Projekt 🪢💀

## Beschreibung
In diesem Projekt wird ein klassisches **Hangman-Spiel** in Python umgesetzt. Der Spieler versucht, ein geheimes Wort Buchstabe für Buchstabe zu erraten, mit einer begrenzten Anzahl an Versuchen. Eine visuelle Darstellung (ASCII-Art) zeigt die verbleibenden Leben.

## Funktionen
- Auswahl eines geheimen Wortes aus einer vordefinierten Liste  
- ASCII-Grafiken für jeden Spielstatus  
- Verfolgung der bereits geratenen Buchstaben  
- Dynamische Darstellung von richtigen und leeren Buchstaben  
- Gewinn- und Verlustbedingungen

## Beispielausgabe
```
Welcome to
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Guess a letter: 
a

  +---+
  |   |
  O   |
      |
      |
      |
=========

_________
The letter a was not in the word.
You have 5/6 lives left.
```

## Gelernt
- Importieren und Verwenden externer Module (z. B. `hangman_art.py`, `hangman_words.py`)  
- Arbeiten mit Listen (Ersetzen von Platzhaltern durch richtige Buchstaben)  
- Kontrollstrukturen (`if`, `else`, `while`)  
- Schleifen zur Iteration  
- Indizierung und Vergleich  
- ASCII-Formatierung  
- Spiellogik und Zustandsverwaltung
