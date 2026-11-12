# USN Kongsberg – Mechanical Engineering Lab

Lab sessions and equipment instructions for mechanical engineering courses at the University of South-Eastern Norway (USN), campus Kongsberg. **Labs** tell you what to do in each lab session and hold the protocols and report templates. **Equipment** has one folder per machine, with a step-by-step guide, labelled photos and a printable quick card.

*Norsk:* Labøvinger og utstyrsveiledninger for maskinfagene ved USN Kongsberg. Under **Labs** finner dere hva dere skal gjøre i hver labøving, med protokoller og rapportmaler. Under **Equipment** har hver maskin sin egen mappe med veiledning, bilder og hurtigkort. Veiledningene finnes på både engelsk og norsk.

> **Website:** [ravo10.github.io/USN-kongsberg-lab-mech](https://ravo10.github.io/USN-kongsberg-lab-mech/) · **Source:** [github.com/ravo10/USN-kongsberg-lab-mech](https://github.com/ravo10/USN-kongsberg-lab-mech)

## Labs

| Course | Semester | Labs | Protocol and template |
| --- | --- | --- | --- |
| [TSM2370 Materialteknikk](labs/tsm2370-materialteknikk/README.md) | Fall 2026 | [Lab 1: Axial tensile testing](labs/tsm2370-materialteknikk/README.md#lab-1--axial-tensile-testing-and-strain-measurement-accuracy) · [Lab 2: Thermal processing and quench severity](labs/tsm2370-materialteknikk/README.md#lab-2--thermal-processing-and-quench-severity) | Protocol: [EN](labs/tsm2370-materialteknikk/protocols/lab-protocol-2026-en.pdf), [NO](labs/tsm2370-materialteknikk/protocols/lab-protocol-2026-no.pdf) · Report template: [EN](labs/tsm2370-materialteknikk/protocols/lab-report-template-2026-en.docx), [NO](labs/tsm2370-materialteknikk/protocols/lab-report-template-2026-no.docx) |

All courses: [labs/](labs/README.md)

## Equipment

All machines: [equipment/](equipment/README.md)

| Equipment | Used in | Guide | Quick card |
| --- | --- | --- | --- |
| **Matsuzawa MXT50** Vickers microhardness tester | TSM2370 Lab 2 (heat treatment of Sølvstål 2210) | [English](equipment/hardness-vickers-matsuzawa-mxt50/README.md) · [Norsk](equipment/hardness-vickers-matsuzawa-mxt50/README.no.md) · PDF: [EN](equipment/hardness-vickers-matsuzawa-mxt50/guide-en.pdf), [NO](equipment/hardness-vickers-matsuzawa-mxt50/guide-no.pdf) · Word: [EN](equipment/hardness-vickers-matsuzawa-mxt50/guide-en.docx), [NO](equipment/hardness-vickers-matsuzawa-mxt50/guide-no.docx) | A4: [EN](equipment/hardness-vickers-matsuzawa-mxt50/quick-card-en.pdf), [NO](equipment/hardness-vickers-matsuzawa-mxt50/quick-card-no.pdf) |
| **Lloyd LR 10K** universal testing machine (tensile, compression, 3-point bending) | TSM2370 Lab 1 (tensile testing) | [English](equipment/tensile-lloyd-lr10k/README.md) · [Norsk](equipment/tensile-lloyd-lr10k/README.no.md) · software and user guide in [ravo10/lr10k-2027](https://github.com/ravo10/lr10k-2027) | A4: [EN](equipment/tensile-lloyd-lr10k/quick-card-en.pdf), [NO](equipment/tensile-lloyd-lr10k/quick-card-no.pdf) |
| **Nabertherm lab furnaces** (up to 1000 °C) and quenching stations | TSM2370 Lab 2 | [English](equipment/furnace-heat-treatment/README.md) · [Norsk](equipment/furnace-heat-treatment/README.no.md) | – |
| **Grinding and polishing machines** (Buehler MetaServ 250, Metaserv, Ecomet I) | TSM2370 Lab 2 | [English](equipment/polisher-metallographic/README.md) · [Norsk](equipment/polisher-metallographic/README.no.md), machines and controls; procedure in progress | – |
| **Stepcraft M700** CNC mill (UCCNC, SolidWorks CAM, 3D Touch Probe) | Student projects (prototype lab) | [Norsk](equipment/cnc-stepcraft-m700/README.no.md) · [English](equipment/cnc-stepcraft-m700/README.md) · PDF: [NO](equipment/cnc-stepcraft-m700/guide-no.pdf), [EN](equipment/cnc-stepcraft-m700/guide-en.pdf) · Word: [NO](equipment/cnc-stepcraft-m700/guide-no.docx), [EN](equipment/cnc-stepcraft-m700/guide-en.docx) | – |

## Before any lab

- Read the guide for the machine **before** the lab session, and bring it (on paper or a screen).
- Follow the safety rules at the top of each guide. If something looks wrong or broken, **stop and tell the lab supervisor**. Do not try to repair equipment yourself.
- Leave the machine as you found it: switched off, cleaned, batteries and lights on charge.

## Repository layout

```
labs/
├── README.md              list of courses + how to add a lab
├── _templates/            general templates (blank lab protocol)
└── tsm2370-materialteknikk/
    ├── README.md          the lab sessions, equipment used, links to guides
    └── protocols/         protocol and report template (Word + PDF)

equipment/
├── README.md              list of all machines
├── hardness-vickers-matsuzawa-mxt50/
│   ├── README.md          guide (English)
│   ├── README.no.md       guide (Norwegian)
│   ├── guide-en.pdf       printable guide
│   ├── guide-no.pdf
│   ├── guide-en.docx      editable Word versions
│   ├── guide-no.docx
│   ├── quick-card-en.pdf  one-page card to laminate and keep at the machine (QR code to the guide)
│   ├── quick-card-no.pdf
│   ├── quick-card-*.html  source of the quick cards (print to A4 PDF, no margins)
│   └── images/            labelled photos used in the guides
├── tensile-lloyd-lr10k/
│   ├── README.md          overview, links to the LR 10K software documentation
│   ├── README.no.md       the same in Norwegian, with the test steps and hotkeys
│   └── quick-card-*.pdf   one-page cards (EN/NO) with QR code, source in quick-card-*.html
├── furnace-heat-treatment/    Nabertherm furnaces and quenching (EN/NO)
├── cnc-stepcraft-m700/       CNC mill: SolidWorks CAM, UCCNC, probe (NO master, EN translation)
├── polisher-metallographic/   grinding and polishing machines (EN/NO), procedure in progress
└── _template/
    └── README.md          starting point for a new machine

tools/
├── export-guide/          script that exports a guide's Markdown to PDF and Word
└── photo/                 script that prepares and labels photos

contribute/README.md       how the website is built and how to change it
```

## Adding a new machine

See [How this website works](contribute/README.md) for how the website is built, how to add photos and how to preview changes.


1. Copy `equipment/_template/` to `equipment/<type>-<make>-<model>/` (lower case, hyphens), for example `equipment/impact-charpy-<make>-<model>/`.
2. Fill in `README.md` (English) and `README.no.md` (Norwegian). Keep the same section order as the existing guides so students know where to look.
3. Put photos in `images/`, numbered in the order they appear (`01-front-view.jpg`, …). Label buttons with numbers that match a parts table in the guide.
4. Add the machine to the **Equipment** table above and to the table in [`equipment/README.md`](equipment/README.md).
5. Add it to [`_data/wiki.yml`](_data/wiki.yml), which builds the website's sidebar and the cards on the website's home page.

The Markdown files are the master copies. The PDF and Word files are exported from them, so update the Markdown first and export them again with [`tools/export-guide`](tools/export-guide/README.md):

```bash
python tools/export-guide/export.py equipment/<folder>
```

## Contact

Lab supervisor: Rasmus Ullestad Relling, USN Kongsberg.
