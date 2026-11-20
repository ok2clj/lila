# Používání webu

## Společná partie

Vyplňte jména (nejvýše 40 znaků) a volitelné osobní záměry (nejvýše 300 znaků). Tlačítkem Přidat hráče rozšíříte skupinu až na šest; křížkem ji zmenšíte až na jednoho. Pořadí jmen určuje střídání. Společné téma je volitelné.

Po zahájení používejte Hodit kostkou. Po šestce hází stejný hráč znovu; série se vyhodnotí po 1–5. Poté si přečtěte zvýrazněné pole, případně kliknutím i cíl hada nebo šípu. Pole lze prozkoumat kdykoli, i bez rozehrané hry. Poznámka náleží aktuálnímu hráči a právě vybranému poli. U jednoho pole se uchovává poslední verze poznámky, nikoli samostatná poznámka pro každou návštěvu.

Předávejte hru tlačítkem Další hráč. Vrátit poslední hod funguje jednou, dokud nepředáte tah; zahrnuje celý stav před posledním hodem, tedy i případnou změnu zápisků po tomto hodu. Po obnovení stránky se historie vrácení neuchovává.

## Ukládání a export

Hra se průběžně ukládá v `localStorage`, pod klíčem `lila-cesta-v1`. Po načtení stejné adresy ve stejném profilu prohlížeče pokračuje rozehraná partie. Vymazání dat prohlížeče může hru odstranit; anonymní režim obvykle neuchová data po zavření. Pokud ukládání není dostupné, stav na to upozorní.

| Formát | Co obsahuje | Použití |
|---|---|---|
| JSON | Kompletní stav, pořadí, rozpracovanou sérii, historii i zápisky | Záloha a obnova na jiném zařízení |
| CSV | Hody, hráče, trasy, poznámky a samostatné zápisky | Excel, LibreOffice; UTF-8 BOM a oddělovač středník |
| TXT | Záměry, aktuální stav, všechny zápisky a chronologii tahů | Čitelné osobní ohlédnutí |
| Tisk deníku | Deník tahů a navázané zápisky | Papír nebo PDF přes tiskový dialog prohlížeče |

Import najdete v Uložit a exportovat. JSON musí pocházet z této verze aplikace, nejvýše 5 MB. Import nahradí současnou hru, proto ji předem případně exportujte. Importní data se ověřují a uživatelské řetězce se vkládají s HTML escapováním.

Závěrečný export funguje i v nedohrané partii. Pro úplnou archivaci zvolte JSON a TXT; tiskový deník nemusí obsahovat poznámku k poli, které nebylo součástí žádného tahu.

## Soukromí

Žádná registrace hráčů a žádné odesílání záměrů na server. Všichni u stejného prohlížeče však vidí tutéž partii. Každý export zahrnuje údaje celé skupiny. Před předáním souboru se domluvte s ostatními.

## Mobil a ovládání

Na úzké obrazovce se plán posouvá vodorovně; texty proto nemusí být zmenšeny do nečitelnosti. Karty hry a výkladu pokračují pod plánem. Pole i hlavní ovládání lze vybírat klávesnicí. Respektuje se systémové omezení animací.
