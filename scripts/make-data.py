import json,pathlib
# Původní české komentáře a otázky; tradiční názvy slouží jako orientační pojmy.
rows='''Zrození|Janma|Každá cesta začíná ochotou vstoupit do neznámého. Zrození zde připomíná chvíli, kdy dáš svému záměru konkrétní podobu.|Čemu chci právě teď dát začátek?
Iluze|Maya|To, co si o situaci vyprávíš, nemusí být celá skutečnost. Rozlišuj pozorovatelná fakta od svých domněnek.|Co vím jistě a co si pouze domýšlím?
Hněv|Krodha|Hněv upozorňuje na překročené hranice nebo nenaplněné potřeby. Jeho energii můžeš proměnit v jasné sdělení bez ubližování.|Jakou potřebu můj hněv chrání?
Chamtivost|Lobha|Touha mít stále víc dokáže zastínit to, co už stačí. Všímej si okamžiku, kdy se potřeba mění v nekonečný hlad.|Jak poznám, že mám dost?
Hmotná rovina|Bhu-loka|Tělo, domov a každodenní povinnosti tvoří základ tvé cesty. Duchovní úvaha může začít docela obyčejnou péčí o sebe.|Co konkrétního dnes potřebuje moje tělo?
Zaslepení|Moha|Silné připoutání zužuje pohled na jedinou možnost. Ustup o krok a dovol si vidět i to, co se do tvého přání nehodí.|Na čem lpím tak silně, že přehlížím jiné možnosti?
Pýcha|Mada|Pocit vlastní důležitosti může bránit učení. Hodnota člověka přitom nemusí stát na převaze nad někým jiným.|Kde se snažím působit lépe, místo abych byl upřímný?
Lakota|Matsarya|Svírání majetku, času nebo uznání často vyrůstá ze strachu ze ztráty. Bezpečí lze hledat také ve vztazích a důvěře.|Co držím příliš pevně a čeho se bojím?
Smyslová rovina|Kama-loka|Smysly přinášejí potěšení i rozptýlení. Pozoruj rozdíl mezi tím, co tě vyživuje, a tím, čím pouze přehlušuješ nepohodu.|Který požitek mi prospívá a který mě odvádí od sebe?
Očista|Shuddhi|Očista je prostor po tom, co už nepotřebuješ. Může jít o úklid, odpočinek i ukončení návyku, který ti bere sílu.|Co mohu ze svého dne odstranit, aby se mi lépe dýchalo?
Zábava|Gandharva|Hravost uvolňuje napětí a vrací lehkost. Všimni si také, zda zábava někdy neslouží jako způsob, jak odložit důležitou věc.|Kdy si dovoluji radost bez výčitek?
Závist|Irshya|Srovnávání ukazuje něco, po čem toužíš. Místo hodnocení druhého můžeš hledat vlastní cestu k této kvalitě.|Co obdivuji u druhých a jak to mohu rozvíjet u sebe?
Prázdnota|Antariksha|Mezidobí bez jasného směru může být nepříjemné. Nemusíš je hned zaplnit; někdy právě v tichu dozrává další krok.|Co se objeví, když na chvíli přestanu vyplňovat každou mezeru?
Jemná rovina|Bhuvar-loka|Vnitřní obrazy a nálady ovlivňují tvé prožívání, i když je druzí nevidí. Vnímej je jako zkušenost, kterou lze pozorovat.|Jaká nálada dnes barví můj pohled na svět?
Svět fantazie|Naga-loka|Představivost otevírá možnosti. Aby se sen mohl stát skutečností, potřebuje také malý proveditelný krok.|Kterou představu chci vyzkoušet v běžném životě?
Žárlivost|Dvesha|Strach, že přijdeš o vztah nebo své místo, může vyvolat potřebu kontrolovat. Zkus místo kontroly pojmenovat svou nejistotu.|O jaké ujištění mohu požádat otevřeně?
Soucit|Daya|Soucit znamená vnímat bolest bez nutnosti soudit. Může být laskavý a zároveň zachovat vlastní hranice.|Jak bych reagoval, kdybych znal celý příběh druhého?
Radost|Harsha-loka|Radost nemusí čekat na dokonalé podmínky. Všimni si drobných okamžiků, ve kterých už život působí dobře.|Co mi dnes přineslo nečekanou radost?
Rovina činů|Karma-loka|Jednání má důsledky, i když výsledek nelze plně řídit. Soustřeď se na část situace, za kterou můžeš převzít odpovědnost.|Jaký krok je nyní skutečně v mé moci?
Štědrost|Dana|Dávání nemusí znamenat velký dar. Čas, pozornost nebo zkušenost mohou být cenné, pokud je nabízíš svobodně.|Co mohu nabídnout bez očekávání protislužby?
Náprava|Samana papa|Uznání chyby má smysl tehdy, když vede k opravě. Sebetrestání lze nahradit odpovědností a konkrétní změnou.|Co mohu napravit a komu se potřebuji omluvit?
Dharma|Dharma-loka|Dharma připomíná řád a smysluplné jednání. Hledej soulad mezi svými hodnotami, okolnostmi a tím, co skutečně děláš.|Podle jaké hodnoty se chci v této situaci zachovat?
Nebeská rovina|Svarga-loka|Příjemné období přináší úlevu. Užij si ho, aniž bys od něj očekával, že bude trvat beze změny.|Co dobrého nyní přijímám a dokážu ocenit?
Špatná společnost|Ku-sanga|Prostředí ovlivňuje to, co považuješ za normální. Všímej si vztahů, po kterých ztrácíš jasnost nebo vlastní hlas.|Ve které společnosti se vzdaluji svým hodnotám?
Dobrá společnost|Su-sanga|Podpůrné vztahy dávají prostor pravdivosti i růstu. Nemusejí se vším souhlasit, aby ti pomáhaly.|Kdo mě podporuje a zároveň mi umí říct pravdu?
Smutek|Duhkha|Smutek bývá odpovědí na ztrátu nebo nenaplněné přání. Dovol mu prostor a hledej přiměřenou oporu.|Co potřebuji oplakat a co mi při tom pomáhá?
Nesobecká služba|Paramartha|Užitečná činnost může přesáhnout osobní prospěch. Udržitelné pomáhání ale počítá i s tvou vlastní kapacitou.|Komu mohu prospět způsobem, který mě nevyčerpá?
Vlastní cesta|Sudharma|Smysluplná praxe odpovídá člověku, který ji žije. Nemusíš přebírat cizí cestu jen proto, že je obdivovaná.|Co je mi vlastní, i když to druzí dělají jinak?
Odklon od hodnot|Adharma|Když jednání ztrácí oporu v hodnotách, vzniká vnitřní rozpor. Návrat může začít jediným poctivým rozhodnutím.|Kde své hodnoty znám, ale nejednám podle nich?
Dobré sklony|Uttama gati|Opakované drobné volby se stávají návykem. Podpoř směr, který ti prospívá, vhodnými podmínkami místo pouhé vůle.|Který dobrý návyk si chci usnadnit?
Posvátná rovina|Yaksha-loka|Některé chvíle vnímáš jako zvlášť hodnotné. Pozornost a úcta mohou proměnit i obyčejnou činnost v něco smysluplného.|Čemu chci v životě věnovat větší úctu?
Rovnováha|Maha-loka|Rovnováha se průběžně upravuje podle situace. Není třeba rozdělovat všechno stejně; důležité je včas poznat vychýlení.|Čeho je teď příliš a čeho málo?
Rovina vůně|Gandha-loka|Vůně a další jemné vjemy vracejí pozornost do přítomnosti. Zpomal a všimni si prostředí, ve kterém právě jsi.|Jaký drobný vjem mě dokáže ukotvit tady a teď?
Rovina chuti|Rasa-loka|Chuť připomíná schopnost rozlišovat a vychutnávat. Všímej si kvality prožitku, místo abys jen přidával další podněty.|Co bych si více užil, kdybych zpomalil?
Očistec|Naraka-loka|Tradiční obraz bolestného místa lze číst jako setkání s důsledky. Obtížná zkušenost může ukázat, co je potřeba změnit.|Jakou změnu ode mě současná obtíž vyžaduje?
Jasné vědomí|Svachchha|Jasnost přichází, když na chvíli ustoupí hluk soudů. Zkus situaci popsat jednoduše, bez přikrašlování i obviňování.|Jak by zněl věcný popis toho, co se děje?
Sebepoznání|Jnana|Poznání sebe vzniká pozorováním skutečných reakcí. Všímej si rozdílu mezi tím, jaký chceš být, a tím, co právě prožíváš.|Co jsem se o sobě dozvěděl z poslední náročné situace?
Životní energie|Prana-loka|Energie není nevyčerpatelná. Sleduj, které činnosti ti dodávají sílu a které ji dlouhodobě spotřebovávají.|Co mě skutečně obnovuje?
Uvolňování|Apana-loka|Odložení přebytečného vytváří prostor pro nové. Můžeš pustit úkol, očekávání nebo zvyk, který už neslouží.|Co si nesu dál jen ze zvyku?
Proudění|Vyana-loka|Jednotlivé části života spolu souvisejí. Malá změna v odpočinku, práci nebo komunikaci může ovlivnit celý den.|Kde se můj život zasekl a co by obnovilo pohyb?
Lidská rovina|Jana-loka|Společný život zahrnuje blízkost i rozdílnost. Setkej se s druhým jako s člověkem, ne pouze jako s rolí ve svém příběhu.|Co mi pomáhá slyšet druhého bez okamžité obrany?
Rovina ohně|Agni-loka|Oheň symbolizuje sílu proměny. Zápal potřebuje směr a míru, aby vytvářel místo toho, aby spaloval.|Kam chci nasměrovat svou rozhodnost?
Lidské zrození|Manushya janma|Lidská zkušenost nabízí možnost uvědomovat si své jednání. Svoboda začíná malou mezerou mezi podnětem a reakcí.|Kde dnes mohu reagovat vědoměji než obvykle?
Nevědomost|Avidya|Nevědomost není ostuda, pokud ji dokážeš přiznat. Jistota bez ověření někdy brání porozumění více než samotná neznalost.|Co potřebuji zjistit, než udělám závěr?
Pravé poznání|Suvidya|Poznání se projevuje v jednání, ne jen ve slovech. Ověřuj své porozumění zkušeností a ochotou opravit názor.|Jak poznám v praxi, že něčemu opravdu rozumím?
Rozlišování|Viveka|Rozlišování pomáhá oddělit okamžité nutkání od dlouhodobě smysluplné volby. Dopřej rozhodnutí potřebný čas.|Co je teď příjemné a co je pro mě skutečně dobré?
Neutralita|Sarasvati|Odstup může otevřít více pohledů současně. Neutralita však nemusí znamenat lhostejnost nebo vyhýbání se odpovědnosti.|Jak by situaci popsal někdo, kdo nestojí na žádné straně?
Sluneční rovina|Yamuna|Slunce zde symbolizuje aktivní, vystupující sílu. Všímej si své schopnosti začít, rozhodnout a vstoupit do dění.|Kde potřebuji více zdravé iniciativy?
Měsíční rovina|Ganga|Měsíc připomíná přijímání, odpočinek a citlivost. I naslouchání a čekání mohou být plnohodnotnou součástí cesty.|Kde si mohu dovolit přijímat místo neustálého výkonu?
Kázeň|Tapas-loka|Kázeň je pravidelná péče o zvolený směr. Nejlépe slouží, když podporuje život a nestává se trestem.|Jaký malý závazek dokážu poctivě dodržet?
Země|Prithvi|Návrat na zem obnovuje kontakt s tím, co je konkrétní. Začni tím, co můžeš vidět, udělat a dokončit.|Jaký obyčejný krok mě teď ukotví?
Násilí|Himsa-loka|Ubližování může mít podobu činu, řeči i nátlaku. Všímej si dopadu svého jednání a hledej způsob, jak škodu zastavit.|Kde mohu nahradit tlak jasnou a respektující hranicí?
Vodní rovina|Jala-loka|Voda symbolizuje přizpůsobivost a citový pohyb. Pružnost nemusí znamenat ztrátu vlastního směru.|V čem mohu povolit, aniž bych zradil sám sebe?
Oddanost|Bhakti-loka|Oddanost znamená věnovat pozornost něčemu, co přesahuje okamžitý prospěch. Připomíná důvěru, péči a ochotu přestat vše řídit.|Čemu chci sloužit celým srdcem?
Ego|Ahamkara|Příběh o sobě pomáhá orientaci, ale může se stát těsnou klecí. Nemusíš každou odlišnost vnímat jako ohrožení.|Kterou svou nálepku bráním až příliš?
Prvotní zvuk|Omkara|Zvuk připomíná rytmus a počátek vyjádření. Naslouchej tónu svého hlasu i tomu, co zůstává mezi slovy.|Jak zní můj vnitřní rozhovor, když se mi nedaří?
Vzdušná rovina|Vayu-loka|Vzduch symbolizuje pohyb a otevřenost. Změna perspektivy může uvolnit to, co se z jediného místa zdá neprůchodné.|Jaký nový pohled chci připustit?
Rovina záření|Tejas-loka|Záření lze chápat jako vliv, který máš na své okolí. Všímej si, co přináší tvoje přítomnost i bez velkých slov.|Jakou atmosféru kolem sebe vytvářím?
Rovina pravdy|Satya-loka|Pravdivost propojuje vnitřní zkušenost s tím, co říkáš. Může být citlivá a nemusí sloužit jako zbraň.|Jakou pravdu potřebuji vyslovit laskavě?
Dobrý úsudek|Subuddhi|Rozum může hledat řešení, která berou v úvahu širší důsledky. Dobré rozhodnutí počítá s fakty i lidskou zkušeností.|Které řešení prospívá také lidem kolem mě?
Zkreslený úsudek|Durbuddhi|Chytré zdůvodnění někdy pouze zakrývá přání. Zkus rozpoznat, kdy hledáš porozumění a kdy obhajobu předem zvoleného závěru.|Jaký nepohodlný fakt ve své úvaze vynechávám?
Štěstí|Sukha|Spokojenost lze někdy najít i bez dalšího úspěchu. Všimni si rozdílu mezi klidným naplněním a krátkou úlevou.|Co v mém životě už nyní funguje dobře?
Temnota|Tamas|Zamlžení a útlum mohou bránit pohybu. Začni malým rozpoznáním současného stavu a jednou dostupnou oporou.|Co je nejmenší krok, který mi pomůže z nehybnosti?
Svět jevů|Prakriti-loka|Svět forem je proměnlivý a vzájemně propojený. Pozoruj změnu, aniž bys od každé podoby vyžadoval trvalost.|Kterou proměnu se právě učím přijímat?
Vnitřní prostor|Antar-loka|Vnitřní prostor umožňuje všimnout si myšlenky, aniž bys ji musel hned následovat. Krátká pauza rozšiřuje možnost volby.|Co slyším, když na chvíli ztiším vnější podněty?
Blaženost|Ananda-loka|Blaženost je zde obrazem hlubšího souladu. Není nutné ji vyrábět ani si vyčítat, když právě nepřichází.|Kdy jsem naposledy cítil klidný soulad se životem?
Kosmické dobro|Rudra-loka|Širší pohled přesahuje jednotlivý zájem. Ptej se, jak tvé rozhodnutí ovlivňuje vztahy, prostředí a budoucnost.|Co by bylo dobré v širším měřítku?
Kosmické vědomí|Vaikuntha-loka|Cíl hry symbolizuje celek, v němž se jednotlivé zkušenosti mohou propojit. Uzavři cestu tím, co si chceš odnést do života.|Co nyní chápu jinak a jak podle toho chci jednat?
Absolutní rovina|Brahma-loka|Představa úplnosti může být inspirativní i svůdná. Ani pocit, že už všechno chápeš, nemusí znamenat konec učení.|Kde zaměňuji vznešenou představu za prožitou zkušenost?
Čistota a soulad|Sattva-guna|Sattva označuje kvalitu jasnosti a vyrovnanosti. Podporuj podmínky, ve kterých je snazší vnímat a jednat s rozvahou.|Co v mém prostředí podporuje jasnost?
Činnost a neklid|Rajo-guna|Radžas označuje pohyb, touhu a aktivitu. Energie slouží dobře, pokud nemusí neustále dokazovat vlastní hodnotu.|Která činnost má smysl a která jen zaplňuje neklid?
Setrvačnost|Tamo-guna|Tamas jako setrvačnost uzavírá číselnou řadu a vrací hru na zem. Nový začátek může vyžadovat opuštění pohodlné nehybnosti.|Co mě drží na místě a jaký jednoduchý krok zvolím?'''
fields=[]
for i,line in enumerate(rows.splitlines(),1):
 name,term,meaning,question=line.split('|'); fields.append(dict(id=i,name=name,term=term,meaning=meaning,question=question))
assert len(fields)==72
root=pathlib.Path(__file__).resolve().parents[1]
data=dict(version=1,fields=fields,arrows={10:23,17:69,20:32,22:60,27:41,28:50,37:66,45:67,46:62,54:68},snakes={12:8,16:4,24:7,29:6,44:9,52:35,55:3,61:13,63:2,72:51})
(root/'dist/data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
