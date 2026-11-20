# Líla · Cesta k sobě

Kompletní česká sada tradiční 72polové hry Leela: původní vektorový plán A3, srozumitelný průvodce A4 a barevná webová hra pro **1–6 pojmenovaných hráčů u jednoho zařízení**.

**Hrát:** https://lila-cesta-sebepoznani.ok2clj.chatgpt.site (hostovaná verze může vyžadovat přihlášení vlastníka).

## Tisková sada

- [Herní plán A3 na šířku](dist/downloads/Lila_herni_plan_A3.pdf): 72 českých polí, 10 hadů a 10 šípů.
- [Český průvodce A4](dist/downloads/Lila_navod_A4.pdf): 28 stran, pravidla, přehled přesunů, význam a otázka pro každé pole, závěrečné ohlédnutí a prameny.

Plán tiskněte barevně na A3, 100 %, bez ořezu. Okraje jsou ponechané pro běžný tisk. Pro A4 zvolte přizpůsobení celé stránce; názvy budou menší. Pro větší desku lze použít plakátový tisk PDF na více listů. Příručku tiskněte na A4, vhodně oboustranně.

## Spuštění na počítači

Není potřeba instalovat balíčky ani účet. Potřebujete Python 3 a moderní prohlížeč:

```sh
python3 -m http.server 4173 --directory dist
```

Otevřete http://localhost:4173. Soubory neotvírejte přímo přes `file://`, aplikace načítá JSON a moduly přes HTTP. Při spuštění jen pro vlastní počítač přidejte `--bind 127.0.0.1`.

Celou složku `dist/` lze nasadit na libovolný statický hosting přes HTTPS, včetně GitHub Pages. Aplikace používá relativní cesty, takže funguje i pod `/lila/`. Na GitHub Pages lze jako zdroj publikovat obsah `dist/` pomocí vlastního nasazení, případně jej kopírovat do zvoleného publikačního adresáře. Není zde automatický workflow, který by měnil nastavení účtu.

## Co web umí

- Pojmenovat 1–6 hráčů, přidat osobní záměry a společné téma.
- Házet kostkou, automaticky vyhodnotit série šestek a všechny hady a šípy.
- Zobrazit význam a otázku libovolného pole, vést soukromé poznámky každého hráče.
- Střídat hráče a přeskakovat dokončené cesty; vrátit poslední hod do předání tahu.
- Uchovat rozehranou hru v `localStorage` tohoto prohlížeče.
- Exportovat JSON pro úplnou obnovu, CSV pro tabulku a TXT pro čitelné ohlédnutí.
- Vytisknout deník přes prohlížeč (včetně volby Uložit jako PDF).
- Obnovit hru ze souboru JSON, stáhnout obě hotová PDF a procházet atlas všech 72 polí.

**Více hráčů znamená společnou partii u jedné obrazovky.** Tato verze nemá síťové místnosti, vzdálenou synchronizaci ani účty hráčů. Záloha JSON umožňuje ruční přenos mezi zařízeními. Náhodu generuje Web Crypto s odmítnutím hodnot, které by způsobily modulo zkreslení.

## Pravidla v kostce

Cílem je **68**, nikoli 72. Před vstupem čekáte na šestku, figurka symbolicky stojí na 68. První šestka otevře cestu přes zrození na 6 a dává další hod. Série se vyhodnotí až po hodu 1–5. Přesně tři šestky před závěrečným hodem se ruší; čtyři a více se počítají celé. Při zrušené vstupní trojici se poslední hod počítá z pole 1. Hadi a šípy působí jen na konečné pole série. Při překročení 72 figurka zůstává, při dosud otevíraném vstupu na 6. Z 72 vede had na 51. Každý hráč končí přesným dopadem na 68 nebo šípem z 54.

Detaily, příklady a odlišnosti od jiných edic jsou v [pravidlech](docs/PRAVIDLA.md). Web i PDF používají stejnou, výslovně vymezenou součtovou variantu. Nelze ji označovat za jediná původní pravidla všech historických podob Líly.

## Duchovní smysl a legenda

Rozšířený průvodce věnuje deset stran myšlence hry, jejímu duchovnímu horizontu, symbolice, možnostem osobní proměny a tichému otevření hry. Obsahuje původní třídílnou legendu **Poutnice a tichý dům / Návrat k pramenu / Kámen, který mohl odpočívat**. Příběh není vydáván za staroindický historický pramen. Stejný doprovod najdete na webu v části **Duchovní smysl** a v [samostatném textu](docs/DUCHOVNI_SMYSL.md).

## Dokumentace

- [Pravidla a tradiční přechody](docs/PRAVIDLA.md)
- [Návod k webu, ukládání a exportům](docs/POUZIVANI.md)
- [Architektura a obnova PDF](docs/VYVOJ.md)
- [Prameny a autorské pojetí](docs/ZDROJE.md)
- [Ověření a známá omezení](docs/OVERENI.md)

## Vývoj a testy

Web je záměrně bez frameworku a externích závislostí. Pro testy potřebujete Node.js 20 nebo novější:

```sh
node --test tests/*.test.mjs
```

Zdroj obsahu polí: `scripts/make-data.py`. Duchovní doprovod vytváří `python3 scripts/make-spirit.py` do společného `dist/spirit.json` a dokumentace. Po úpravě spusťte `python3 scripts/make-data.py`; vznikne společný `dist/data.json`. PDF se generují z téhož souboru pomocí macOS CoreGraphics/CoreText, viz dokumentace vývoje. Hotové PDF jsou již přiložené; jejich vytváření není potřeba pro hraní webu.

## Soukromí a pojetí

Žádná analytika, externí fonty ani síťový přenos osobních zápisků. Hosting obvykle eviduje běžné HTTP požadavky; vlastní hra data nikam neodesílá. Sdílený prohlížeč zpřístupňuje hru dalším uživatelům téhož profilu. Export obsahuje jména, záměry a poznámky, proto jej sdílejte po domluvě s hráči.

Líla zde slouží k úvaze a rozhovoru. Pole nejsou hodnocením osoby, diagnózou ani předpovědí. Každý má právo otázku přeskočit.

## Autorské zpracování

Grafika, české vysvětlující texty, otázky a kód byly vytvořeny pro tento projekt. Komerční české edice posloužily jako orientace v zadání, nikoli jako zdroj převzatých ilustrací nebo komentářů. Historické pojmy, rozložení a pravidla jsou popsány s uvedením pramenů. Projekt automaticky nepřiděluje práva k cizím publikacím. O případném zvolení otevřené licence pro vlastní kód a obsah rozhoduje vlastník projektu; tato verze žádnou konkrétní otevřenou licenci neuděluje.
