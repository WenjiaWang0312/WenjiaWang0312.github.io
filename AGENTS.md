# Repository Guidelines

## Site Purpose
This repository is a personal academic homepage. Optimize for accurate research content, clear project presentation, stable URLs, and strong readability on desktop and mobile. Treat the homepage as a research landing page, not a generic blog or template demo.

## Default Editing Strategy
Prefer content edits over theme refactors. For routine updates, edit `_pages/`, `_publications/`, `_talks/`, `_teaching/`, `projects/`, `files/`, and `assets/publications/`. Only change `_layouts/`, `_includes/`, `_sass/`, or `assets/js/` when the request truly requires shared layout, styling, or behavior changes.

## Key Paths
Core pages live in `_pages/`. Research collections live in `_publications/`, `_talks/`, `_teaching/`, `_portfolio/`, and `_posts/`. Standalone project microsites live in `projects/<slug>/`. Source JavaScript lives in `assets/js/_main.js`; `assets/js/main.min.js` is generated. CV source is `_pages/cv.md`, with optional JSON output in `_data/cv.json`.

## Homepage Rules
`_pages/about.md` is the homepage. Keep it concise and high-signal. News should stay milestone-driven, not diary-like. Featured papers should highlight representative work rather than exhaustively listing everything. When adding a strong new paper or project, check whether the homepage should also be updated.

## Content Sync Rules
- New publication: add `_publications/YYYY-MM-DD-slug.md`, add a teaser image in `assets/publications/`, and verify `paperurl`, `pdfurl`, `weburl`, and `header.teaser`.
- New project: add `projects/<slug>/index.html` with local assets, then link it from the matching publication or homepage when relevant.
- CV updates: edit `_pages/cv.md`. Only run `bash scripts/update_cv_json.sh` if `/cv-json/` is in use or the user asks to maintain the JSON CV.
- Generated assets: rebuild `assets/js/main.min.js` with `npm run build:js` after changing `assets/js/**`.

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
