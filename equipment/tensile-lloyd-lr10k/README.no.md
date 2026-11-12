# Lloyd LR 10K – Universal strekkmaskin

> **English version:** [README.md](README.md) · **Hurtigkort (A4, til laminering ved maskinen):** [norsk](quick-card-no.pdf) · [engelsk](quick-card-en.pdf)

Lloyd LR 10K (1990-tallet, 10 kN) brukes til strekk-, trykk- og trepunkts bøyeprøving, blant annet i TSM2370 Lab 1 (aksial strekktesting av aluminium med optisk ekstensometer).

Maskinen styres fra en PC med **LR 10K Control Software**, som har eget repository og egen dokumentasjon: [ravo10/lr10k-2027](https://github.com/ravo10/lr10k-2027). Dokumentasjonen der er på engelsk; det viktigste står på norsk under.

**Brukes i:** [TSM2370 Lab 1 – Axial tensile testing and strain measurement accuracy](../../labs/tsm2370-materialteknikk/README.md#lab-1--axial-tensile-testing-and-strain-measurement-accuracy)

## Sikkerhet (kortversjon)

- En strekkmaskin kan klemme fingre, og prøver kan ryke voldsomt. **Hold hendene unna klemmene** når traversen kan gå.
- **Kjenn maskinens egen stoppknapp** og ha den innen rekkevidde under hver test. *Stop* (F1) i programmet virker bare når PC-en, kabelen og programmet virker.
- **Bruk vernebriller**, særlig ved sprø prøver og kompositter.
- **Avlast før du tar ut prøven:** *Return to zero point* (F5).
- Sperren på 50 N (når traversen kjøres uten test) og lastgrensen virker gjennom programmet. De er en ekstra sikring, ikke en erstatning for maskinens egne grenser eller for å følge med på testen.
- Sjekk resultatene før du bruker dem. Programmet er et studentprosjekt ved USN, ikke laget eller støttet av Lloyd Instruments eller AMETEK.

Hele sikkerhetsavsnittet (engelsk) står i [programvarens README](https://github.com/ravo10/lr10k-2027#safety).

## Slik kjører du en strekktest

Tallene følger *Quick start* i programvarens README og hurtigkortet.

**1. Koble til.** Slå på maskinen, sett i seriekabelen (via USB-serieadapteren) og start programmet. *PC Config.* → velg COM-porten til LR 10K → *Connect PC*. Status vises til høyre i menylinjen.

**2. Still inn testen.** I *Settings*: strekk eller trykk, test- og kjørehastighet, prøvens mål (tykkelse og bredde, eller diameter, og målelengde L0), enheter og lastgrense. Trykk **Apply to LR 10K**. Velg mappe for resultatene: *File* → *Specify Storage Folder*.

**3. Spenn fast prøven.** Kjør traversen med *Up*/*Down* (F2/F3, hold F4 for fort) til prøven sitter i begge klemmene **uten last**. Trykk **Set zero point** (F6).

**4. Optisk ekstensometer** (hopp over uten kamera):

- To runde, grønne prikker (Ø5 mm, #00FF00, matt papir) **60 mm fra hverandre** på prøvens senterlinje, satt på med plasseringsmalen og limt flatt.
- *View* → *Extensometer*, slå på kameraet, trykk **Pick from image** og klikk midt på en prikk.
- Skriv inn **L0** = målt avstand mellom prikkene. *Tracking* skal vise **2 markers**.
- Jevnt lys, ingen refleksjoner, og ikke rør kameraet eller holderen under testen. Mistes prikkene i et halvt sekund, settes testen på pause.

**5. Kjør testen.** **Start Test** (F7). *Pause* (F9) og fortsett (F7) ved behov, **End Test** (F8) etter brudd. Testen stopper også selv ved lastgrensen.

**6. Sjekk resultatene.** Programmet plasserer UTS, grensene for E-modulen og flytegrensen (Rp0,2) automatisk. Se over dem, og flytt eller legg til punkter med Ctrl+klikk. Beregn materialegenskapene i *Calculator* for å se grafen for sann spenning. Uten ekstensometer blir E-modulen for lav, fordi maskinen og klemmene også strekkes.

**7. Lagre.** Ctrl+S lagrer testen (`.lr10k`, kan åpnes igjen) og Excel-boken (`.xlsx`).

**8. Avslutt.** *Return to zero point* (F5), ta ut prøven, og *+ New Test* for neste prøve.

## Hurtigtaster

| Tast | Uten test | Under test | Testen på pause |
| --- | --- | --- | --- |
| F1 | Stopp traversen | | |
| F2 / F3 | Opp / ned | | |
| F4 (hold) | Fort, i retningen til F2/F3 | | |
| F5 | Tilbake til nullpunktet | | |
| F6 | Sett nullpunkt | | |
| F7 | Start test | | Fortsett testen |
| F8 | | Avslutt test | Avslutt test |
| F9 | | Pause | |

Ctrl+S lagrer, Ctrl+O åpner en test, og Ctrl+Z fjerner det siste punktet du satte.

## Feilsøking

| Problem | Prøv dette |
| --- | --- |
| *Start Test* er grå | Hold musepekeren over knappen: verktøytipset sier hva som mangler. |
| Kobler ikke til | Sjekk kabelen og COM-porten. *Disconnect COM* og koble til igjen. |
| «Connection lost» | Adapteren er dratt ut eller driveren startet på nytt. Sett den i igjen og trykk *Reconnect*. |
| Ekstensometeret finner bare 1 prikk | *Pick from image* på en prikk igjen med prøven på plass og laboratorielyset på. Jevnere lys, og sjekk at begge prikkene er i bildet. |
| E-modulen er for lav | Normalt uten ekstensometer: maskinen og klemmene strekkes også. Bruk ekstensometeret når du trenger E-modulen. |

## Her finner du mer (engelsk)

| Du vil … | Les |
| --- | --- |
| Få oversikt over programmet og laste det ned | [LR 10K Control Software – README](https://github.com/ravo10/lr10k-2027#readme) |
| Kjøre en test trinn for trinn (oppsett, hurtigtaster, punkter, lagring, problemer) | [Brukerveiledning](https://github.com/ravo10/lr10k-2027/blob/main/docs/index.md) |
| Lage og sette på ekstensometerprikkene | [Markørveiledning](https://github.com/ravo10/lr10k-2027/blob/main/docs/extensometer-markers.md) |
| Sette opp webkamera-ekstensometeret og den 3D-printede holderen | [Foreslått ekstensometeroppsett](https://github.com/ravo10/lr10k-2027/blob/main/docs/extensometer-setup.md) |
| Forstå Excel-rapporten | [Brukerveiledning – Saving](https://github.com/ravo10/lr10k-2027/blob/main/docs/index.md#saving-a-successfully-completed-test--excel) |
| Øve uten maskinen | I programmet: *GUI Settings* › *LR 10K Simulation* › *Activate* |
