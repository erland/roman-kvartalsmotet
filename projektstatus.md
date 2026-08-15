# Projektstatus

## Projektmetadata

- Titel: Kvartalsmötet
- Undertitel: Protokollet var redan skrivet
- Författare: Erland Lindmark
- Genre: Organisatorisk thriller med satirisk humor.
- Målgrupp: Vuxen.
- Omslagsbild: Skapad (`omslag/omslag-kvartalsmotet.png`).

## Nuvarande fas

GitHub Actions-publicering uppdaterad: PDF-byggets Lua-filter och PDF-template är korrigerade för preview/release.

## Senast godkända kapitel eller del

- Senast godkända: Inget kapitel är formellt godkänt ännu.
- Senast ändrad: GitHub Actions PDF-bygge korrigerat efter preview-fel.

## Nästa rekommenderade steg

Kör GitHub Actions `Build preview` igen. Preview ska bygga både EPUB och PDF i artifactet `kvartalsmotet-preview`.

## Viktiga öppna beslut

- Om kapitel 1–18 ska markeras som godkända efter användarens helhetsläsning.
- Om nästa leverans ska vara PDF, EPUB eller båda.
- Om omslagsbilden ska användas även i exporten.
- Om någon ytterligare kort epilog eller eftertext önskas.

## Risker att bevaka

- Huvudspåret får inte bli för tekniskt.
- AI-punkten får inte ta över intrigen.
- Karin får inte bli för passiv för länge.
- Tomas får inte bli så tyst att läsaren tappar intresse.
- Humorn ska stärka spänningen, inte punktera den.

## Kontinuitet som måste följas upp snart

- Romanens första hela utkast är färdigt i kapitel 1–18.
- Kapitel 18 fastslår att 12.00-protokollet inte är ostridigt enhetsunderlag.
- `Bilaga 7. Fastställd version` skapades 11.59.48 efter bestridanden, ajournering och aktiv säkerhetsavvikelse.
- Ansvarsmatrisen synliggör logiken “Holm vid invändning, Ryd vid bekräftelse”.
- Internrevisionen har öppnat granskningsnotering och IT-säkerhet har säkrat loggar.
- Lars har skickat korrigerande meddelande till enheten.
- Nästa steg bör vara helhetsläsning/revision innan godkännande eller export.

## Användarens aktuella önskemål

- Kortare roman, cirka 150 sidor.
- Vuxen thriller med spänning, humor och intriger.
- Inblick i personers tankar och känslor, inte bara snabb dialog.
- Viss användning av längre meningar och mer reflekterande rytm.
- Personlighetsmix i gruppen.
- Lågmält romantiskt understråk mellan Karin och Tomas.


## Genomförd strukturell revisionsrunda 1

- Bilaga 7/Norra flödet förtydligades: risken handlar om borttagen manuell spärr och kontroller som inte var testade.
- Erik Branting planterades tidigare genom `EB`, portföljstyrning och 12.00-spår.
- Karin får återkommande sammanfattningar av beviskedjan för att minska teknisk överlast.
- Helena avslöjas som avsändare till de första anonyma varningarna.
- Mira får tydligare motiv till sin tidigare tystnad.
- Lars får en tydligare kurva från kontrollerande chef till pressad och delvis ansvarstagande chef.
- Finalens kärna skärptes: `Tomas bekräftar. Karin balanserar.`
- Kapitel 18 förstärktes med tydligare status för 12.00-protokollet och mer emotionell efterklang.


## Genomförd spänningsrevision v2

- Kapitel 1 fick en skarpare yttre krok genom Tomas vikta A4 med texten `Vänta på versionen`.
- Kapitel 6 fick en starkare kapitelkrok: den ersatta versionen är redan förbilagd dagens protokollutkast, med Tomas namn och en plats reserverad för Karin.
- Kapitel 8, 14 och 15 fick tydligare ankarmeningar som förenklar beviskedjan och håller läsaren nära thrillerkärnan.
- Kapitel 10 fick ett farligare slut genom filen `KH_kompletterande_arkitekturbedömning_utkast.docx`.
- Kapitel 12 planterar tydligare att Helenas varningar både kan vara hjälp och styrning.
- Kapitel 16 ger Mira en mer kostsam offentlig handling när hon erkänner att hon såg den ersatta versionen och teg.
- Kapitel 18 förstärker Karins emotionella slutpunkt: hennes gamla ironiska skydd kommer inte automatiskt, och hon står kvar i rummet utan att gömma sig bakom det.


## Språk- och röstrevision v3

Genomförd 2026-05-21. Fokus: jämnare rytm, tydligare röstmarkörer för Karin, Lars, Mira, Jamal och Eva-Lotta, mindre repetitiva blick- och tystnadsmarkörer, samt putsade övergångar utan att ändra huvudintrigen.


## Revision v4 – karaktär och relationer

Datum: 2026-05-21

Genomfört:
- Karin/Tomas-relationen har förtydligats i kapitel 1, 3, 7 och 18.
- Tomas självuppoffrande mönster har gjorts tydligare i relation till Karin.
- Miras ansvar och yrkesmässiga självbild har fördjupats i kapitel 12 och bärs vidare i kapitel 16.
- Lars ansvarskurva har stärkts genom ett tydligare namngivet ansvarstagande i kapitel 16.
- Slutets emotionella payoff har förstärkts utan att ändra huvudintrigen.


## Slutputs v5 – genomförd kontroll

- Datum: 2026-05-21
- Kapitel 1–18 finns i korrekt numerisk ordning.
- Kapitelrubriker och kapitelnoteringar har normaliserats.
- Revisionskommentarer som råkat ligga i kapitelnoteringarnas öppna frågor har rensats bort.
- Projektets statusfiler pekar nu på slutputsad version 5.
- Inga kapitel är formellt godkända ännu; de är slutputsade utkast.


## GitHub Actions-publicering

- Status: Införd enligt anpassat Romanskaparen-koncept.
- `.github/` ligger i projektroten, på samma nivå som `README.md`.
- Preview-workflow bygger EPUB och PDF som ett gemensamt artifact.
- Release-workflow publicerar EPUB och PDF som separata release-assets vid `v*`-taggar.


## GitHub Actions-fix 2026-08-15

- Åtgärdat PDF-fel `Cannot decode byte '\\x80'` genom att skriva om `publishing/pdf-filter.lua` så den inte använder UTF-8-tecken inuti Lua-pattern-klasser.
- Lagt till `\tightlist` i `publishing/pdf-template.tex` för robust Pandoc/PDF-generering.
- Lokalt test: `scripts/build_book.py --formats epub,pdf` skapar både EPUB och PDF utan fel.
