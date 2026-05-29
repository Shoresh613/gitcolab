# Git-samarbete: Quiz-app

Det här är ett litet övningsprojekt för att träna på att jobba flera personer i samma kodbas med Git och GitHub.

Ni ska bygga vidare på en enkel quiz-app i Python. Målet är inte att skapa ett perfekt program, utan att öva på ett realistiskt arbetsflöde.

Det finns två sätt att göra övningen:

- Rekommenderat flöde: använd GitHub Issues och Pull Requests, där GitHub hjälper dig skapa branchen.
- Manuellt flöde: skapa branchen själv i terminalen med Git-kommandon.

I båda fallen tränar ni på samma grundide:

1. Välj eller skapa en issue
2. Skapa en egen branch
3. Gör en liten ändring
4. Commita och pusha
5. Skapa en pull request
6. Få feedback
7. Merga in ändringen i `main`
8. Hämta senaste versionen av `main`

## Projektide

Quiz-appen ska kunna ställa frågor, ta emot svar och räkna poäng. Frågorna kan handla om till exempel Python, AI, databaser och Git.

En möjlig första version kan bestå av några enkla filer:

```text
gitcolab/
  README.md
  quiz.py
  questions.py
  scoring.py
```

Exempel:

- `quiz.py` kör själva programmet
- `questions.py` innehåller quizfrågor
- `scoring.py` innehåller funktioner för poäng eller resultat


### 1. Hämta projektet

Klona repot:

```bash
git clone https://github.com/Shoresh613/gitcolab.git
cd gitcolab
```

Om du redan har klonat projektet, börja med att hämta senaste versionen:

```bash
git checkout main
git pull
```

## Rekommenderat flöde: GitHub Issues och Pull Requests

Det här är det enklaste flödet under lektionen och det vi använder i första hand. GitHub hjälper dig att skapa en branch kopplad till en issue, så att du slipper skriva alla Git-kommandon själv.

### 1. Välj en issue

Gå till extension GitHub Pull Requests och välj en issue att jobba med. Det kallas ibland att claima en issue.

Om du istället gör det manuellt, skriv då gärna en kommentar i issuen, till exempel:

```text
Jag tar denna.
```

Välj en liten uppgift. Hellre en liten färdig ändring än en stor halvfärdig.

### 2. Skapa branch från issuen

God sed att göra en git pull i main innan man skapar en ny branch för att alltid utgå från den senaste koden. 

I listan över issues finns en högerpil bredvid varje issue.

Klicka på pilen bredvid den issue du vill jobba med (öppna först issuen för att kolla om någon annan redan börjat, ta i så fall en annan issue, eller skapa en ny) och låt GitHub skapa en branch åt dig.

GitHub skapar då branchen, säger automatiskt att du claimat issuen, och byter automatiskt till den nyskapade branchen. 

### 3. Gör ändringen

Ändra koden. Testa sedan programmet:

```bash
python quiz.py
```

Om projektet använder `python3` på din dator:

```bash
python3 quiz.py
```

### 4. Commita och pusha

Med hjälp av source control i VS Code ser du automatiskt vilka filer som ändrats, och kan skriva in vilka ändringar du gjort, eller låta Copilot skriva commit-message åt dig. 

### 5. Skapa pull request

När man skickar upp sin ändring får man direkt en liten popup nere till höger i VS Code-fönstret med frågan om man vill skapa en Pull Request. Svara ja på det om du känner att du är färdig att lämna ifrån dig den kod du gjort.

Klicka på den, skriv kort vad du har gjort och skapa PR:en.

Hinner man inte klicka kan man skapa en pull request genom att klicka sig fram.

Exempel på PR-text:

```text
Lägger till fem nya frågor om Python.

Closes #3
```

`Closes #3` betyder att issue nummer 3 stängs automatiskt när PR:en mergas.

### 6. Låt någon gå igenom den innan merge

Någon i teamet kan gå igenom pull requests för att se om koden verkar bra, innan de mergas in i main.

### 7. Efter merge

När din PR är mergad, gå tillbaka till `main` och hämta senaste versionen:

```bash
git checkout main
git pull
```

Sedan kan du välja en ny issue och skapa en ny branch.

### Om GitHub säger att det finns en konflikt

Ibland har två personer ändrat samma del av samma fil. Då kan GitHub säga att din pull request har en merge conflict.

Det betyder inte att något är förstört. Det betyder bara att Git inte vet vilken version som ska gälla. Man kan då använda VS Code inbyggda merge conflict resolver, eller kolla på Github (mer robust).

## Manuellt flöde: skapa branch själv

Det här flödet gör samma sak som det automatiska ovan, men du skapar branchen själv i terminalen. Rekommenderas inte.

### 1. Välj en issue

Gå till GitHub och välj en issue att jobba med. Skriv gärna en kommentar i issuen, till exempel:

```text
Jag tar denna.
```

Välj en liten uppgift. Hellre en liten färdig ändring än en stor halvfärdig.

### 2. Skapa en branch

Skapa en branch med ett tydligt namn:

```bash
git checkout -b add-python-questions
```

Exempel på branchnamn:

- `add-ai-questions`
- `fix-score-calculation`
- `improve-readme`
- `randomize-questions`

### 3. Gör ändringen

Ändra koden. Testa sedan programmet:

```bash
python quiz.py
```

Om projektet använder `python3` på din dator:

```bash
python3 quiz.py
```

### 4. Commita

Kolla vilka filer du har ändrat:

```bash
git status
```

Lägg till filerna:

```bash
git add .
```

Skapa en commit:

```bash
git commit -m "Add Python quiz questions"
```

En bra commit-message säger kort vad ändringen gör.

### 5. Pusha

Skicka upp din branch till GitHub:

```bash
git push -u origin add-python-questions
```

Byt ut `add-python-questions` mot namnet på din branch.

### 6. Skapa en pull request

På GitHub:

1. Öppna din branch
2. Klicka på "Compare & pull request"
3. Skriv kort vad du har gjort
4. Koppla gärna PR:en till ditt issue
5. Skapa pull request

Exempel på PR-text:

```text
Lägger till fem nya frågor om Python.

Closes #3
```

### 7. Efter merge

När din PR är mergad, gå tillbaka till `main` och hämta senaste versionen:

```bash
git checkout main
git pull
```

Sedan kan du välja ett nytt issue och skapa en ny branch.

## Förslag på issues

Några lagom stora uppgifter för övningen.

### Enkla issues

- Lägg till 5 frågor om Python
- Lägg till 5 frågor om AI
- Lägg till 5 frågor om databaser
- Lägg till 5 frågor om Git
- Förbättra texten som visas när quizet startar
- Förbättra texten som visas när quizet är slut
- Rätta stavfel i frågor eller instruktioner

### Mellansvåra issues

- Slumpa ordningen på frågorna
- Räkna och visa poäng
- Visa rätt svar efter varje fråga
- Visa procent rätt i slutet
- Lägg till nivåer: lätt, medel, svår

### Extra issues om tid finns

- Spara high score i en fil
- Läs frågor från en JSON-fil
- Lägg till kategori-val innan quizet startar
- Lägg till enkla tester
- Gör en meny där användaren kan välja vad den vill göra

## Exempel på enkel startkod

Om projektet startar från noll kan läraren lägga in detta i `quiz.py`:

```python
questions = [
    {
        "question": "Vad skriver man för att skriva ut text i Python?",
        "answer": "print"
    },
    {
        "question": "Vilket kommando används för att se ändrade filer i Git?",
        "answer": "git status"
    }
]

score = 0

for item in questions:
    user_answer = input(item["question"] + " ")

    if user_answer.lower().strip() == item["answer"].lower().strip():
        print("Rätt!")
        score += 1
    else:
        print("Fel. Rätt svar är:", item["answer"])

print("Du fick", score, "av", len(questions), "poäng.")
```

Kör programmet med:

```bash
python quiz.py
```

### Om det blir merge conflict

Det är inte ett misslyckande. Det är en bra erfarenhet.

En enkel förklaring:

```text
Git kunde inte automatiskt kombinera två ändringar i samma del av samma fil.
Vi behöver välja hur slutversionen ska se ut.
```

Kör bara:

```bash
git status
```

Öppna filen, leta efter konfliktmarkeringar:

```text
<<<<<<< HEAD
...
=======
...
>>>>>>> branch-name
```

Redigera filen så att den ser rätt ut, och commita sedan lösningen.

## Bra regler under övningen

- Jobba alltid i en egen branch
- Gör små ändringar
- Testa innan du pushar
- Skriv tydliga commit-meddelanden
- Skapa PR även för små ändringar
- Läs diffen innan du ber om review
- Uppdatera `main` efter att din PR har mergats

## Målet med övningen

Efter övningen ska du ha testat hela kedjan från issue till merge. Du behöver inte kunna alla Git-kommandon utantill, men du ska förstå varför man använder branches och pull requests när flera jobbar i samma projekt.
