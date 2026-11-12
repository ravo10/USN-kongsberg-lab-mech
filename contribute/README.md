# How this website works

This page is for whoever looks after the lab wiki next: lab supervisors, teachers and students who want to fix or add something. You do not need to know web programming. If you can edit a text file, you can edit this website.

*Norsk:* Denne siden forklarer hvordan nettsiden er bygget, og hvordan du retter eller legger til innhold. Alt innhold er tekstfiler (Markdown) i et Git-repository. Når en endring lagres i `main`, bygger GitHub nettsiden på nytt i løpet av omtrent ett minutt.

## 1. The short version

- Every page is a **Markdown file** (`.md`) in the Git repository [ravo10/USN-kongsberg-lab-mech](https://github.com/ravo10/USN-kongsberg-lab-mech). The same files are readable directly on GitHub.
- When a change is saved to the **`main`** branch, **GitHub Actions** runs **Jekyll**, which turns the Markdown into web pages, and publishes them on **GitHub Pages** at <https://ravo10.github.io/USN-kongsberg-lab-mech/>.
- This takes **about one minute**. Nothing has to be uploaded by hand.

```text
 edit a .md file ──► commit to main ──► GitHub Actions: Jekyll build ──► GitHub Pages (live site)
                                          (about 1 minute)
```

You can follow each build under the repository's **Actions** tab ("Deploy Jekyll with GitHub Pages dependencies preinstalled"). A green tick means the new version is live. A red cross means the build failed and the old version is still online; open the run to see the error.

## 2. Making a small change (no installation)

1. Open the page on the website and click **Edit** (top right). This opens the file on GitHub.
2. Click the pencil, change the text, and click **Commit changes**. Commit directly to `main`.
3. Wait a minute and reload the page.

Typos, a wrong value, a missing safety point: this is the whole job. Anyone without write access to the repository gets a "propose changes" button instead, which sends the change to the owner for review.

## 3. What the files do

| File or folder | What it is |
| --- | --- |
| `equipment/<machine>/README.md` | The guide for one machine, in English. Becomes the page `/equipment/<machine>/`. |
| `equipment/<machine>/README.no.md` | The same guide in Norwegian. Becomes `/equipment/<machine>/README.no.html`. When it exists, the page gets a **Norsk / English** switch automatically. |
| `equipment/<machine>/images/` | Photos for that guide, numbered in reading order (`01-…`, `02-…`). |
| `labs/<course>/README.md` | What happens in each lab session of a course, with protocols and report templates. |
| `_data/wiki.yml` | **The menu.** Lists the labs and machines shown in the left sidebar and as cards on the home page. Add a line here when you add a machine or a course. |
| `index.html` | The website's home page (search box, cards, "Before any lab"). |
| `README.md` (top level) | The front page **on GitHub**. Not published on the website, which uses `index.html` instead. Keep both lists of machines in step. |
| `_config.yml` | Jekyll settings: site title, plugins, which files are left out. Rarely changed. |
| `_layouts/default.html` | The frame around every page: top bar, sidebar, breadcrumbs, Edit button, "On this page" outline, footer. |
| `assets/css/site.css` | Colours, fonts and layout, including dark mode, phone layout and print. |
| `assets/js/wiki.js` | Search, the "On this page" outline and the phone menu. No external libraries. |
| `search.json` | Builds the search index from all pages at every build. Nothing to do by hand. |
| `_includes/icon.html` | The small line icons on the cards and buttons. |
| `.github/workflows/jekyll-gh-pages.yml` | The GitHub Actions job that builds and publishes the site. |
| `tools/` | Helper scripts: [export a guide to PDF and Word](../tools/export-guide/README.md) and [prepare and label photos](https://github.com/ravo10/USN-kongsberg-lab-mech/blob/main/tools/photo/photo.py). Not part of the website. |

## 4. How a Markdown file becomes a page

Jekyll and a few standard GitHub Pages plugins do the work. You only write normal Markdown.

- **`README.md` becomes the folder's page.** `equipment/furnace-heat-treatment/README.md` is shown at `/equipment/furnace-heat-treatment/`.
- **The first `#` heading becomes the page title**, used in the browser tab, the search results and the breadcrumbs.
- **Links between `.md` files keep working.** Write links to the `.md` file, for example `[MXT50 guide](../hardness-vickers-matsuzawa-mxt50/README.md)`. That link works on GitHub, and Jekyll changes it to the web page on the site.
- **`##` and `###` headings get anchors** and appear in the "On this page" outline when a page has three or more of them. The anchor is the heading in lower case, with spaces turned into `-` and most punctuation dropped: `## 4. Check the machine on the reference block` → `#4-check-the-machine-on-the-reference-block`. A dash in a heading leaves a double hyphen: `Lab 1 – Axial tensile testing` → `#lab-1--axial-tensile-testing`.
- **Photo captions:** an image on its own line, followed by a blank line and a line in italics, is shown as a centred caption:

  ```markdown
  ![Figure 3: the turret](images/03-turret.jpg)

  *Figure 3. The three turret positions.*
  ```

- **PDF and Word files** next to the Markdown are published as downloads. They are made from the Markdown with [`tools/export-guide`](../tools/export-guide/README.md), so edit the Markdown first and export again.

## 5. Common jobs

### Add or change a photo

1. Prepare it, so it is upright, 1050 px wide and has no metadata (phone photos can contain the GPS position):

   ```bash
   python tools/photo/photo.py prepare IMG_1234.jpg equipment/<machine>/images/04-control-panel.jpg
   ```

2. If buttons need numbers, write a small `labels.json` and add the yellow labels (see the instructions at the top of [`photo.py`](https://github.com/ravo10/USN-kongsberg-lab-mech/blob/main/tools/photo/photo.py)). Open the result and check that no label hides a button or its text.
3. Add it to the guide with a figure number and a caption, in both languages.

### Add a new machine

1. Copy `equipment/_template/` to `equipment/<type>-<make>-<model>/` (lower case, hyphens). The template has both `README.md` (English) and `README.no.md` (Norwegian).
2. Fill in both files and replace everything in [square brackets]. Do not use angle brackets like `<Model>` for placeholders: Markdown reads them as HTML and the page breaks.
3. Add the photos (see above).
4. Add the machine to `_data/wiki.yml` (sidebar and home page), to the table in `equipment/README.md` and to the table in the top-level `README.md`.
5. Export PDF and Word with `tools/export-guide` if the guide is finished.

In `_data/wiki.yml`, `status` decides the label on the card: `ready` (Guide), `in-progress` (In progress, with a yellow dot in the sidebar) or `external` (Linked docs). YAML is strict about indentation: use two spaces, never tabs, and copy an existing entry.

### Add a course or lab session

Make `labs/<course-code>-<course-name>/README.md` like the TSM2370 one, put protocols and templates in `protocols/`, and add the course to `_data/wiki.yml` and `labs/README.md`.

## 6. Rules for content

- **No student names or student IDs**, no sign-up lists or grades. The site is public.
- **Remove photo metadata** before adding a photo (the `prepare` step does this).
- **Posted HMS instructions** may be copied as text, citing the title, version and date. Leave out personal names.
- **Markdown is the master copy.** Never edit only the PDF or Word file.
- Third-party documents (manuals, slides from other teachers) only with permission.

## 7. Preview on your own computer (optional)

Not needed for small edits. Useful when you change the layout, the CSS or `_data/wiki.yml`.

1. Install Ruby (on Windows: [RubyInstaller](https://rubyinstaller.org/) with the Devkit).
2. In the repository folder, run once:

   ```bash
   bundle install
   ```

3. Start the preview:

   ```bash
   bundle exec jekyll serve --baseurl /USN-kongsberg-lab-mech
   ```

4. Open <http://localhost:4000/USN-kongsberg-lab-mech/>. The page reloads when you save a file (refresh the browser).

The `Gemfile` uses the same `github-pages` package as GitHub, so the preview looks like the live site.

## 8. If something goes wrong

| Problem | What to check |
| --- | --- |
| The change is not on the site | Wait a minute and reload without cache (Ctrl+F5). Check the **Actions** tab: is the latest run green? |
| The Actions run is red | Open it and read the error in "Build with Jekyll". Most often a mistake in `_data/wiki.yml` (indentation) or `_config.yml`. |
| A page shows "404" | The folder needs a `README.md`. Check the spelling of the folder name in links: GitHub Pages is case-sensitive. |
| A link jumps to the top instead of a section | The anchor does not match the heading. Open the page, hover over the heading in the "On this page" outline, and copy the anchor from there. |
| A photo does not show | Check the path and the case of the file name (`Front.JPG` is not `front.jpg`). |
| The site looks unstyled | `assets/css/site.css` failed to load: check the Actions log and that `_config.yml` was not changed by mistake. |

## 9. Settings on GitHub

These are set once, under the repository's **Settings**:

- **Pages → Build and deployment → Source:** *GitHub Actions* (the workflow above does the build).
- **About** (the ⚙ next to "About" on the repository page): description, website link and topics.
