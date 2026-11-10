# USN Kongsberg – Mechanical Engineering Lab

Instructions for the lab equipment used in mechanical engineering courses at the University of South-Eastern Norway (USN), campus Kongsberg. Each machine has its own folder with a step-by-step guide, labelled photos and a printable quick card.

*Norsk:* Instruksjoner for laboratorieutstyret i maskinfagene ved USN Kongsberg. Hver maskin har sin egen mappe med veiledning, bilder og et hurtigkort for utskrift. Veiledningene finnes på både engelsk og norsk.

## Equipment

| Equipment | Used in | Guide | Quick card |
| --- | --- | --- | --- |
| **Matsuzawa MXT50** Vickers microhardness tester | TSM2370 Lab 2 (heat treatment of AISI 1045) | [English](equipment/hardness-vickers-matsuzawa-mxt50/README.md) · [Norsk](equipment/hardness-vickers-matsuzawa-mxt50/README.no.md) · PDF: [EN](equipment/hardness-vickers-matsuzawa-mxt50/guide-en.pdf), [NO](equipment/hardness-vickers-matsuzawa-mxt50/guide-no.pdf) | [A4, norsk](equipment/hardness-vickers-matsuzawa-mxt50/quick-card-no.pdf) |
| **Lloyd LR 10K** universal testing machine (tensile, compression, 3-point bending) | TSM2370 Lab 1 (tensile testing) | [Overview and links](equipment/tensile-lloyd-lr10k/README.md) · software and user guide in [ravo10/lr10k-2027](https://github.com/ravo10/lr10k-2027) | – |

## Before any lab

- Read the guide for the machine **before** the lab session, and bring it (on paper or a screen).
- Follow the safety rules at the top of each guide. If something looks wrong or broken, **stop and tell the lab supervisor**. Do not try to repair equipment yourself.
- Leave the machine as you found it: switched off, cleaned, batteries and lights on charge.

## Repository layout

```
equipment/
├── hardness-vickers-matsuzawa-mxt50/
│   ├── README.md          guide (English)
│   ├── README.no.md       guide (Norwegian)
│   ├── guide-en.pdf       printable guide
│   ├── guide-no.pdf
│   ├── quick-card-no.pdf  one-page card to laminate and keep at the machine
│   └── images/            labelled photos used in the guides
├── tensile-lloyd-lr10k/
│   └── README.md          overview, links to the LR 10K software documentation
└── _template/
    └── README.md          starting point for a new machine
```

## Adding a new machine

1. Copy `equipment/_template/` to `equipment/<type>-<make>-<model>/` (lower case, hyphens), for example `equipment/impact-charpy-<make>-<model>/`.
2. Fill in `README.md` (English) and `README.no.md` (Norwegian). Keep the same section order as the existing guides so students know where to look.
3. Put photos in `images/`, numbered in the order they appear (`01-front-view.jpg`, …). Label buttons with numbers that match a parts table in the guide.
4. Add the machine to the **Equipment** table above.

The Markdown files are the master copies. The PDFs are exported from them, so update the Markdown first and export the PDFs again.

## Contact

Lab supervisor: Rasmus Ullestad Relling, USN Kongsberg.
