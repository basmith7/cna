# Section 60 read notes (scan p76-p79)

Scan: 60.21 on p76; 60.22-60.43 on p77; 60.44-60.82 + start of 60.92 on p78; rest of 60.92 and 60.93 on p79.
Crops: /tmp/apwork/crops-s60/. Generator: /tmp/apwork/scripts/s60.py.

## OCR text vs scan
- 60.22: scan says "Victory Conditions are listed in Case 60.71"; OCR has 60.81 (link rewritten). 60.23: scan says 60.72; OCR 60.81. (SPI misprints: the conditions are at 60.81/60.82.)
- 60.31 C4218: scan "(I; Att: I(M) [T; Ar/LTC]" (paren unclosed in print too); OCR "I(M) [T; Ar/LTC" without closing bracket.
- 60.31 C4020: scan "1 Libyan Div (I)"; OCR "(DJ".
- 60.31 C3920: scan "[T; Tvl/LTC]"; OCR "Tvil/LTC)".
- 60.31 C3919: scan "Det: all except XXI)"; OCR "XX)".
- 60.31 C3918: scan "LXII(L)"; OCR "LXIICL)".
- 60.31 C4707: scan "5 heavy"; OCR "Sheavy".
- 60.31 C4507: scan "(I)"; OCR "(1)".
- 60.31 Bardia: scan "Det: II(M) and IX(L)"; OCR "IIQVW) and IX(L)".
- 60.31 el Grein: scan C1715; OCR "Ci715".
- 60.31 Map A or B: scan "XVIIILib (I; *); XXXIILib (I; *)"; OCR "(1; *)".
- 60.31 Tripoli/Tripolitania: scan "(I)"; OCR "(D" / "(D.".
- 60.33 heading: scan "Second-Third Line"; OCR "Lime".
- 60.41 C3922: scan "1st Kings"; OCR "Ist". Same "1st"/"Ist" for C3520, Matruh (1st Durham), Cairo (1st Welch, 1st Cheshire).
- 60.41 C3320: scan "(I; 7Spt/7)"; OCR "(1; ...)".
- 60.41 Matruh: scan "D3714"; OCR "13714". 4th Indian: scan "D3615"; OCR "13615".
- 60.41 Alexandria: scan "4th NZ FIeld Arty" (typo in print as "FIeld"); OCR same.
- 60.44: scan header has "(Factors" over the columns; OCR drops it.
- 60.46: scan rows read "(2 SGSU's) (12 Ready)", "(9 ready)", "(all ready)"; OCR table is a reflow, values match.
- 60.5 list (not used in JSON): scan Martuba B5526, Ztert B5917, Derna B5925, Augila B0707, Dekheila E3512; OCR "BS526", "BS5917", "BS5925", "BO707", "£3512". Scan has a blank-name airfield B5825; OCR "_ B5825".
- 60.92 B: scan "Benghazi (B 4827)"; OCR matches. Footnote: scan "Dumps 1 and 2"; OCR "Dumps | and 2". Scan "a Commonwealth unit"; OCR "aCommonwealth".
- 60.93 B/C: scan really says "As in 60.82 'B'/'C'" (SPI misprint for 60.92); OCR matches scan; read as 60.92.

## Printed oddities (scan agrees with OCR; kept as printed or noted)
- Benghazi is printed B4827 (60.31, 60.92); places.json has benghazi at A4827. I used {"place":"benghazi"}. One of the two is wrong; worth a check against the map.
- "Anywhere in Libya" line prints 4/1AR and XXI Cp twice ("...XXI Cp; XXVI Cp 4/1AR; XXI Cp (Ar)"). Listed once each; needs a ruling.
- 60.45: the text says 1 BB, 3 cruisers, 7 destroyers in total, but the lists give Alexandria 2 BB / 2 CA / 4 AA cruisers / 6 DD and Valletta 1 CA / 1 AA cruiser / 2 DD. It also gives two different movement bans (Game-Turn 2 OpStage 1 vs "September 1/IV Stage/Turn"). Both recorded in fleet as notes; needs a ruling.
- Spellings in print: Marmarcia (Marmarica), Giaribub, Maddelena, Grazianni's, Sidi Birani / Baranni, Agadabia, Stafforshires, Welch/Welsh.
- The C3922 group's first unit is printed "3rd Coldstream Gds/(I)".
- Matruh Garrison's Att list has no closing parenthesis in the print.

## Could not read / uncertain
- Nothing illegible. Unit type letters "(I)" vs "(1)" are clear in the scan as I.
- "HQ: Libyan Tank Command" and "HQ: 2nd New Zealand Division" set as alone=true (HQ counter only); this is my reading, unconfirmed.

## Schema could not express
- Placeholder unit ids: the requested "TODO-" prefix fails the unitId pattern (lowercase only), so ids are "unit:it:todo-<slug>" / "unit:cw:todo-<slug>".
- Either-or objectives (Axis strategic: Alexandria OR Cairo, any hex): no any_of-only level (all_of needs one item). Written as one objective over hexes E3613, E3714, E1730 with any_hex=true; Cairo may have more hexes than places.json's single E1730.
- Placement with two locators: "Libyan part of sheet C, not within 4 of a CW unit", "Egypt on sheet C or D", "Cairo and/or Helwan" — the extra part went into "constraint".
- Loose broken-down TOE (2 A9, 1 A10 cruiser points in Alexandria) not tied to a unit: written as an empty-units deployment with a note.
- Autoblinda 40 option (attach 2 TOE points or start them in Tobruk as replacements): a special sentence.
- Alexandria has no single place id (alexandria-east/-west); used hexes E3613+E3714. Halfaya Pass (C3922), Barce (B5504), Mechili (B4921) are not in places.json; used hexes.
- 60.93 repeats the 60.92 supply-unit blocks in its own "replaces" plus the air-facility supply units, and repeats the Alexandria/Cairo "adds", since 60.93 B/C say "as in ... B/C above and in addition".
- air, fleet: free-form objects (as the schema allows).
