# Project Index

## Projekt

- Titel: Kvartalsmötet
- Undertitel: Protokollet var redan skrivet
- Författare: Erland Lindmark
- Senast uppdaterad: 2026-08-15
- Nuvarande fas: GitHub Actions-publicering – PDF-fix revision 7
- Senast godkända kapitel: Inget
- Nästa kapitel: Kör preview-workflow på GitHub igen
- Omslagsbild: Skapad (`omslag/omslag-kvartalsmotet.png`)

## Kapitelinventering

| Kapitel | Fil | Titel | Status |
|---|---|---|---|
| 1 | kapitel/kapitel-01.md | Kaffe före förändring | Utkast slutputsat v5 |
| 2 | kapitel/kapitel-02.md | Ett kvitto på engagemang | Utkast slutputsat v5 |
| 3 | kapitel/kapitel-03.md | Fritext | Utkast slutputsat v5 |
| 4 | kapitel/kapitel-04.md | Bilaga 7 | Utkast slutputsat v5 |
| 5 | kapitel/kapitel-05.md | Inte i det här forumet | Utkast slutputsat v5 |
| 6 | kapitel/kapitel-06.md | Kvalitetssäkring | Utkast slutputsat v5 |
| 7 | kapitel/kapitel-07.md | Pausen | Utkast slutputsat v5 |
| 8 | kapitel/kapitel-08.md | Fredagsbeslutet | Utkast slutputsat v5 |
| 9 | kapitel/kapitel-09.md | Rummet utan protokoll | Utkast slutputsat v5 |
| 10 | kapitel/kapitel-10.md | Framtidspunkten | Utkast slutputsat v5 |
| 11 | kapitel/kapitel-11.md | Arbetsmaterial | Utkast slutputsat v5 |
| 12 | kapitel/kapitel-12.md | Den som godkänner tystnad | Utkast slutputsat v5 |
| 13 | kapitel/kapitel-13.md | Styrgruppen | Utkast slutputsat v5 |
| 14 | kapitel/kapitel-14.md | Tolv minuter | Utkast slutputsat v5 |
| 15 | kapitel/kapitel-15.md | Utanför glaset | Utkast slutputsat v5 |
| 16 | kapitel/kapitel-16.md | Den färdiga sanningen | Utkast slutputsat v5 |
| 17 | kapitel/kapitel-17.md | Karin bryter mötet | Utkast slutputsat v5 |
| 18 | kapitel/kapitel-18.md | Protokollet | Utkast slutputsat v5 |

## Kanoniska projektfiler

| Fil | Syfte | Status |
|---|---|---|
| README.md | Start och arbetsflöde | OK |
| roman-bibel.md | Centrala fakta | OK |
| synopsis.md | Handlingsöversikt | OK |
| kapitelplan.md | Kapitelplan och status | OK |
| stilguide.md | Språk, ton och perspektiv | OK |
| tidslinje.md | Händelser i romanen | OK |
| kontinuitetsanteckningar.md | Fakta och öppna trådar | OK |
| revisionsonskemal.md | Planerade förbättringar | OK |
| arbetslogg.md | Projektändringar | OK |
| projektstatus.md | Senaste status och nästa steg | OK |
| karaktarer/huvudperson.md | Huvudperson | OK |
| karaktarer/antagonist.md | Motkraft | OK |
| karaktarer/bifigurer.md | Bifigurer | OK |
| exports/README.md | Exportinformation | OK |
| exports/exportlogg.md | Exporthistorik | OK |
| omslag/omslag-kvartalsmotet.png | Omslagsbild/framsida | OK |
| omslag/README.md | Omslagsmetadata | OK |

## Synkkontroll

- Kapitel i `kapitel/`: 18
- Senaste kapitel i `kapitelplan.md`: Kapitel 18
- Senaste kapitel i `projektstatus.md`: Kapitel 18
- Senaste kapitel i `arbetslogg.md`: Kapitel 18
- Senaste export: Ingen
- Resultat: Synkad efter slutputs och konsekvenskontroll v5


## Senaste revision

- Datum: 2026-08-15
- Typ: GitHub Actions PDF-fix revision 7
- Berörda filer: `publishing/pdf-filter.lua`, `publishing/pdf-template.tex`, `project-manifest.json`, status-/loggfiler
- Resultat: Preview/PDF-bygge korrigerat och lokalt testat


## GitHub Actions-publicering

| Fil/katalog | Syfte | Status |
|---|---|---|
| `.github/workflows/01-validate.yml` | Snabb projektvalidering vid PR/push | OK |
| `.github/workflows/02-build-preview.yml` | Manuellt previewbygge av EPUB/PDF | OK |
| `.github/workflows/03-release.yml` | Releasebygge vid `v*`-taggar | OK |
| `scripts/build_book.py` | Bygger EPUB och PDF från kanoniska kapitel | OK |
| `scripts/validate_project.py` | Validerar kapitel, metadata, omslag och länkar | OK |
| `publishing/` | Metadata och layoutfiler för EPUB/PDF | OK |
| `project-manifest.json` | Maskinläsbar projekt- och publiceringsmetadata | OK |
