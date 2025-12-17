# 日本語の練習 - Japansk Øvingsapp

En interaktiv webapp for å øve japanske setninger, bygget med Astro og TypeScript.

## 🚀 Prosjektstruktur

```
/
├── src/
│   ├── data/           # JSON-filer med kategoriserte setninger
│   │   ├── tog.json
│   │   ├── meg-selv.json
│   │   ├── daglige-rutiner.json
│   │   └── mat.json
│   └── pages/
│       └── index.astro # Hovedside
├── public/
└── package.json
```

## 📚 Kategorier

Hver kategori inneholder 10 setninger med:

- **Furigana** (lesehjelp over kanji)
- **Romaji** (latinsk transkripsjon)
- **Interaktive tooltips** med forklaringer
- **Smart svar-sjekk** med Levenshtein-avstand

### Tilgjengelige kategorier:

- 🚆 **Tog** (電車) - 10 setninger om tog og transport
- 👤 **Meg selv** (自己紹介) - 10 setninger for å presentere deg selv
- ⏰ **Daglige rutiner** (日常) - 10 setninger om daglige aktiviteter
- 🍜 **Mat** (食べ物) - 10 setninger om mat og drikke

## 🎯 Funksjoner

- **Klikk og lukk kategorier** for fokusert læring
- **Progress bar** viser fremgang
- **Smart svar-sjekk** som aksepterer synonymer og små feil
- **Visuell feedback**: Grønt (riktig), gult (nesten riktig), rødt (feil)
- **Hover-tooltips** med grammatikkforklaringer
- **Verb-bøyninger** vises i tooltips

## 🛠️ Kommandoer

```bash
# Installere avhengigheter
npm install

# Starte dev-server
npm run dev

# Bygge for produksjon
npm run build

# Forhåndsvise produksjonsbygg
npm run preview
```

## 📝 Legge til nye kategorier

1. Opprett en ny JSON-fil i `src/data/`:

```json
{
  "category": "kategori-navn",
  "categoryName": "Norsk navn",
  "categoryNameJapanese": "日本語",
  "emoji": "🎌",
  "sentences": [
    {
      "id": 1,
      "words": [
        {
          "furigana": "ひらがな",
          "kanji": "漢字",
          "romaji": "romaji",
          "tooltip": "Forklaring på norsk",
          "isParticle": false
        }
      ],
      "answers": ["mulig svar 1", "mulig svar 2"]
    }
  ]
}
```

2. Importer filen i `src/pages/index.astro`:

```typescript
import nyKategori from "../data/ny-kategori.json";
const categories = [togData, megSelvData, nyKategori];
```

## 🎨 Tilpasning

- **CSS** er inline i `index.astro` for enkel tilpasning
- **Svar-sjekk terskler** kan justeres i JavaScript-koden:
  - `>= 0.9` = Riktig (grønt)
  - `>= 0.7` = Nesten riktig (gult)
  - `< 0.7` = Feil (rødt)

## 📖 Læringsmetode

1. Les den japanske setningen
2. Hold over ord for å se forklaringer
3. Skriv oversettelsen på norsk
4. Trykk Enter for å sjekke svaret
5. Få umiddelbar feedback med forslag

## 🌟 Tips

- Bruk tooltips for å lære grammatikk underveis
- Partikler (は, を, に, etc.) er markert i grønt
- Verb viser både høflig og uformell form
- Progress baren motiverer til å fullføre alle setninger

## 📂 Flytte den gamle HTML-filen

Den gamle `japanese-trains.html` filen kan nå slettes eller flyttes til en annen mappe siden alt er migrert til dette Astro-prosjektet.

---

頑張って！(Ganbatte - Lykke til!)
