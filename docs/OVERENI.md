# Ověření verze 1.0

## Automatické testy

`node --test tests/*.test.mjs`: devět testů, všechny prošly. Kontrolují:

- úplnost ID 1–72 a 10 + 10 propojení;
- vstup a čekání, včetně zrušených vstupních tří šestek;
- součet série, zrušení právě tří a ponechání čtyř šestek;
- každý z dvaceti konkrétních přesunů;
- přesný cíl 68, jeho překročení, 72–51 a nemožnost překročit 72;
- střídání, sólo hru a vynechání dokončených hráčů;
- odmítnutí nesprávných sekvencí;
- odstraňování modulo zkreslení kostky;
- uvozování CSV a ochranu běžných začátků tabulkových vzorců.

`node --check dist/app.js`: bez chyby syntaxe.

## PDF

Obě PDF vytvořena a znovu otevřena PDFKitem. Plán má jednu stranu A3 na šířku; průvodce 18 stran A4. Všechny strany se vykreslily do PNG pro vizuální kontrolu; text byl extrahován pro porovnání názvů a otázek. Před vydáním byl zkontrolován plán, titul, pravidla, atlas i prameny. Texty nejsou rastrové obrázky.

## Známé meze

Jde o partii u jednoho zařízení, bez online synchronizace. Poznámka u pole je aktuální verzí zápisu, nikoli časovou řadou. Vrácení hodu nepřežije nové načtení a předání tahu. Změna internetové adresy nebo profilu prohlížeče oddělí místní uložené hry; JSON je způsob přenosu. Tiskový deník obsahuje poznámky navázané na trasy tahů, zatímco TXT a JSON zahrnují i ostatní zápisky.

Praktický tisk na konkrétní tiskárně nebyl proveden. Doporučujeme první kontrolní výtisk před laminací.
