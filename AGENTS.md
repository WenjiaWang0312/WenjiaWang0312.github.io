# Repository Guidelines

## Site Purpose
This repository is a personal academic homepage. Optimize for accurate research content, clear project presentation, stable URLs, and strong readability on desktop and mobile. Treat the homepage as a research landing page, not a generic blog or template demo.

## Default Editing Strategy
Prefer content edits over theme refactors. For routine updates, edit `_pages/`, `_publications/`, `_talks/`, `_teaching/`, `projects/`, `files/`, and `assets/publications/`. Only change `_layouts/`, `_includes/`, `_sass/`, or `assets/js/` when the request truly requires shared layout, styling, or behavior changes.

## Key Paths
Core pages live in `_pages/`. Research collections live in `_publications/`, `_talks/`, `_teaching/`, `_portfolio/`, and `_posts/`. Standalone project microsites live in `projects/<slug>/`. Source JavaScript lives in `assets/js/_main.js`; `assets/js/main.min.js` is generated.

CV is JSON-driven:
- Route: `/cv/` comes from `_pages/cv.md` (wrapper) and renders `_includes/cv-template.html` using `_data/cv.json`.
- Styles: JSON CV styles live in `_sass/layout/_json_cv.scss`.

## Homepage Rules
`_pages/about.md` is the homepage. Keep it concise and high-signal. News should stay milestone-driven, not diary-like. Featured papers should highlight representative work rather than exhaustively listing everything. When adding a strong new paper or project, check whether the homepage should also be updated.

## Homepage Conventions (Current)
These are local conventions used by the current homepage implementation. Prefer following them over redesigning.

- Section order (top to bottom): `Recent News` -> `Selected Papers` -> `Research Scope` -> `Openings / Collaboration` -> `Academic Services`.
- Section styling: do not use colored "card" blocks for sections. Use divider lines between large sections (thicker) and keep the background clean.
- Recent News tags: display a short bracket tag (e.g., `[Open Source]`, `[Accept]`, `[Project Page]`, `[Preprint]`) using the shared `home-news-tag` pill style.
- Tag variants: for consistent light color-coding, always add one variant class:
  - `home-news-tag--accept`, `home-news-tag--preprint`, `home-news-tag--open-source`, `home-news-tag--project`, `home-news-tag--award`, `home-news-tag--other`.
- Reuse: use the exact same tag markup and classes on both `/` and `/news/` so the styles remain consistent.
- Selected Papers layout: use a compact horizontal row layout similar to publications (teaser on the left, text on the right). Keep it minimal:
  - Title (links to the project page).
  - Venue/year displayed to the right of the title.
  - One-sentence contribution/summary.
  - Do not include extra `Project / arXiv / GitHub` link rows inside Selected Papers unless explicitly requested.
- Selected Papers separators: use subtle thin dividers between items, but keep enough vertical spacing so dividers do not visually collide with teaser images.
- Research Scope text: the detailed Real2Sim/Sim2Real explanatory paragraphs may be commented out when the homepage is kept ultra concise.
- Collaboration tone: prefer humble phrasing such as "Our group is open to research collaborations and student projects ..." rather than overly direct self-promotion.

## News Page Conventions
`_pages/news.md` should mirror the homepage tagging scheme and present news as a simple timeline.

- Sort: list items in reverse chronological order (newest first).
- Tags: each bullet should include a bracket tag (using `home-news-tag` plus a `home-news-tag--*` variant) and keep dates explicit (e.g., `Mar 10, 2026`).
- Visual: keep tag colors light/subtle; all news items should still read as one unified list rather than separate colored categories.

## Publications Conventions
- List layout: remove "card" backgrounds. Use thin dividers between papers and thicker dividers between years.
- Detail pages: publication detail pages should show meaningful fields (teaser, authors, venue/year, links, abstract/citation). If a detail page is empty, improve the template/fields rather than keeping a blank landing page.

## Content Sync Rules
- New publication: add `_publications/YYYY-MM-DD-slug.md`, add a teaser image in `assets/publications/`, and verify `paperurl`, `pdfurl`, `weburl`, and `header.teaser`.
- New project: add `projects/<slug>/index.html` with local assets, then link it from the matching publication or homepage when relevant.
- CV updates: update structured CV content in `_data/cv.json`. Keep `/cv/` aligned with the standard archive content column (left-aligned, not a centered narrow column), so it visually matches `/publications/`.
- Generated assets: rebuild `assets/js/main.min.js` with `npm run build:js` after changing `assets/js/**`.

## Project Media Conventions (Video Covers)
Project microsites often use HTML5 `<video poster="...">` previews. To keep naming consistent:

- Cover naming: for a video file `some_video.mp4`, the cover image should be `some_video_cover.jpg`.
- Location: the cover image should live in the same folder as the video file (relative to the microsite `index.html`).
- Prefer generating covers via `ffmpeg` (scriptable and reproducible) rather than relying on browser "first frame" behavior.

## Local Development Conventions
- Internal links: do not build internal links by hard-coding `site.url` for local preview. Localhost navigation should stay on localhost; only use absolute URLs in production builds.

## Writing Style
Use short, factual academic prose. Prefer concise summaries over promotional language. Homepage sections should scan quickly. Publication blurbs should emphasize the contribution and venue. Keep filenames and permalinks lowercase and use 2-space indentation in YAML, HTML, SCSS, and site JavaScript.

## Validation Checklist
Run `bundle exec jekyll build --destination ./_site` before finishing. Use `./preview.sh` for manual review when layout or content changes are visible. Check `/`, `/publications/`, `/projects/`, and `/cv/`; verify image paths, PDF links, external links, and mobile layout. Run `npm install` once per environment and `npm run build:js` when JavaScript changes.

## Change Safety
Do not change existing permalinks unless explicitly requested. Do not move files in `files/` or image assets without updating all references. Do not edit generated files by hand when a source file exists. Do not update homepage callouts without checking the matching collection or project page.

## When To Ask
Ask before changing navigation structure, deleting pages or assets, renaming URLs, removing optional features such as `/cv-json/`, or making major homepage redesigns. If a request could be handled either by a local page edit or a shared theme refactor, prefer the local edit unless the user wants a site-wide change.

## Commit Guidelines
Use short imperative commit messages such as `Add EmbodMocap project page` or `Update homepage featured papers`. Keep each commit scoped to one logical change.
