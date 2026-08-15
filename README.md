# Kvartalsmötet

Detta är projektarkivet för romanen **Kvartalsmötet – Protokollet var redan skrivet** av **Erland Lindmark**.

## Rekommenderat arbetsflöde

1. Planera romankärnan: huvudperson, mål, hinder, insats och förändring.
2. Skapa synopsis, kapitelplan, romanbibel och stilguide.
3. Skriv ett kapitel i taget.
4. Justera kapitlet tills det är godkänt.
5. Uppdatera projektfilerna och projektstatus.
6. Fortsätt med nästa kapitel eller revision.

## Viktiga filer

- `projektstatus.md` visar nuvarande fas, senaste skrivna kapitel och nästa rekommenderade steg.
- `roman-bibel.md` innehåller projektets centrala fakta.
- `synopsis.md` sammanfattar hela handlingen.
- `kapitelplan.md` är färdplanen för romanen.
- `stilguide.md` håller språk, ton och perspektiv konsekvent.
- `tidslinje.md` håller ordning på händelser.
- `kontinuitetsanteckningar.md` fångar fakta som inte får motsägas.
- `revisionsonskemal.md` samlar planerade förbättringar.
- `arbetslogg.md` visar vad som har gjorts.
- `kapitel/` innehåller kapitelutkast och godkända kapitel.

## Omslagsstatus

Omslagsbild/framsida är önskad men ännu inte skapad.

## Omslag

Aktuell omslagsbild finns i `omslag/omslag-kvartalsmotet.png`.


## Aktuell status

- Version: Slutputsad och konsekvenskontrollerad version 5
- Datum: 2026-05-21
- Kapitel: 1–18 finns som utkast
- Omslagsbild: `omslag/omslag-kvartalsmotet.png`
- Nästa steg: helhetsläsning/godkännande eller export till PDF/EPUB

## Aktuell status efter spänningsrevision v2

Kapitel 1–18 är skrivna som utkast och genomgångna i strukturell revision samt spänningsrevision. Nästa rekommenderade steg är språk- och röstrevision innan export till PDF/EPUB.


## Aktuell version

Språk- och röstreviderad version 3 skapad 2026-05-21. Kapitel 1–18 finns som reviderade utkast. Omslagsbild finns i `omslag/omslag-kvartalsmotet.png`.


## Senaste projektläge 2026-05-21

Projektet är uppdaterat till karaktärs- och relationsreviderad version 4. Revisionen fördjupar Karin/Tomas-relationen, Miras ansvarsbåge och Lars namngivna ansvarstagande.

## GitHub Actions-publicering

Projektet innehåller nu ett anpassat CI-/publiceringsupplägg:

- `.github/workflows/01-validate.yml` validerar projektstruktur, kapitel, metadata och omslag.
- `.github/workflows/02-build-preview.yml` bygger EPUB och PDF manuellt som ett gemensamt preview-artifact.
- `.github/workflows/03-release.yml` bygger EPUB och PDF vid taggar enligt `v*` och publicerar dem som GitHub Release-assets.
- `scripts/build_book.py` bygger EPUB/PDF från `kapitel/kapitel-XX.md` i numerisk ordning.
- `publishing/metadata.yaml` innehåller exportmetadata för titel, undertitel, författare, språk och omslag.
