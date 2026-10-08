# Section 61 (Desert Fox) read notes

Source: archive.org scan jp2 79-81 (printed pp. 29-31). Crops in /tmp/apwork/crops-s61/.

## OCR vs scan differences
- 61.31 Msus: OCR "84004", scan "B4004".
- 61.31 Mersa Matruh: OCR "D8714", scan "D3714".
- 61.31/61.21 etc: OCR "Ist" for "1st" throughout (1st RHA, 1st Buffs, 1st Chesire, 1st South Staffordshires, 1st Essex).
- 61.33: OCR inserts a stray line "6RTR/3rd Amr X" above the air table; not in the scan there.
- 61.33 table: scan header is "Plane / Available"; OCR drops "Plane".
- 61.34: OCR has a stray "9" (the page's truck graphic) after the Malta paragraph; 61.42 likewise has a "16" graphic.
- 61.36: OCR "Mersa Brega'" has a stray apostrophe (scan speck).
- 61.42 table: scan header "Total Available"; OCR "Available".
- 61.43 heading: OCR "Axis Tracks", scan "Axis Trucks".
- 61.6: OCR "Solium", scan "Sollum".
- 61.73 B: OCR "As in 61.72 'C'", scan prints "61.62 'C'" (OCR silently corrected it).
- 61.72 D / 61.73: OCR keeps line breaks differently; values agree.
- All numbers otherwise agree with the scan.

## Printed oddities needing a ruling
1. 61.33 places a Hurricane squadron at "Tobruk (C 4907)"; Tobruk is C4807 everywhere else.
2. 61.72 C says it replaces 61.43 (Axis trucks) and 61.72 D says it replaces 61.35 (CW trucks); the content is supply, so 61.44 and 61.36 are meant. Encoded that way.
3. 61.73 B cites 61.62 "C" (no such case); read as 61.72 C.
4. 61.73 gives no initial motorisation points; unclear whether 61.72 B applies.
5. 61.32 gives tanks to 5 RTR of the 3rd Armoured Bde, but 5 RTR is not in the 61.31 listing (only 6 RTR and 3rd Hussars are assigned). 61.38 also has "ARTR assigned" in the 4th Armd Bde, probably a misprint for a numbered RTR.
6. 61.31 assigns 6 RTR [4/7] to the 3rd Armd Bde while 61.38 says the 7th Armoured's 7th Armd Div contains 4th Armd Bde with 6 RTR "reassigned": consistent, but 7th Armoured is placed whole at Alexandria; the data relies on the 6 RTR listing at A2022 taking precedence.
7. Victory 61.8: "the player who holds Tobruk wins", then "anything less than [the Axis strategic set] is a Commonwealth victory" contradict each other for an Axis player holding Tobruk only. Also the CW "Smashing Victory" has no schema level (recorded as strategic). No supply condition printed. "Any two villages/cities in Egypt" is a count the schema cannot express (constraint string).
8. 61.31 "106th AT Regt" in Cairo: only the 106th RHA exists, filed under anti-tank regiments; mapped to unit:cw:106-rha.
9. 61.41 "2nd Artillery Ragruppament": the sheet has four battalions of 2 Arty Rgppmnto and no HQ; all four listed.
10. 61.41 "with no divison less than two hexes from another": ambiguous whether a gap of one hex (two hexes apart) is allowed.
11. 61.72 C excludes "the road from E 1716 the Maatan Groter (A 1318)": E1716 is in Egypt; surely A1716. Maaten Groter spelled two ways (61.41 "Maaten", 61.72 "Maatan").
12. 61.44: the Axis Tripoli dump has no water figure; the air-facility pool has no stores.
13. 61.1 promises a campaign scenario from the same set-up but Section 61 gives it nothing else (no end, victory, initiative). desert-fox-campaign.json extends rommels-arrival with end GT111 OpStage 3 as a placeholder; unconfirmed.
14. Spellings: "Savonna" (Savona), "Chesire", "Sidi Barrini", "Agadabia" vs "Agedabia", "shceduled", "Ragruppament".
15. R-027: Tobruk port recorded at efficiency 2, not the printed 7.

## What the schema could not express
- Italian first-line trucks (45/220/50) given out freely with no hex: put in the side trucks list with a constraint/note.
- Pools shared among several dumps with per-dump percentage caps and minimum 50: one supply block with count and a constraint string.
- "Within the triangle Tocra-Er Regima-Benghazi" and "between Ras el Ali and Nofilia": hexes as anchors plus constraint.
- German land units and planes "as scheduled before GT26 OpStage 3": no unit list; a deployment with empty units and a note.
- CW 3rd Armoured Bde tank TOE: put in special as a sentence (toe format for TOE by tank type not used).
- Release schedule (61.38): sentences only.
- Benghazi prisoners, POW camp and guard: a note on the Benghazi dump.
- Victory: no "smashing" level, no "N of a class of places" objective, no conflict resolution.
- Air and fleet blocks are free-form objects (untyped).
