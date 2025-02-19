# Äventyr

Vad är det okej att använda AI till i programmeringen?

Exempelvis att skriva en berättlse, skapa ett innehåll. Problemlösningen är ditt jobb. AI kan hjälpa dig att skapa innehållet.

## Prompter

Du är en expert på att skriva äventyr i formatet [choose your own adventure]. Du har en väldigt lång erfarenhet av att skriva engagerande berättelser för [ungdomar] i det här formatet. 
Jag behöver din hjälp med skrivandet. Du kommer att svara i formatet av en python lista med dicts.
Jag klistrar in formatet som du ska svara i. Bekräfta att du förstår.

### Formatet 

Här är formatet för att skriva en berättelse i formatet [choose your own adventure]. 

```
format = [
    {
        "id": 1,
        "title": "String title for page",
        "text": "String text for page",
        "options": [
            {"text": "Option 1 with next page id", "next_id": 2},
            {"text": "Option 2 with next page id", "next_id": 3},
        ],
    },
]
```

## Nu är det dags att skriva en berättelse

Du har förberett AI med förutsättningarna. Vill du styra ännu mer över vad den kommer att skriva så skriv så mycket om förutsättningarna som möjligt. Vad är det för kontext, vilka karaktärer finns det, vilka är de viktigaste händelserna?

# App.py

Det här är delvis en uppgift i att läsa och förstå någon annans kod. Det är en väldigt viktig färdighet att ha som programmerare.

Programmet ni har fått med finns i app.py och historient sparas i en annan fil som importeras till `app.py`.

För att importera historien till app.py används import, det är viktigt att redigera den så att den stämmer med ditt filnamn och variabelnamn.

```python
from <filnamn> import <variabelnamnet> as BOOK
```

I `app.py` så finns det ett antal funktioner som används för att köra äventyret. Funktionerna startas från `main()`.

## input_int

Funktionen används för att användaren ska kunna mata in ett heltal och hanterar det så att programmet inte kraschar om användaren matar in något annat än ett heltal.

```python
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
```

1. `def input_int(prompt):` - Definierar en funktion som heter input_int som tar ett argument `prompt`.
2. `while True:` - Startar en oändlig loop som fortsätter tills ett giltigt heltal har angetts.
3. `try:` - Försöker köra koden inom blocket.
4. `return int(input(prompt))` - Visar prompten för användaren och försöker konvertera användarens inmatning till ett heltal. Om det lyckas, returneras heltalet och funktionen avslutas.
5. `except ValueError:` - Om en `ValueError` uppstår (vilket händer om inmatningen inte kan konverteras till ett heltal), fångas undantaget och följande kod körs:
6. `print("Invalid input. Please enter a number.")` - Skriver ut ett felmeddelande som informerar användaren om att inmatningen var ogiltig och att de ska ange ett nummer.

## get_page

Funktionen används för att hämta ut en specifik sida från den `lista` med `dicts` som representerar boken. För att hitta sidan används parametern `page_id`. Se formatet för boken ovan.

```python
def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None
```

1. `def get_page(book_data, page_id):` - Definierar en funktion som heter `get_page` som tar två argument: `book_data` (en lista med sidor) och `page_id` (ID för den sida som ska hämtas).
2. `for page in book_data:` - Loopar igenom varje sida i `book_data`.
3. `if page["id"] == page_id:` - Kontrollerar om sidans ID matchar det angivna `page_id`.
4. `return page` - Om en matchande sida hittas, returneras den sidan.
5. `return None` - Om ingen matchande sida hittas efter att ha loopat igenom alla sidor, returneras `None`.

## show_page

Funktionen används för att visa en specifik sida från boken. Den tar in en sida som en `dict` och skriver ut dess titel, text och tillgängliga alternativ. Se formatet för boken ovan.

```python
def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")
```

1. `def show_page(page):` - Definierar en funktion som heter `show_page` som tar en sida som argument.
2. `print(page["title"])` - Skriver ut titeln på sidan.
3. `print(page["text"])` - Skriver ut texten på sidan.
4. `for i, option in enumerate(page["options"]):` - Loopar igenom varje alternativ på sidan och använder `enumerate` för att få både index (`i`) och alternativet (`option`).
5. `print(f"{i + 1}. {option['text']}")` - Skriver ut indexet för alternativet (börjar från 1 istället för 0) och texten för alternativet.

## main

Funktionen `main` är huvudfunktionen som körs för att starta äventyret. Den innehåller en loop som fortsätter tills användaren når slutet av boken.

```python
def main():
    current_page_id = 1
    while current_page_id is not None:
      # logik för att hämta och visa sidan
```

# Uppgift

Du ska arbeta med att ta fram en berättelse. Du ska sedan använda den färdiga koden för att visa upp berättelsen. Du ska skapa en ny fil för din berättelse och importera den till `app.py`.

1. Skapa en berättelse i formatet [choose your own adventure](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) med minst 5 sidor.
2. Skapa en ny fil för din berättelse och spara den i formatet som en `lista` med `dicts`.
3. Importera din berättelse till `app.py` genom att använda `import`.
4. Kör programmet och testa din berättelse.

Det är grunden för uppgiften. 

## Utveckling

Här finns en lista med förslag på hur du kan utveckla din berättelse och programmet:

1. Lägga till fler sidor och alternativ i berättelsen.
2. Skapa en huvudmeny för spelaren. Tips: använd en loop för att låta spelaren välja att starta ett nytt spel eller avsluta.
3. Spara en historik över användarens val och låta dem gå tillbaka till tidigare sidor. Tips: använd en lista för att spara historiken, du lägger till spelarens val i listan med append.
    - Skapa en replay-funktion som spelar upp berättelsen från historiken.
4. Lägga till fler funktioner för att förbättra användarupplevelsen, som att spara och ladda spel. 
5. Stridsystem: Lägg till stridssekvenser där spelaren måste välja olika alternativ för att vinna striden.
    - Använd dig av sten, sax, påse för att simulera striden. A slår B, B slår C, C slår A.
    - Fienden kan vara en dict med olika egenskaper.
    - Skapa en funktion för combat som tar in spelarens liv, fiendens dict och sedan promptar stridssekvensen, returnera True om spelaren vinner och False om spelaren förlorar.
6. Lägg till fler val för spelaren, som att välja en karaktär i början som påverkar spelet.
7. Att kunna samla föremål under spelets gång.
    - inventory system, ett inventory(lista) med föremål(dicts) som spelaren kan samla på sig.
    - Faktiskt kunna använda föremålen för att lösa problem.
7. Skapa en poängräknare som ökar eller minskar beroende på spelarens val.
8. Lägg till en tidsbegränsning för att göra val, där spelaren måste välja inom en viss tid eller förlora.