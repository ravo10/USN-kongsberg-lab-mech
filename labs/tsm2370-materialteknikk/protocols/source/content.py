# Content for the TSM2370 lab documents (fall 2026). Source: v3 protocols (EN/NO).

SUP = "Rasmus Ullestad Relling"
REPO = "github.com/ravo10/USN-kongsberg-lab-mech"

# ---------------------------------------------------------------- shared EN pieces
L1_TITLE = "Lab 1: Axial Tensile Testing and Strain Measurement Accuracy"
L2_TITLE = "Lab 2: Thermal Processing and Quench Severity"

L1_OBJ = ("Determine how an unknown aluminium alloy behaves under a controlled, axial pulling load until fracture. "
          "The experiment also demonstrates why an extensometer is needed, instead of the machine's crosshead travel, "
          "to calculate strain accurately.")
L1_THEORY = ("Engineering stress (σ) is the applied axial force (F) divided by the original cross-sectional area (A₀). "
             "Engineering strain (ε) is the change in length (ΔL) divided by the original gauge length (L₀). "
             "The load cell of the universal testing machine (UTM) measures force accurately, but strain calculated from "
             "crosshead travel includes errors from the grips and the machine frame. An extensometer measures the "
             "elongation directly over the gauge length. The material goes from linear elastic deformation into plastic "
             "deformation, with strain hardening, necking and finally fracture.")
L1_FORMULAS = ["Engineering stress: σ = F / A₀", "Engineering strain: ε = ΔL / L₀", "Young's modulus: E = σ / ε  (linear elastic region)"]
L1_EQUIP = (["Device / material", "Amount / specification", "Manufacturer", "Notes"], [
    ["Universal testing machine", "10 kN (max. 5 kN grips)", "Lloyd (LR 10K)", "Axial pulling"],
    ["Camera extensometer", "1 unit", "Basler / Logitech", "Optical strain measurement"],
    ["Aluminium sheet dog-bones", "1 mm thick, 12.5 mm wide", "ISO standard", "Unknown alloy test coupons"],
    ["Digital calipers", "1 unit", "–", "For L₀, width and thickness"],
], [4.6, 4.2, 3.4, 4.4])
L1_SETUP = ("The Lloyd LR 10K is fitted with tensile grips. The camera extensometer is mounted facing the specimen and tracks "
            "optical strain markers on the gauge section. The aluminium dog-bone is centred in the grips.")
L1_STEPS = [
    "Take safety precautions and make sure the UTM safety shields are in place.",
    "Use digital calipers to measure the initial gauge length (L₀) and the width and thickness of the stamped aluminium part.",
    "Enter the measured L₀ in the extensometer software and clamp the specimen securely in the UTM grips.",
    "Start the tensile pull at the specified crosshead speed.",
    "Run the test until the specimen fractures completely.",
    "Export the raw force and elongation data from the LR 10K software.",
    "Clean the workstation and dispose of the fractured aluminium pieces safely.",
]
L1_RESULTS = (["Parameter / measurement", "Value", "Unit"], [
    ["Yield strength (machine travel)", "", "MPa"], ["Yield strength (extensometer)", "", "MPa"],
    ["Ultimate tensile strength (UTS)", "", "MPa"], ["Young's modulus (machine travel)", "", "GPa"],
    ["Young's modulus (extensometer)", "", "GPa"],
], [9.6, 4, 3])
L1_CALC = ("Calculate the yield strength, ultimate tensile strength (UTS) and Young's modulus (E) for both datasets "
           "(machine travel and extensometer). Use the results to identify the unknown aluminium alloy.")
L1_DISC = ("Discuss the difference in the linear elastic slope (E) between the two curves. Explain why the extensometer is "
           "required to get true material properties, and use the measured properties to determine the unknown aluminium alloy.")
L1_HAZ = "Pinch points in the UTM grips; sharp edges on fractured aluminium specimens."
L1_PPE = "Safety glasses, closed-toe shoes, standard lab clothing."
L1_WASTE = "Put the fractured aluminium pieces in the designated metal recycling bin."

L2_OBJ = ("Measure the local resistance to plastic deformation (Vickers hardness) of different microstructures in "
          "Sølvstål 2210 (1.2210 / 115CrV3, a high-carbon tool steel). The experiment shows how the quench medium "
          "(cold water vs. warm water or oil) and the thermal processing route decide the final mechanical properties.")
L2_THEORY_INTRO = "Hardness correlates strongly with a material's yield strength. The experiment uses two separate thermal units:"
L2_THEORY = [
    "**Primary austenitizing furnace (1000 °C):** Samples B, C and D are all first placed in the primary furnace at 1000 °C, "
    "well above the upper critical temperature. The steel matrix transforms fully into single-phase austenite (γ, FCC), "
    "and the carbon dissolves in the iron lattice.",
    "**Quenching (cold water vs. warm water or oil):** Samples B and C are cooled rapidly, directly from 1000 °C. Rapid "
    "quenching prevents carbon diffusion and forces the FCC austenite into a body-centred tetragonal (BCT) lattice: "
    "martensite, the hardest and most brittle microstructure. A 20 °C cold-water quench (Sample B) is more severe than "
    "70 °C warm water or oil (Sample C).",
    "**Isothermal annealing and air cooling (600 °C oven → ~20 °C air):** Sample D is NOT quenched in liquid. After "
    "austenitizing at 1000 °C it is moved directly to a secondary oven at 600 °C and held for 15–30 minutes. Because "
    "600 °C is well above the martensite start temperature (Ms), carbon diffuses quickly and the austenite transforms "
    "fully into soft, ductile pearlite (ferrite + cementite). When the transformation is complete, the sample is taken "
    "out and air-cooled on a heat-resistant surface to room temperature (~20 °C) for handling and hardness testing.",
]
L2_FORMULAS = ["Vickers hardness: HV = 1.8544 · F / d²", "Mean diagonal: d = (d₁ + d₂) / 2", "Units: F in kgf, d in mm. This lab uses HV1 (F = 1 kgf)."]
L2_EQUIP = (["Device / material", "Amount / specification", "Manufacturer / grade", "Notes"], [
    ["High-carbon steel blocks", "Prepared pieces (Sølvstål 2210)", "1.2210 / 115CrV3", "4 prepared samples per group"],
    ["Lab furnaces and ovens", "Primary furnace (1000 °C) and secondary oven (600 °C)", "Tinius Olsen / lab", "Austenitizing (1000 °C) and isothermal anneal (600 °C)"],
    ["Quench media stations", "20 °C water, 70 °C water, oil", "–", "Different quench severity"],
    ["Vickers hardness tester", "1 unit", "Matsuzawa (MXT50)", "HV1 (1 kgf), 15 s dwell"],
    ["Polishing equipment", "As needed", "–", "Prepare surfaces for indentation"],
], [4.0, 4.6, 3.6, 4.4])
L2_SETUP = ("Four prepared Sølvstål 2210 blocks (A, B, C, D) are handed out. The primary furnace is preheated to 1000 °C for "
            "austenitizing Samples B, C and D. The quench baths are brought to their temperatures (20 °C water and 70 °C warm "
            "water or oil). A secondary oven is preheated to 600 °C for the isothermal anneal of Sample D. Hardness is measured "
            f"on the Matsuzawa MXT50; see the equipment guide at {REPO}.")
L2_STEPS = [
    "Take safety precautions and put on heat-resistant protective equipment (gloves, tongs, face shield).",
    "**Sample A (baseline):** Measure the baseline Vickers hardness of the prepared, untreated steel block.",
    "**Sample B (cold-water quench):** Place in the 1000 °C primary furnace for full austenitization. Quench rapidly in "
    "20 °C cold water. Polish and measure the Vickers hardness.",
    "**Sample C (reduced-severity quench):** Place in the 1000 °C primary furnace for full austenitization. Quench in 70 °C "
    "warm water OR quenching oil. Polish and measure the Vickers hardness.",
    "**Sample D (600 °C isothermal anneal and air cooling):** Place in the 1000 °C primary furnace for full austenitization. "
    "Move it directly to the secondary oven at 600 °C and hold for 15–30 minutes for complete pearlite transformation. Take "
    "it out and let it air-cool on a heat-resistant surface to room temperature (~20 °C). Polish and measure the Vickers hardness.",
    "Record all hardness indentations and clear the testing equipment.",
]
L2_RESULTS = (["Parameter / measurement", "Value", "Unit"], [
    ["Sample A hardness (baseline, untreated)", "", "HV1"],
    ["Sample B hardness (1000 °C → 20 °C water quench)", "", "HV1"],
    ["Sample C hardness (1000 °C → 70 °C water / oil quench)", "", "HV1"],
    ["Sample D hardness (1000 °C → 600 °C anneal → 20 °C air)", "", "HV1"],
], [10.6, 3, 3])
L2_CALC = ("Record the Vickers hardness of all four samples in the table. If you make several indentations per sample, "
           "give the mean value.")
L2_DISC = ("Compare Sample B (cold water) and Sample C (warm water or oil) to explain quench severity and cooling rate in "
           "high-carbon tool steel. Compare Sample B (martensite) and Sample D (1000 °C → 600 °C for 15–30 min, then "
           "air-cooled) to explain how the cooling route controls the phase transformation (BCT martensite vs. pearlite) "
           "and the final hardness.")
L2_HAZ = "Extreme heat (1000 °C furnace, 600 °C oven), hot steel blocks, burns, quenching vapours and splashes."
L2_PPE = "Heat-resistant gloves, tongs, face shield, lab coat, closed-toe shoes."
L2_WASTE = "Dispose of polishing waste properly. Handle quenching fluids according to the lab's environmental guidelines."

REFS_EN = [
    "[1] Häll, K. (2026). Materials Science & Engineering: Practical Characterization. University of South-Eastern Norway.",
    "[2] USN Department of Science and Industry Systems (2026). TSM2370 Materialteknikk 2026 course material. University of South-Eastern Norway.",
    f"[3] USN Kongsberg Mechanical Engineering Lab (2026). Equipment guides (Lloyd LR 10K, Matsuzawa MXT50). {REPO}",
]


def protocol_en(title, obj, theory, formulas, equip, setup, steps, results, calc, disc):
    b = [("label", "Laboratory protocol · TSM2370 Materialteknikk"), ("title", title),
         ("info", [("Author", "[First Last Name]"), ("Student ID", "[Student ID]"), ("Course / programme", "TSM2370 Materialteknikk"),
                   ("Supervisor", SUP), ("Institution / lab", "University of South-Eastern Norway, Kongsberg"),
                   ("Experiment date", "[DD/MM/YYYY]"), ("Lab partner(s)", "[Lab partner names]")]),
         ("h1", "1. Objective"), ("p", obj),
         ("h1", "2. Theoretical background")]
    b += theory
    b += [("h2", "2.1 Relevant formulas"), ("formula", formulas),
          ("h1", "3. Materials and equipment"), ("table", *equip),
          ("h1", "4. Experimental procedure"), ("h2", "4.1 Experimental setup"), ("p", setup),
          ("h2", "4.2 Procedure"), ("ol", steps),
          ("h1", "5. Results and measurements"), ("table", *results),
          ("h2", "5.1 Calculations"), ("p", calc),
          ("h2", "5.2 Graphs / diagrams"), ("p", "[Insert diagram or figure here, with labelled axes and units. Plotting can be done in Python or Excel.]"),
          ("h1", "6. Discussion"), ("h2", "6.1 Interpretation of results"), ("p", disc),
          ("h2", "6.2 Error analysis"), ("p", "**Systematic errors:** [Error source 1]"), ("p", "**Random errors:** [Error source 1]"),
          ("h1", "7. Conclusion"), ("p", "[Summarise the most important findings and answer the question posed in the objective.]"),
          ("h1", "8. References"), ("ul", REFS_EN),
          ("h1", "9. Appendix"), ("h2", "9.1 Raw data"), ("p", "[Raw data tables or measurement sheets]"),
          ("h2", "9.2 Additional figures"), ("p", "[Further graphs, photos or sketches]"),
          ("sign", "Date", "Signature", "I hereby confirm that this protocol was written independently and truthfully.")]
    return b


def report_en(title, exp_no, theory_blocks, formulas, obj, equip, haz, ppe, waste, steps, results, disc):
    b = [("label", "Laboratory report · TSM2370 Materialteknikk"), ("title", title),
         ("info", [("Experiment title", title), ("Course / subject", "TSM2370 Materialteknikk"), ("Experiment no.", exp_no),
                   ("Date performed", "[DD/MM/YYYY]"), ("Date submitted", "[DD/MM/YYYY]"), ("Author / student name", "[First Last Name]"),
                   ("Student ID", "[Student ID]"), ("Lab partner(s)", "[Lab partner names]"), ("Instructor / TA", SUP)]),
         ("h1", "1. Abstract"),
         ("p", "[A concise summary (150–250 words) of the whole report: the purpose, the methods, the main results with key "
               "numbers, and the main conclusion. Write the abstract last, when all other sections are finished.]"),
         ("h1", "2. Introduction"), ("h2", "2.1 Background and theory")]
    b += theory_blocks
    b += [("p", "**Relevant formulas:**"), ("formula", formulas),
          ("h2", "2.2 Objectives"), ("p", obj),
          ("h2", "2.3 Hypothesis"), ("p", "[State your hypothesis or expected outcome, based on the theory.]"),
          ("h1", "3. Materials and equipment"), ("table", *equip),
          ("h1", "4. Safety considerations"), ("h2", "4.1 Hazards"), ("p", haz),
          ("h2", "4.2 Personal protective equipment (PPE)"), ("p", ppe),
          ("h2", "4.3 Waste disposal"), ("p", waste),
          ("h1", "5. Methods / procedure"), ("ol", steps),
          ("h1", "6. Results"), ("h2", "6.1 Observations"), ("p", "[Describe any qualitative observations made during the experiment.]"),
          ("h2", "6.2 Data table"), ("table", *results),
          ("h2", "6.3 Calculations"),
          ("p", "[Show one full sample calculation for each type of computation: the equation, the substituted values, and the "
                "result with correct units.]"),
          ("h2", "6.4 Figures / graphs"), ("p", "[Insert figures or graphs here. Label the axes and give the units.]"),
          ("h1", "7. Discussion"), ("h2", "7.1 Interpretation of results"), ("p", disc),
          ("h2", "7.2 Comparison with theoretical values"), ("p", "[Discuss how your values compare with theoretical or literature values.]"),
          ("h2", "7.3 Sources of error"), ("p", "**Systematic errors:** [Identify calibration or method errors]"),
          ("p", "**Random errors:** [Identify environmental or measurement scatter errors]"),
          ("h1", "8. Conclusion"), ("p", "[Summarise the most important findings and answer the question posed in the objectives.]"),
          ("h1", "9. References"), ("ul", REFS_EN),
          ("h1", "10. Appendices"), ("h2", "Appendix A – Raw data"), ("p", "[Insert raw data logs or printouts here.]"),
          ("h2", "Appendix B – Additional figures"), ("p", "[Insert additional photos or supplementary graphs here.]")]
    return b


L2_THEORY_BLOCKS = [("p", L2_THEORY_INTRO), ("ul", L2_THEORY)]

PROTOCOL_EN = (protocol_en(L1_TITLE, L1_OBJ, [("p", L1_THEORY)], L1_FORMULAS, L1_EQUIP, L1_SETUP, L1_STEPS, L1_RESULTS, L1_CALC, L1_DISC)
               + [("pagebreak",)]
               + protocol_en(L2_TITLE, L2_OBJ, L2_THEORY_BLOCKS, L2_FORMULAS, L2_EQUIP, L2_SETUP, L2_STEPS, L2_RESULTS, L2_CALC, L2_DISC))

REPORT_EN = (report_en(L1_TITLE, "1", [("p", L1_THEORY)], L1_FORMULAS, L1_OBJ, L1_EQUIP, L1_HAZ, L1_PPE, L1_WASTE, L1_STEPS, L1_RESULTS,
                       L1_DISC + " [Compare your values with literature values for common alloys, e.g. 6061-T6 and 5052-H32.]")
             + [("pagebreak",)]
             + report_en(L2_TITLE, "2", L2_THEORY_BLOCKS, L2_FORMULAS, L2_OBJ, L2_EQUIP, L2_HAZ, L2_PPE, L2_WASTE, L2_STEPS, L2_RESULTS, L2_DISC))

# ---------------------------------------------------------------- Norwegian protocol
N1_TITLE = "Lab 1: Aksial strekktesting og nøyaktighet i tøyningsmåling"
N2_TITLE = "Lab 2: Termisk behandling og bråkjølingsgrad"


def protocol_no(title, obj, theory, formulas, equip, setup, steps, results, calc, disc):
    return [("label", "Lab-protokoll · TSM2370 Materialteknikk"), ("title", title),
            ("info", [("Forfatter", "[Fornavn Etternavn]"), ("Studentnummer", "[Studentnummer]"), ("Emne / program", "TSM2370 Materialteknikk"),
                      ("Veileder", SUP), ("Institusjon / lab", "Universitetet i Sørøst-Norge, Kongsberg"),
                      ("Dato for forsøk", "[DD/MM/ÅÅÅÅ]"), ("Lab-partner(e)", "[Navn på lab-partnere]")]),
            ("h1", "1. Hensikt"), ("p", obj), ("h1", "2. Teoretisk bakgrunn")] + theory + [
            ("h2", "2.1 Relevante formler"), ("formula", formulas),
            ("h1", "3. Materialer og utstyr"), ("table", *equip),
            ("h1", "4. Fremgangsmåte"), ("h2", "4.1 Oppsett av forsøket"), ("p", setup),
            ("h2", "4.2 Trinnvis gjennomføring"), ("ol", steps),
            ("h1", "5. Resultater og målinger"), ("table", *results),
            ("h2", "5.1 Beregninger"), ("p", calc),
            ("h2", "5.2 Grafer / diagrammer"), ("p", "[Sett inn diagram eller figur her, med navn på aksene og enheter. Plotting kan gjøres i Python eller Excel.]"),
            ("h1", "6. Diskusjon"), ("h2", "6.1 Tolkning av resultater"), ("p", disc),
            ("h2", "6.2 Feilanalyse"), ("p", "**Systematiske feil:** [Feilkilde 1]"), ("p", "**Tilfeldige feil:** [Feilkilde 1]"),
            ("h1", "7. Konklusjon"), ("p", "[Oppsummer de viktigste funnene og svar på spørsmålet i hensikten.]"),
            ("h1", "8. Referanser"), ("ul", [
                "[1] Häll, K. (2026). Materials Science & Engineering: Practical Characterization. Universitetet i Sørøst-Norge.",
                "[2] Institutt for realfag og industrisystemer (2026). TSM2370 Materialteknikk 2026, kursmateriell. Universitetet i Sørøst-Norge.",
                f"[3] USN Kongsberg Mechanical Engineering Lab (2026). Utstyrsveiledninger (Lloyd LR 10K, Matsuzawa MXT50). {REPO}"]),
            ("h1", "9. Vedlegg"), ("h2", "9.1 Rådata"), ("p", "[Rådatatabeller eller måleskjemaer]"),
            ("h2", "9.2 Ekstra figurer"), ("p", "[Flere grafer, bilder eller skisser]"),
            ("sign", "Dato", "Signatur", "Jeg bekrefter at denne protokollen er skrevet selvstendig og sannferdig.")]


PROTOCOL_NO = protocol_no(
    N1_TITLE,
    "Bestemme hvordan en ukjent aluminiumslegering oppfører seg under en kontrollert, aksial strekkbelastning frem til brudd. "
    "Forsøket viser også hvorfor et ekstensometer trengs, i stedet for maskinens krysshodebevegelse, for å beregne tøyningen nøyaktig.",
    [("p", "Nominell spenning (σ) er den påførte aksiale kraften (F) delt på det opprinnelige tverrsnittsarealet (A₀). Nominell tøyning (ε) "
           "er endringen i lengde (ΔL) delt på den opprinnelige målelengden (L₀). Veiecellen i strekkmaskinen måler kraften nøyaktig, men "
           "tøyning beregnet fra krysshodebevegelsen inneholder feil fra klemmene og maskinrammen. Et ekstensometer måler forlengelsen "
           "direkte over målelengden. Materialet går fra lineær elastisk deformasjon over i plastisk deformasjon, med arbeidsherding, "
           "innsnevring og til slutt brudd.")],
    ["Nominell spenning: σ = F / A₀", "Nominell tøyning: ε = ΔL / L₀", "Elastisitetsmodul: E = σ / ε  (lineært elastisk område)"],
    (["Utstyr / materiale", "Mengde / spesifikasjon", "Produsent", "Merknader"], [
        ["Universell strekkmaskin", "10 kN (maks. 5 kN klemmer)", "Lloyd (LR 10K)", "Aksialt strekk"],
        ["Kamera-ekstensometer", "1 stk.", "Basler / Logitech", "Optisk tøyningsmåling"],
        ["Aluminiumsprøver (hundeben)", "1 mm tykk, 12,5 mm bred", "ISO-standard", "Prøver av ukjent legering"],
        ["Digitalt skyvelære", "1 stk.", "–", "For L₀, bredde og tykkelse"]], [4.6, 4.2, 3.4, 4.4]),
    "Lloyd LR 10K er utstyrt med strekk-klemmer. Kamera-ekstensometeret monteres vendt mot prøven og sporer optiske tøyningsmarkører "
    "på måleseksjonen. Aluminiumsprøven sentreres i klemmene.",
    ["Ta sikkerhetsforholdsregler og sørg for at sikkerhetsskjermene på strekkmaskinen er på plass.",
     "Bruk digitalt skyvelære til å måle opprinnelig målelengde (L₀) og bredde og tykkelse på den utstansede aluminiumsprøven.",
     "Legg inn målt L₀ i programvaren til ekstensometeret og spenn prøven godt fast i klemmene.",
     "Start strekktesten med angitt krysshodehastighet.",
     "Kjør testen til prøven bryter helt.",
     "Eksporter rådata for kraft og forlengelse fra LR 10K-programvaren.",
     "Rydd arbeidsstasjonen og kast aluminiumsbitene på en sikker måte."],
    (["Parameter / måling", "Verdi", "Enhet"], [
        ["Flytegrense (maskinbevegelse)", "", "MPa"], ["Flytegrense (ekstensometer)", "", "MPa"],
        ["Strekkfasthet (UTS)", "", "MPa"], ["Elastisitetsmodul (maskinbevegelse)", "", "GPa"],
        ["Elastisitetsmodul (ekstensometer)", "", "GPa"]], [9.6, 4, 3]),
    "Beregn flytegrense, strekkfasthet (UTS) og elastisitetsmodul (E) for begge datasettene (maskinbevegelse og ekstensometer). "
    "Bruk resultatene til å identifisere den ukjente aluminiumslegeringen.",
    "Diskuter forskjellen i den lineære elastiske stigningen (E) mellom de to kurvene. Forklar hvorfor ekstensometeret er nødvendig for å "
    "få sanne materialegenskaper, og bruk de målte egenskapene til å bestemme den ukjente aluminiumslegeringen.",
) + [("pagebreak",)] + protocol_no(
    N2_TITLE,
    "Måle lokal motstand mot plastisk deformasjon (Vickers-hardhet) i ulike mikrostrukturer i Sølvstål 2210 (1.2210 / 115CrV3, et "
    "høykarbon verktøystål). Forsøket viser hvordan bråkjølingsmediet (kaldt vann vs. varmt vann eller olje) og den termiske "
    "behandlingen bestemmer de endelige mekaniske egenskapene.",
    [("p", "Hardhet korrelerer sterkt med et materiales flytegrense. Forsøket bruker to adskilte termiske enheter:"),
     ("ul", [
         "**Hovedovn for austenitisering (1000 °C):** Prøve B, C og D plasseres alle først i hovedovnen på 1000 °C, godt over øvre kritiske "
         "temperatur. Stålmatrisen omdannes helt til én-fase austenitt (γ, FCC), og karbonet løses opp i jerngitteret.",
         "**Bråkjøling (kaldt vann vs. varmt vann eller olje):** Prøve B og C kjøles raskt, direkte fra 1000 °C. Rask bråkjøling hindrer "
         "karbondiffusjon og tvinger FCC-austenitten over i et romsentrert tetragonalt (BCT) gitter: martensitt, den hardeste og mest "
         "sprø mikrostrukturen. Et 20 °C kaldtvannsbad (prøve B) gir kraftigere bråkjøling enn 70 °C varmt vann eller olje (prøve C).",
         "**Isoterm gløding og luftavkjøling (600 °C-ovn → ~20 °C luft):** Prøve D bråkjøles IKKE i væske. Etter austenitisering ved "
         "1000 °C flyttes den direkte til en sekundærovn på 600 °C og holdes der i 15–30 minutter. Fordi 600 °C er godt over "
         "martensitt-starttemperaturen (Ms), diffunderer karbonet raskt, og austenitten omdannes helt til myk, duktil perlitt "
         "(ferritt + sementitt). Når omdanningen er ferdig, tas prøven ut og luftavkjøles på et varmebestandig underlag til "
         "romtemperatur (~20 °C) for håndtering og hardhetsmåling."])],
    ["Vickers-hardhet: HV = 1,8544 · F / d²", "Middeldiagonal: d = (d₁ + d₂) / 2", "Enheter: F i kgf, d i mm. Denne laben bruker HV1 (F = 1 kgf)."],
    (["Utstyr / materiale", "Mengde / spesifikasjon", "Produsent / kvalitet", "Merknader"], [
        ["Høykarbon stålblokker", "Klargjorte biter (Sølvstål 2210)", "1.2210 / 115CrV3", "4 klargjorte prøver per gruppe"],
        ["Laboratorieovner", "Hovedovn (1000 °C) og sekundærovn (600 °C)", "Tinius Olsen / lab", "Austenitisering (1000 °C) og isoterm gløding (600 °C)"],
        ["Stasjoner for bråkjøling", "20 °C vann, 70 °C vann, olje", "–", "Ulik bråkjølingsgrad"],
        ["Vickers hardhetsmåler", "1 stk.", "Matsuzawa (MXT50)", "HV1 (1 kgf), 15 s holdetid"],
        ["Poleringsutstyr", "Etter behov", "–", "Klargjøre overflaten for inntrykk"]], [4.0, 4.6, 3.6, 4.4]),
    "Fire klargjorte blokker av Sølvstål 2210 (A, B, C, D) deles ut. Hovedovnen forvarmes til 1000 °C for austenitisering av prøve B, C "
    "og D. Bråkjølingsbadene bringes til riktig temperatur (20 °C vann og 70 °C varmt vann eller olje). En sekundærovn forvarmes til "
    f"600 °C for isoterm gløding av prøve D. Hardheten måles på Matsuzawa MXT50; se utstyrsveiledningen på {REPO}.",
    ["Ta sikkerhetsforholdsregler og ta på varmebestandig verneutstyr (hansker, tenger, ansiktsskjerm).",
     "**Prøve A (referanse):** Mål referansehardheten (Vickers) på den klargjorte, ubehandlede stålblokken.",
     "**Prøve B (bråkjøling i kaldt vann):** Plasser prøven i hovedovnen på 1000 °C for full austenitisering. Bråkjøl raskt i 20 °C kaldt "
     "vann. Poler og mål Vickers-hardheten.",
     "**Prøve C (redusert bråkjøling):** Plasser prøven i hovedovnen på 1000 °C for full austenitisering. Bråkjøl i 70 °C varmt vann ELLER "
     "bråkjølingsolje. Poler og mål Vickers-hardheten.",
     "**Prøve D (isoterm gløding ved 600 °C og luftavkjøling):** Plasser prøven i hovedovnen på 1000 °C for full austenitisering. Flytt den "
     "direkte til sekundærovnen på 600 °C og hold i 15–30 minutter for fullstendig perlittomdanning. Ta den ut og la den luftavkjøles på et "
     "varmebestandig underlag til romtemperatur (~20 °C). Poler og mål Vickers-hardheten.",
     "Noter alle hardhetsmålinger og rydd testutstyret."],
    (["Parameter / måling", "Verdi", "Enhet"], [
        ["Prøve A hardhet (referanse, ubehandlet)", "", "HV1"],
        ["Prøve B hardhet (1000 °C → 20 °C vann)", "", "HV1"],
        ["Prøve C hardhet (1000 °C → 70 °C vann / olje)", "", "HV1"],
        ["Prøve D hardhet (1000 °C → 600 °C gløding → 20 °C luft)", "", "HV1"]], [10.6, 3, 3]),
    "Noter Vickers-hardheten for alle fire prøvene i tabellen. Lager du flere inntrykk per prøve, oppgi middelverdien.",
    "Sammenlign prøve B (kaldt vann) og prøve C (varmt vann eller olje) for å forklare bråkjølingsgrad og kjølehastighet i høykarbon "
    "verktøystål. Sammenlign prøve B (martensitt) og prøve D (1000 °C → 600 °C i 15–30 min, så luftavkjølt) for å forklare hvordan "
    "kjøleveien styrer faseomdanningen (BCT-martensitt vs. perlitt) og den endelige hardheten.",
)

DOCS = {
    "lab-protocol-2026-en": dict(title="TSM2370 Lab protocols 2026 (English)", header="TSM2370 Materialteknikk · Lab protocol · Fall 2026",
                                 page="Page", of="of", blocks=PROTOCOL_EN),
    "lab-protocol-2026-no": dict(title="TSM2370 Lab-protokoller 2026 (norsk)", header="TSM2370 Materialteknikk · Lab-protokoll · Høst 2026",
                                 page="Side", of="av", blocks=PROTOCOL_NO),
    "lab-report-template-2026-en": dict(title="TSM2370 Lab report template 2026", header="TSM2370 Materialteknikk · Lab report · Fall 2026",
                                        page="Page", of="of", blocks=REPORT_EN),
}
