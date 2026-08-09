# Kapitel 9 – Segmentering

11:04.

Tre minuter kvar.

Lina såg listan på projektorn och kände en märklig klarhet.

Marcus Levin.
Noor Haddad.
Camilla Ågren.
Jens Holm.
Oskar Lind.
Lina Sjöberg.

Det var inte längre en deltagarlista.

Det var en kedja.

Angriparen hade byggt den av roller, förtroenden och gamla undantag. En chef som kunde fatta beslut. En AI-strateg som kunde signera rekommendationer. En verksamhetsrepresentant som kunde bekräfta manuell hantering. En lösningsarkitekt som visste vägarna genom integrationslagren. En säkerhetsarkitekt som kunde begränsa eller släppa igenom. En strategisk arkitekt som kunde få det att se sammanhängande ut.

Det var nästan elegant.

Lina hatade eleganta katastrofer.

“Vi behöver sex bekräftelser?” frågade Marcus.

“Majoritet,” sa Oskar. “Minst fyra av sex.”

“Kan vi använda våra konton?”

“De är komprometterade eller delvis begränsade.”

“Så nej.”

“Så kanske.”

Jens höjde handen.

“Jag vill föreslå att ‘kanske’ inte blir vår officiella incidentstrategi.”

“För sent,” sa Noor.

Camilla stod bredvid dörren med telefonen i handen. Hon såg ut som någon som fått för mycket ansvar utan att först få den traditionella introduktionskursen i hur man undviker ansvar.

“Vad händer om vi inte bekräftar?” frågade hon.

Oskar läste från systemvyn.

“Då kvarstår tidigare beslut.”

“Automatisk prioriterad frigivning?”

“Ja.”

“Vad innebär det konkret?” frågade Stefan.

Jens pekade på sin skärm.

“Mottagande köer behandlar exportpaketet som giltigt beslutsunderlag. De lokala manuella rutinerna kan fortsätta. Frigivningslistan blir svårare att dra tillbaka, eftersom den har både systemstatus, chefsgodkännande, verksamhetsbekräftelse och AI-rekommendation bakom sig.”

“Fast allt är falskt,” sa Camilla.

“Ja,” sa Lina. “Men falskt med rätt metadata.”

Det var kanske den mest myndighetsnära mardröm hon kunde föreställa sig.

Eva Rasks röst kom från Teams-högtalaren.

“Ni måste bryta beslutsflödet eller isolera systemen som behandlar det.”

“Segmentering,” sa Oskar direkt.

“Vilken nivå?” frågade Peter från drift.

Oskar lutade sig fram.

“Ärendetjänstens utgående integrationer, manuell exportkö, behörighetstjänstens äldre kompatibilitetslager, A-03 och A-17. Och projektorns nät åt helvete.”

“Det där är inte en nivå,” sa Peter. “Det är en önskelista.”

“Det är en miniminivå.”

Stefan skakade på huvudet.

“Om vi segmenterar ärendetjänstens utgående integrationer slår vi mot alla flöden som väntar på beslut.”

“Om vi inte gör det,” sa Lina, “släpper vi angriparens beslut vidare.”

“Det vet vi inte.”

“Vi vet tillräckligt.”

Stefan slog handflatan mot bordet.

“Nej, Lina. Du vet tekniskt tillräckligt. Jag vet verksamhetsmässigt att ett stopp kan skapa köer, kostnader, felaktiga kvarhållanden, medborgare och företag som drabbas. Det är också verkligt.”

Hon svarade inte direkt.

För han hade rätt.

Det gjorde inte hotet mindre. Bara valet smutsigare.

Marcus såg mellan dem.

“Vad är alternativet?”

“Partiell segmentering,” sa Jens. “Stoppa bara de mottagande köer som inte redan behandlat paketet. Låt annat flöde fortsätta.”

“Kan vi veta vilka de är?”

“Jag kan se vissa.”

“Vissa?” frågade Marcus.

“Det är ett starkt ord i vår bransch.”

“Jens.”

“Nej. Vi kan inte veta alla. Inte snabbt.”

Camilla lyfte blicken.

“Men vi vet vilka flöden som använder prioriterad frigivning manuellt?”

Alla tittade på henne.

Hon tog ett steg närmare bordet.

“Vi behöver inte stoppa hela ärendetjänsten. Vi måste stoppa de verksamhetsrutiner som kan använda den falska listan. Det är inte alla flöden.”

Stefan såg ut som om han både ville protestera och var stolt.

“Vilka?”

Camilla började räkna på fingrarna.

“Terminal Nord. Terminal Syd. Kontrollstöd extern. Kanske godsflöde Öst om de fått kopian. Inte personflöden. Inte ordinarie lågprioriterade ärenden. Inte arkiverade beslut.”

Jens skrev snabbt.

“Det där är bättre än vår systemkarta.”

“Det är för att jag pratar med människor,” sa Camilla.

Oskar såg plågad ut.

“Vi kan skapa tekniska spärrar mot de köerna om vi får rätt regler.”

“Jag kan ge reglerna,” sa Camilla.

“Noor,” sa Lina. “Kan AI-analysen matcha Camillas flödeslista mot exportpaketets mottagare?”

Noor andades in.

“Ja. Lokalt.”

Oskar öppnade munnen.

“Jag vet,” sa Noor. “Hasha, logga, ingen persondata, inga nya anslutningar, inget moln, inget dumt.”

“Det sista är inte en teknisk kontroll,” sa Oskar.

“Det är den äldsta kontrollen vi har.”

Klockan visade 11:05.

Två minuter.

På projektorn blinkade listan.

Bekräftelse krävs före 11:07.

Observatör skrev i Teams-chatten.

Observatör:
Tid kvar: 120 sekunder.

“Den hånar oss,” sa Jens.

“Det är nästan det minst oroande,” sa Lina.

Marcus gick fram till tavlan.

“Okej. Vi behöver fyra bekräftelser på motbeslutet. Vilka kan vi lita på?”

Ingen svarade.

Det var en absurd fråga i ett rum där alla konton blivit misstänkta.

“Fel fråga,” sa Lina. “Vilka människor kan vi lita på?”

Marcus såg på henne.

Där fanns skillnaden.

Systemet hade tappat identitetens koppling till människan. De behövde skapa en ny, tillfällig, ful men fungerande verifiering.

“Analogt,” sa hon.

Jens lyste upp.

“Papper?”

“Inte papper. Röst. Blick. Fysisk närvaro. Eva på länk verifierar.”

Oskar skakade på huvudet.

“Det räcker inte för systemet.”

“Nej. Men det räcker för oss att veta vem som faktiskt gör vad. Sedan använder vi de minst komprometterade tekniska vägarna.”

Peter från drift sa:

“Jag kan lägga in segmenteringsregler om Eva godkänner och Marcus bekräftar.”

Eva svarade direkt:

“Jag godkänner om Marcus fattar beslutet och ni dokumenterar verksamhetskonsekvens.”

Stefan höjde handen.

“Jag skriver konsekvensen.”

“Nu?” sa Jens.

“Ja.”

“Jag har aldrig sett dig se så levande ut.”

Stefan ignorerade honom och började skriva på Marcus dator, eftersom hans egen hade nätproblem och han vägrade säga det högt.

“Formulera kort,” sa Lina.

Stefan läste medan han skrev.

“Tillfällig begränsning av manuell prioriterad frigivning i identifierade flöden för att förhindra behandling av potentiellt manipulerat beslutsunderlag. Ordinarie opåverkade flöden fortsätter. Verksamhetspåverkan accepteras för berörda flöden tills spårbarhet återställts.”

Jens blinkade.

“Det där var faktiskt begripligt.”

“Jag har alltid kunnat skriva,” sa Stefan. “Jag väljer bara att inte slösa det på er.”

Camilla lutade sig fram.

“Lägg till att lokala enheter ska invänta muntlig bekräftelse från utsedd chef innan de använder nya listor.”

Stefan skrev.

Noor matade in Camillas flöden i analysen.

“Matchning klar. Fyra mottagande köer. Två har behandlat paketet, två väntar.”

“Stoppa de två som väntar,” sa Lina.

Oskar sa:

“Det räcker inte. De två som behandlat kan redan ha skickat vidare.”

“Segmentera utgående från dem också,” sa Jens.

Peter suckade i Teams.

“Ni förstår att det här kommer märkas?”

“Ja,” sa Marcus.

Alla tittade på honom.

Han såg inte säker ut. Men han såg närvarande ut.

“Gör det,” sa han.

Eva Rask sa:

“Bekräfta beslut.”

Marcus gick till mitten av rummet.

“Jag, Marcus Levin, bekräftar tillfällig segmentering av identifierade manuella frigivningsflöden.”

Oskar knappade.

“En.”

Noor reste sig.

“Jag, Noor Haddad, återkallar AI-rekommendationen och bekräftar att exportpaketet inte är giltigt beslutsunderlag.”

“Två,” sa Oskar.

Camilla tog ett steg fram.

“Jag, Camilla Ågren, bekräftar att verksamheten inte ska använda prioriterade frigivningslistor utan muntlig verifiering.”

“Tre.”

Alla tittade på Lina.

Hon kände plötsligt hur mycket hon inte ville göra det.

Inte för att hon var osäker på beslutet.

För att hon visste att angriparen hade byggt spelet så här. Att de svarade på en struktur någon annan skapat. Att även motståndet skedde i angriparens ram.

Men klockan visade 11:06.

Det fanns ingen ren väg.

“Jag, Lina Sjöberg, bekräftar att arkitekturbedömningen är att gamla integrationsvägar och tillfälliga behörigheter inte kan betraktas som tillförlitliga tills de isolerats.”

Oskar tryckte Enter.

“Fyra.”

På projektorn blinkade listan.

Marcus Levin – bekräftad.
Noor Haddad – bekräftad.
Camilla Ågren – bekräftad.
Lina Sjöberg – bekräftad.

Under dem stod Jens och Oskar kvar obekräftade.

Motstridigt beslut registrerat.

Lina hann känna lättnad.

Sedan ändrades texten.

Majoritetsbekräftelse otillräcklig vid säkerhetsklassad processpåverkan.

Full rollkedja krävs.

Jens stirrade.

“Det där stod inte förut.”

Oskar läste systemregeln.

“Den ändrades.”

“När?”

“Nu.”

Observatör skrev i chatten.

Observatör:
Fullständig styrning kräver fullständig ansvarskedja.

Eva Rask sa:

“Det där är inte systemtext.”

“Nej,” sa Lina.

Det var en röst.

Inte tekniskt. Inte bokstavligt.

Men mönstret hade blivit för tydligt.

Någon kommunicerade genom processerna.

Jens tog ett steg fram.

“Jag bekräftar teknisk mottagarkedja och köstopp.”

“Fem,” sa Oskar automatiskt.

Alla tittade på honom.

Han var sist.

Säkerhet.

Oskar såg på skärmen.

Lina såg något mycket mänskligt passera över hans ansikte. Rädsla, men inte för sig själv. För att göra fel. För att bli den punkt där allt antingen stoppades eller låstes fast.

“Oskar,” sa hon.

“Om jag bekräftar via mitt konto och det är kapat kan jag ge angriparen säkerhetsmandat.”

“Om du inte bekräftar går beslutet inte igenom.”

“Jag vet.”

“Kan Eva bekräfta åt dig?” frågade Marcus.

Eva svarade:

“Systemet kräver lokal rollkedja.”

Oskar stod stilla.

Klockan visade 11:06:41.

Lina gick fram till honom.

“Du brukar säga obehagliga saker utan filter.”

“Ja.”

“Säg en nu.”

Han såg på henne.

“Vi borde ha stängt ner mer tidigare.”

“Jag vet.”

“Vi borde inte ha låtit organisationen bygga säkerhet på dokumenterade förhoppningar.”

“Jag vet.”

“Det här kommer inte stoppa allt.”

“Nej.”

Han andades in.

“Men det stoppar nästa led.”

“Ja.”

Oskar nickade en gång.

Sedan skrev han.

“Jag, Oskar Lind, bekräftar teknisk säkerhetsbegränsning av identifierade flöden och spärrar fortsatt automatisk behandling.”

Enter.

Projektorn blinkade.

Full rollkedja bekräftad.

Motbeslut registrerat.

Peter från drift svor i högtalaren.

“Regler går in nu.”

På Noors skärm blev två mottagande köer röda. Sedan två till orange.

Jens lutade sig fram.

“Vi stoppade de väntande.”

“Och de behandlade?” frågade Camilla.

“Utgående segmentering aktiv. Vidarebefordran stoppad.”

Marcus satte handen mot bordet.

För en sekund såg han ut som om han skulle falla.

Lina kände lättnaden slå igenom rummet, men hon litade inte på den.

Inte än.

Observatör skrev inte.

Projektorn visade fortfarande bekräftelsen.

Sedan försvann allt.

Skärmen blev svart.

En ny rad dök upp.

Segmentering registrerad.

Alternativ väg aktiveras.

Oskar blev vit.

“Vad betyder alternativ väg?” frågade Marcus.

Jens svarade innan Oskar hann.

“Att det fanns en annan väg.”

Noor såg på AI-grafen.

En ny röd linje ritades upp.

Inte till ärendetjänsten.

Inte till manuell kö.

Till identitetstjänsten.

Lina läste nodnamnet.

central_federation_prod

Oskar viskade:

“Nej.”

På Teams-skärmen kom Eva Rasks röst, plötsligt skarp:

“Bryt federation. Nu.”

Stefan sa:

“Om vi bryter federation stänger vi ute halva myndigheten.”

Lina såg på klockan.

11:07.

På projektorn dök nästa meddelande upp.

Extern inloggning: marcus.levin
Plats: okänd
Behörighet: global administratör
