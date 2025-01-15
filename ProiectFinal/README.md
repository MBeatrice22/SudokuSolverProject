# PROIECT SUDOKU CU INTERFAȚĂ GRAFICĂ

## Descriere
Acest proiect implementează un joc de Sudoku cu o interfață grafică creată folosind biblioteca **Tkinter** din Python. Proiectul permite utilizatorului să rezolve un Sudoku oferind opțiunea de a completa manual celulele și de a obține soluția folosind algoritmul **Backtracking**. De asemenea, există funcționalități de verificare a erorilor și de resetare a jocului.

## Biblioteci folosite
- **Tkinter**: Folosită pentru crearea interfeței grafice. Aceasta permite crearea unui GUI simplu și interactiv.
- **messagebox**: Utilizat pentru a afișa mesaje de alertă sau informații utilizatorului (de exemplu, pentru a semnala erori).

## Funcționalități
1. **Interfață grafică cu 9x9 celule**: Utilizatorul poate introduce cifre între 1 și 9 în celulele Sudoku.
2. **Verificare erori**: Programul va verifica dacă există duplicate pe linii, coloane sau sub-grile 3x3.
3. **Rezolvarea Sudoku-ului**: Utilizatorul poate apăsa un buton pentru a rezolva automat Sudoku-ul folosind algoritmul de backtracking.
4. **Resetare Sudoku**: Există un buton care permite resetarea completă a jocului.

## Instrucțiuni de utilizare
1. **Deschideți aplicația**: Rulează fișierul Python (de exemplu, `sudoku_gui.py`) într-un mediu Python compatibil.
2. **Introducerea datelor**: Completează manual câmpurile golite din grid-ul Sudoku (numai cu valori între 1 și 9).
3. **Rezolvarea Sudoku-ului**: Apasă pe butonul **Rezolvă Sudoku** pentru a obține soluția.
4. **Resetarea jocului**: Apasă pe butonul **Resetează Sudoku** pentru a începe un nou joc.

## Rularea programului

### Pași pentru instalare
1. Asigură-te că ai instalat **Python**. Poți descărca Python de la [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Clonează sau descarcă proiectul pe calculatorul tău.
3. Instalează Tkinter dacă nu este deja instalat (de obicei, Tkinter vine preinstalat cu Python).

### Rularea propriu-zisă
1. Navighează la directorul în care se află fișierul `sudoku_gui.py`.
2. Deschide un terminal sau command prompt.
3. Rulează următoarea comandă:

   ```bash
   python sudoku_gui.py
