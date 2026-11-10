# Lab sessions

Each course has a folder with its lab sessions: what you will do, which equipment you will use, and the protocol and report template you need. The equipment guides themselves live in [`equipment/`](../equipment/) and are linked from each lab.

*Norsk:* Hvert emne har en mappe med labøvingene sine: hva dere skal gjøre, hvilket utstyr dere bruker, og protokollen og rapportmalen dere trenger. Veiledningene for utstyret ligger i [`equipment/`](../equipment/) og er lenket fra hver lab.

| Course | Semester | Labs |
| --- | --- | --- |
| [TSM2370 Materialteknikk](tsm2370-materialteknikk/README.md) | Fall 2026 | Lab 1: Axial tensile testing · Lab 2: Thermal processing and quench severity |

## General templates

- [Laboratory protocol template (Word)](_templates/laboratory-protocol-template.docx): a blank protocol with the standard sections (objective, theory, materials and equipment, procedure, results, discussion, conclusion, references, appendix).

## Adding a course or a lab

1. Make a folder `labs/<course-code>-<course-name>/` with a `README.md` like the TSM2370 one.
2. Put protocols and report templates in a `protocols/` subfolder. Add a PDF next to every Word file so students can read it in the browser.
3. Link each piece of equipment to its guide in `equipment/`. If the equipment has no guide yet, add a placeholder folder for it (see [`equipment/_template`](../equipment/_template/README.md)).
4. Add the course to the table above.

Do not upload sign-up lists, grades or anything else with student names or student IDs. The repository is meant to be readable by everyone in the course.
