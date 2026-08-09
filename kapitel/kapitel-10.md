# Kapitel 10 – Teknikskuld

“Bryt federation,” sa Eva Rask igen.

Hennes röst sprack inte. Den blev bara tunnare, vassare. Som om varje ord hade slipats fram av någon som visste exakt hur dåligt det kunde bli.

På projektorn stod raden kvar:

Extern inloggning: marcus.levin  
Plats: okänd  
Behörighet: global administratör

Marcus stirrade på sitt eget namn.

Det fanns något nästan oanständigt i det. En människa som såg sin identitet användas för något han själv inte förstod, men ändå kunde bli ansvarig för. Lina såg hur han försökte hitta chefens hållning igen, men kroppen svek honom. Händerna låg platt mot bordet. Fingrarna var vita.

“Jag har inte global admin,” sa han.

“Du har det nu,” sa Oskar.

“Det ska vara omöjligt.”

Oskar svarade inte.

De hade sagt det för många gånger.

Jens vände skärmen mot Lina.

“Det gick via central federation. Men inte direkt.”

“Visa.”

Han drog upp en karta, inte den snygga sorten från PowerPoint utan en ful, levande teknisk vy där noderna såg ut som något någon byggt under tidspress och sedan vägrat titta på i dagsljus.

A-03.
A-17.
Kompatibilitetslager.
Behörighetstjänst.
Manuell kö.
central_federation_prod.

Och mellan dem: linjer.

För många linjer.

Lina kände igen känslan. Det var samma som att öppna en garderob man vet är full och ändå bli förolämpad när allt rasar ut.

“Varför finns A-03 kopplad till central federation?” frågade hon.

Jens drog handen över ansiktet.

“Det gör den inte.”

Oskar pekade på skärmen.

“Jo.”

“Den ska inte göra det.”

“Vi är tillbaka där.”

Jens slöt ögonen en sekund.

“Okej. Det finns en indirekt väg.”

“Hur indirekt?”

“Så indirekt att den borde skämmas.”

“No,” sa Noor från sin plats, på engelska av ren stress. “Please tell me this is not another temporary exception.”

Jens sa ingenting.

Lina såg på honom.

“Jens.”

Han lutade sig bakåt.

“Det började som ett migreringsstöd.”

Stefan stönade.

“Nej.”

“Jo.”

“Vilken migrering?” frågade Marcus.

“Identitetsmoderniseringen.”

Det blev tyst på ett särskilt sätt.

Identitetsmoderniseringen hade varit ett av Atlantis stora program. Fyra år, tre programledare, två omstarter och en slutrapport som påstod att projektet levererat “väsentliga förflyttningar mot målbild” vilket i praktiken betydde att ingen längre orkade fråga vad som inte var klart.

Lina hade varit remissinstans på tredje versionen av målarkitekturen.

Hon hade skrivit: beroenden till äldre integrationslager måste brytas innan federation införs brett.

Svaret hade varit: hanteras i senare fas.

Senare fas var myndighetens eleganta namn på aldrig.

“Det skulle vara avvecklat innan federation blev produktionskritisk,” sa hon.

Jens nickade.

“Ja.”

“Varför blev det inte det?”

“För att vissa verksamhetsflöden fortfarande behövde äldre attributformat.”

“Vilka?”

Han klickade.

Listan kom upp.

Terminal Nord.
Terminal Syd.
Kontrollstöd extern.
Tillståndsflöde särskild hantering.
Arkivkoppling äldre ärenden.

Camilla såg på skärmen.

“Det är samma flöden.”

“Ja,” sa Jens.

“Så den gamla manuella hanteringen och identitetsundantaget hänger ihop?”

“Ja.”

“Varför visste ingen det?”

Jens log utan glädje.

“För att alla visste sin del.”

Lina kände hur meningen träffade rummet hårdare än någon teknisk detalj.

Alla visste sin del.

Det var Atlantis i fyra ord.

Marcus tryckte handen mot munnen.

“Kan vi bryta federation utan att stänga ute hela myndigheten?”

Oskar svarade:

“Nej.”

Peter från drift, fortfarande kvar i Teams, sa:

“Tekniskt kan vi bryta federation för specifika beroenden.”

Oskar vände sig mot skärmen.

“Inte om global admin redan är aktiv.”

“Vi kan begränsa tokenutgivning.”

“Hur snabbt?”

Peter tvekade.

“Med rätt godkännande—”

Eva Rask avbröt.

“Godkänt.”

“Från verksamhet—”

“Godkänt.”

“Från driftledning—”

“Peter,” sa Eva.

“Jag förstår.”

Men han började inte skriva.

Lina såg det direkt.

“Vad väntar du på?”

Peter tittade åt sidan, bort från kameran.

“Det finns en change freeze.”

Jens började skratta.

Först lågt. Sedan högre.

Ingen annan skrattade.

“Förlåt,” sa han till slut. “Jag hade glömt att katastrofer måste respektera releasekalendern.”

Peter såg olycklig ut.

“Jag säger inte att vi inte gör det. Jag säger att systemet kommer kräva change-referens.”

Marcus lyfte huvudet.

“Kan du skapa en?”

“Inte utan ärende.”

“Incidentportalen är nere,” sa Lina.

“Ja.”

Alla stirrade på varandra.

Det var inte längre ens satir. Satir hade en gräns där någon överdrev verkligheten för effekt. Atlantis behövde ingen hjälp.

Stefan reste sig.

“Reservrutin.”

“Finns den?” frågade Jens.

“Ja.”

Alla tittade på honom.

Stefan såg för första gången på länge nästan nöjd ut.

“För förändringar under spärrperiod finns manuell reservrutin med muntligt godkännande från verksamhetsansvarig och säkerhetsfunktion.”

Jens pekade på honom.

“Jag tar tillbaka hälften av alla elaka saker jag tänkt om dig.”

“Bara hälften?”

“Det är en process.”

Eva Rask sa:

“Jag är säkerhetsfunktion. Vem är verksamhetsansvarig?”

Camilla höjde handen.

“Min chef kan godkänna.”

“Ring.”

Camilla ringde.

Alla väntade.

Klockan var 11:12.

Lina märkte hur tiden hade förändrat form. Förut hade förmiddagen varit ett antal agendapunkter. Nu var varje minut en behållare för skada. Varje fördröjning kunde bli en ny regel, ett nytt mejl, en ny falsk signering.

Camilla fick svar.

“Vi behöver muntligt godkännande för reservändring under change freeze. Ja. Nej, det är inte samma sak som tidigare. Ja, jag vet att listan ser godkänd ut. Den är inte godkänd. Nej, inte ens om Marcus... Marcus står här. Nej, han har inte godkänt det.”

Hon blundade.

“För att hans konto är kapat.”

Paus.

“Ja. Som i kapat.”

Paus.

“Nej, inte sociala medier. Myndighetskonto.”

Lina såg Jens öppna munnen. Hon pekade på honom utan att titta. Han stängde den.

Camilla lyssnade.

Sedan räckte hon telefonen mot högtalaren.

“Hon godkänner.”

Eva Rask lutade sig fram på skärmen.

“Det här är Eva Rask, informationssäkerhet. Bekräfta att du godkänner reservändring för att begränsa federation och tokenutgivning för berörda äldre flöden.”

En röst i telefonen, skarp och irriterad och mycket vaken nu, svarade:

“Jag godkänner.”

Peter började skriva.

“Jag lägger in change-referens som muntligt reservgodkännande.”

“Gör det,” sa Eva.

“Systemet frågar efter klassning.”

“Kritisk incident.”

“Påverkansområde?”

“Identitet och verksamhetskritiska frigivningsflöden.”

“Återställningsplan?”

Jens stirrade på skärmen.

“Är du seriös?”

Peter såg plågad ut.

“Fältet är obligatoriskt.”

Lina tog ett steg fram.

“Skriv: återställning sker efter verifierad identitet, spårbarhet och avveckling av äldre beroende.”

Peter skrev.

“Det är långt.”

“Systemet får anpassa sig till verkligheten för en gångs skull.”

Oskar tittade på sin egen skärm.

“Global admin-sessionen rör sig.”

“Vart?” frågade Marcus.

“Grupphantering.”

“Vilken grupp?”

Oskar blev tyst.

Lina kände det innan han sa det.

“Global administratörer.”

“No,” sa Noor igen.

“Den försöker lägga till fler konton.”

“Vilka?” frågade Eva.

Oskar läste.

“Först Marcus igen. Sedan ett servicekonto.”

“Vilket servicekonto?” frågade Jens.

Oskar sa namnet.

Jens ansikte förändrades.

Lina hatade att hon redan kände igen den förändringen.

“Vad är det?” frågade hon.

“Det är gammalt.”

“Hur gammalt?”

“Tillräckligt gammalt för att jag fortfarande hade hår som inte gav upp.”

“Jens.”

Han lutade sig över tangentbordet och öppnade en annan vy.

“Det servicekontot användes i identitetsmoderniseringen för synk mellan gamla katalogen och nya federationstjänsten.”

“Användes?”

“Ja.”

“Är det avvecklat?”

Han såg på henne.

“Vill du verkligen fråga?”

Lina slog handen i bordet.

Inte hårt. Tillräckligt.

“Jag vill att någon en enda gång den här morgonen säger att något faktiskt är avvecklat när det ska vara avvecklat.”

Ingen gjorde det.

Stefan sa lågt:

“Vi avvecklar dokument, inte beroenden.”

Det var inte en ursäkt.

Det var nästan en bekännelse.

Noor hade återvänt till AI-grafen.

“Jag kan söka efter servicekontot i beslutsdokumenten.”

“Gör det,” sa Lina.

Oskar invände inte den här gången.

Noor sökte.

Resultaten kom upp.

Beslut om temporär parallell synk.
Riskacceptans äldre attribut.
Avvecklingsplan fas 2.
Avvecklingsplan fas 2 reviderad.
Avvecklingsplan fas 2 slutlig.
Avvecklingsplan fas 2 slutlig ersätter slutlig.

Jens viskade:

“Vi borde förbjudas att namnge filer.”

Noor öppnade den senaste.

“Det står att kontot skulle stängas efter verifierad migrering av samtliga beroende flöden.”

“Vem verifierade?” frågade Marcus.

Noor skrollade.

“Ansvarig: programkontor identitetsmodernisering.”

“Finns det?”

Jens skakade på huvudet.

“Lades ner efter slutrapporten.”

“Vem äger ansvaret nu?” frågade Camilla.

Ingen svarade.

Lina såg på skärmen, på kontot som inte längre hade en ägare men fortfarande hade makt.

Det var inte ett undantag.

Det var en kvarleva med rättigheter.

Teknikskuld var ett för snällt ord. Skuld antydde att någon visste beloppet och hade en plan för återbetalning. Det här var mer som att hitta ett gammalt lån i källaren som börjat skriva egna fakturor.

Peter sa:

“Jag är inne i ändringen. Behöver bekräftelse innan jag trycker.”

Eva svarade:

“Bekräftat.”

Camillas chef i telefonen:

“Bekräftat.”

Marcus tog ett steg fram.

“Bekräftat från IT-strategienheten.”

Oskar sa:

“Vänta.”

Alla stannade.

“Vad nu?” frågade Marcus.

“Om vi begränsar federation på de äldre flödena kommer vi också bryta vår egen möjlighet att använda rollkedjan.”

“Behöver vi den fortfarande?”

Oskar tittade på projektorn.

Observatör hade inte skrivit sedan segmenteringen.

“Jag vet inte.”

Lina såg mot listan på konton. Marcus. Servicekontot. Global admin-gruppen.

“Angriparen försöker skaffa uthållighet,” sa hon.

“Ja.”

“Då måste vi stoppa det.”

“Ja.”

“Även om vi förlorar vår egen väg.”

“Ja.”

Det var Oskar som sa det sista.

Han hade redan förstått beslutet. Han behövde bara hata det först.

Peter tryckte.

På skärmen i Teams syntes ingenting dramatiskt. Ingen röd varning, ingen digital explosion. Bara hans ansikte som blev upplyst av ett administrationsgränssnitt de andra inte såg.

Oskar såg däremot.

“Tokenutgivning begränsad.”

Jens följde noderna.

“A-03 tappar federation.”

Noor såg på grafen.

“Kompatibilitetslagret blir grått.”

Camilla höll telefonen med båda händerna.

Marcus slöt ögonen.

För en sekund kände Lina att rummet faktiskt andades.

Sedan sa Oskar:

“Global admin-sessionen är fortfarande aktiv.”

Peter svor.

“Den borde ha tappat förnyelse.”

“Den har redan hunnit skapa en lokal nödnyckel.”

“Vad är lokal nödnyckel?” frågade Stefan.

Jens svarade:

“Ett sätt att ta sig in när federation inte fungerar.”

Stefan såg på honom.

“Varför finns det?”

“För att när federation inte fungerar vill folk kunna ta sig in.”

“Det låter rimligt.”

“Ja,” sa Lina. “Det är hela problemet.”

Oskar öppnade detaljerna.

“Nödnyckeln är kopplad till ett break-glass-konto.”

Marcus såg upp.

“Det har väl strikt kontroll?”

Oskar läste tyst.

Jens sa:

“Du får inte vara hoppfull nu. Det är olämpligt.”

Oskar fortsatte läsa.

“Break-glass-kontot kräver tvåpersonersgodkännande.”

“Bra,” sa Marcus.

“Godkännare är Marcus Levin och...”

Han stannade.

Lina kände hur hela förmiddagen drog sig samman till en punkt.

“Och?”

Oskar tittade på henne.

“Lina Sjöberg.”

Det blev helt tyst.

På projektorn tändes skärmen igen.

Observatör:
Reservåtkomst initierad.

Observatör:
Tvåpersonersgodkännande krävs.

Sedan kom två rader.

marcus.levin – godkänd  
lina.sjoberg – inväntar

Lina stirrade på sitt namn.

Hennes dator pep.

En godkännanderuta fyllde skärmen.

RESERVÅTKOMST – KRITISK ADMINISTRATION  
Godkänn / Avvisa

Muspekaren rörde sig.

Inte av henne.

Långsamt gled den mot Godkänn.
