# Vývoj a struktura projektu

## Bez závislostí na webu

Statická aplikace používá HTML, CSS, ES moduly, Fetch, Web Crypto, Blob a localStorage. Cílem je současný Chrome, Firefox, Safari či Edge přes HTTPS nebo localhost. Není potřeba sestavení ani npm install. Server pouze obsluhuje soubory.

```
dist/
  index.html       stránka hry
  style.css        responzivní vzhled
  app.js           rozhraní, ukládání, importy a exporty
  engine.js        čistá logika a generování hodů
  data.json        72 polí a mapy 20 přesunů
  spirit.json      společný duchovní doprovod pro web a PDF
  downloads/       hotové PDF
scripts/
  make-data.py     zdroj původního českého obsahu
  make-spirit.py   duchovní kapitoly a původní alegorická legenda
  make-pdfs.m      macOS generátor vektorových PDF a kontrolních PNG
tests/
  engine.test.mjs  hraniční případy pravidel
docs/              česká dokumentace
```

## Úpravy obsahu

Upravte `scripts/make-data.py`, nikoli jen odvozený JSON. Spusťte:

```sh
python3 scripts/make-data.py
node --test tests/*.test.mjs
```

`id` 1–72 jsou stabilní. Při změně pravidel upravte engine, webový návod, markdown dokumentaci a PDF společně. Změna formátu zálohy vyžaduje verzování a migrační strategii. Současná verze přijímá `version: 1` a `rules: johari-series-v1`.

## Obnovení PDF na macOS

Generátor používá systémové frameworky AppKit, CoreText a PDFKit. Vyžaduje macOS s Command Line Tools a fonty Arial a Georgia. Nepotřebuje placený program ani stažené obrázky.

```sh
clang -fno-modules -framework AppKit -framework CoreText -framework PDFKit scripts/make-pdfs.m -o /tmp/lila-pdf
/tmp/lila-pdf "$PWD"
```

Vzniknou dvě PDF v `dist/downloads/` a kontrolní vykreslení všech stran v ignorované složce `tmp/pdfs/`. Velikosti: A3 420 × 297 mm, A4 210 × 297 mm. Text se sází pomocí CoreText, není obrázkem. Generátor také uloží extrahované texty pro kontrolu. Jiný operační systém může web provozovat bez omezení; pro opětovnou sazbu PDF je v této verzi potřeba macOS nebo vlastní náhrada generátoru.

## Herní stav

`players`: jméno, záměr, `position` (null před vstupem), `finished`, `notes` indexované číslem pole. `active` určuje aktuálního hráče. `rolls` obsahuje nerozhodnutou sérii šestek. `history` obsahuje čas, hráče, hody, trasu a souhrn. `awaitNext` brání dalšímu hodu po uzavření tahu. `backup` pro vrácení je pouze v paměti a neexportuje se.

## Nasazení

Publikuje se pouze `dist/`. `.openai/hosting.json` identifikuje hostovanou instanci; neobsahuje přístupový token. Repo na GitHubu a hostovaná instance jsou dva samostatné cíle. Aktualizace repozitáře sama automaticky nepublikuje hostovanou instanci. Na GitHub Pages je nutné nastavit vlastní publikaci statického výstupu; tento projekt žádné takové nastavení automaticky nevynucuje.

## Možná rozšíření

Síťové místnosti by vyžadovaly serverový autoritativní stav, kódy místností, ověření hráčů a řešení souběhu tahů. Současná lokální hra takovou funkci nepředstírá. Dále by šly přidat migrované zálohy, více pravidlových variant nebo samostatné poznámky pro každou návštěvu pole.

## Rozšířený duchovní doprovod

`python3 scripts/make-spirit.py` obnoví `dist/spirit.json` a `docs/DUCHOVNI_SMYSL.md` ze stejného zdroje. Web ho načítá až po otevření duchovní části a ošetřuje text escapováním. PDF generátor vkládá deset stran před praktický návod. Celkem má průvodce 28 stran. Přepínač `/tmp/lila-pdf "$PWD" --guide-only` aktualizuje pouze průvodce a ponechá existující plán.
