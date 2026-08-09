# Kontinuitetsanteckningar


## Kapitel 4 – nya fasta fakta
- Gruppen strukturerar incidenten i en workshopliknande form trots situationens allvar.
- Jens delar upp problemet i identitet, integrationsväg och verksamhetspåverkan.
- Det finns flera motstridiga integrationskartor.
- AI-demon används lokalt för att jämföra dokumenterade systemrelationer med tekniska relationer.
- En koppling hittas mellan ärendetjänsten och ett system som alla tror är avvecklat.
- Ett aktivt tullärende ändras i produktion.


## Kapitel 5 – nya fasta fakta
- Ett tullärende har ändrats från granskning till frigiven.
- Lokala verksamhetsdelar går över till manuell hantering.
- Det finns flera parallella manuella rutiner för avvikande frigivning.
- Terminal Nord har en gammal specialrutin efter en tidigare integrationsstörning.
- Delade filytor används fortfarande för kritiska manuella flöden.
- En falsk fil laddas upp i Camillas namn: frigivning_prioriterad.xlsx.
- Filen laddas ned av flera verksamhetsfunktioner.


## Kapitel 6 – nya fasta fakta
- Marcus godkänner att nya skrivningar stoppas på den delade ytan.
- TEMP-MANUELL-FRIGIVNING-UTÖKAD är en gammal tillfällig behörighetsgrupp.
- Gruppen skapades som sexveckors workaround men är fortfarande aktiv.
- Gruppen har fyrtiosex medlemmar.
- Gruppen ger utökad hantering av frigivningsstatus och export till manuell kö.
- A-03 är en fallback-nod kopplad till äldre flöden.
- Marcus läggs till i gruppen av Linas kapade konto.
- Ett falskt mejl skickas från Marcus konto som godkänner frigivningslistan.
- Noor läggs till i gruppen av Marcus konto i realtid.


## Kapitel 7 – nya fasta fakta
- AI-underlaget innehåller deltagarlista med namn, roll, enhet, mejladress, användar-ID, behörighetsprofil och ansvarsområde.
- Noor kan via TEMP-MANUELL-FRIGIVNING-UTÖKAD trigga prioriterad manuell frigivningskö och godkänna exportpaket.
- Ett exportpaket heter AI_rekommenderad_prioritering.zip och ligger i kö för Noors signering.
- Angriparen verkar utnyttja förtroendekedjor: Lina som arkitekt, Marcus som chef, Camilla som verksamhetsrepresentant, Noor som AI-ansvarig.
- Dokumenthistorik har manipulerats för att koppla Noor och Oskar till äldre beslut.
- KVALITETSSAKRING_DECENTRALISERAD_ARKITEKTUR_SLUTVERSION.pptx har ändrats externt.
- Projektorn visar en ny beslutspunkt klockan 11:00: Aktivera automatisk prioriterad frigivning.


## Kapitel 8 – nya fasta fakta
- Beslutspunkten klockan 11:00 aktiveras.
- AI_rekommenderad_prioritering.zip signeras och distribueras via Noors konto.
- Incidentforumet skapas med ledning, säkerhet, drift, kommunikation och juridik.
- En okänd deltagare med namnet Observatör finns i incidentforumet.
- Observatör har lagts till av Eva Rasks konto utan att hon gjort det.
- Observatör skriver protokolliknande beslutstext i chatten.
- Eva Rask identifierar personerna i Fyrskeppet som del av attackytan.
- Rollkedjan består av Marcus, Noor, Camilla, Jens, Oskar och Lina.
- Ett motstridigt motbeslut kräver majoritetsbekräftelse före 11:07.


## Kapitel 9 – nya fasta fakta
- Rollkedjan bekräftar ett motbeslut mot automatisk prioriterad frigivning.
- Camilla identifierar berörda manuella flöden.
- Stefan formulerar verksamhetskonsekvensen för segmentering.
- Segmentering stoppar väntande mottagande köer och vidarebefordran från behandlade köer.
- Observatör ändrar eller presenterar regeln så att full rollkedja krävs.
- Alternativ väg aktiveras mot central_federation_prod.
- Eva Rask beordrar att federation bryts.
- Marcus konto loggar in externt med global administratörsbehörighet.


## Kapitel 10 – nya fasta fakta
- Identitetsmoderniseringen lämnade kvar äldre beroenden mellan A-03/A-17, kompatibilitetslager och central federation.
- Vissa verksamhetsflöden behövde äldre attributformat och höll beroenden vid liv.
- Ett gammalt servicekonto för synk mellan gammal katalog och ny federation finns kvar.
- Change freeze finns aktiv men kan kringgås via manuell reservrutin.
- Camillas chef och Eva Rask godkänner reservändring muntligt.
- Peter från drift begränsar tokenutgivning och äldre federationsflöden.
- Global admin-sessionen överlever åtgärden genom att skapa eller aktivera lokal nödnyckel.
- Break-glass-konto kräver tvåpersonersgodkännande från Marcus Levin och Lina Sjöberg.
- Marcus är redan markerad som godkänd i break-glass-flödet.
- Linas dator visar godkännanderuta där muspekaren rör sig mot Godkänn utan hennes kontroll.


## Kapitel 11 – nya fasta fakta
- Jens stoppar break-glass-godkännandet genom att dra ur Linas nätverksanslutning.
- Linas telefon får också reservåtkomstförfrågningar och stängs av.
- Alla personliga enheter i rummet isoleras eller stängs av.
- Första kända åtkomst till AI-underlaget skedde 08:41 via funktionskontot Fyrskeppet_av.
- Mötesrumsmoderniseringen gav temporär åtkomst till intern dokumentyta utan slutdatum.
- Fyrskeppets mötesteknik var angriparens första brohuvud.
- Peter isolerar Fyrskeppet från nätet, vilket släcker Teams, projektor och mötesljud.
- En leverantörsliknande person dyker upp utanför rummet med begäran om lokal återaktivering.


## Kapitel 12 – nya fasta fakta
- Daniel Ryd uppger sig vara leverantörstekniker och vill återaktivera Fyrskeppet.
- Receptionen har inte skickat Daniel.
- Baltic Room Solutions är underleverantör för fjärrdiagnostik och firmware i mötesrumsmoderniseringen.
- Rumsplattformens servicekonto kunde läsa mötesbokningar, deltagarlistor och bifogade dokument.
- Intrångskedjan rekonstrueras: 08:41 dokumentåtkomst via Fyrskeppet_av, 09:37 behörighetsändring, 09:44 Linas identitet via A-17, 10:41 Marcus via Lina, 10:52 Noor via Marcus, 11:00 exportpaket, 11:07 federation, 11:18 break-glass-försök.
- Angriparens mål är ett beslagtaget godsflöde med särskild kontroll.
- Ärendet har nästa behandlingspunkt 11:35.
- Rumsnoden har mobil reservkanal som kringgår nätsegmentering.


## Kapitel 13 – nya fasta fakta
- Rumsnodens modemreserv stoppas fysiskt genom att antennmodulen dras loss.
- Fjärråterställningen stoppas vid 99 procent.
- Marcus och Jens når terminalens lokala beslutsansvariga via analog telefon.
- Camilla formulerar instruktion om fysisk kvarhållning av godset.
- Terminalen bekräftar fysisk spärr av godsflödet.
- Daniel försöker ta sig in men stoppas och omhändertas av väktare.
- Daniel hävdar att han följde fjärrinstruktioner.
- Break-glass fullbordas inte.
- Primär attackväg via mötesrum isoleras och mobil reservkanal bryts.
- Gruppens centrala efterfråga blir: vad har organisationen låtit bli att förändra?


## Kapitel 14 – nya fasta fakta
- Fyrskeppet förblir offline efter incidenten.
- Daniel Ryd är verklig konsult men hävdar att han följde fjärrinstruktioner.
- Godset är fysiskt spärrat, ärendet fryst, exportpaketet återkallat och break-glass ofullbordat.
- Gruppen formulerar efteranalysens kärna: problemet var aldrig bara intrånget.
- Holmgren vill först tona ned systemiska slutsatser men accepterar större genomlysning.
- Gruppen blir initial arbetsgrupp för genomlysningen.
- Slutformulering på tavlan: Börja med det som fortfarande kallas tillfälligt.
- Lina lämnar Fyrskeppet med insikten att människor kan förändras även om organisationer gör motstånd.
