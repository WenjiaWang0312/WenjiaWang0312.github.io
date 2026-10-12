# EgoFound3R Project Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a lightweight local EgoFound3R publication entry and project page with selected downloaded assets.

**Architecture:** Add one Jekyll publication record and one standalone project directory. Reuse the source page's content hierarchy, copy its stylesheet, and keep only three figures, the overview video, one demo video, and the paper PDF locally.

**Tech Stack:** Jekyll, static HTML/CSS, HTML5 video, curl, Bundler.

---

### Task 1: Download selected source assets

**Files:**
- Create: `projects/egofound3r/assets/EgoFound3R.pdf`
- Create: `projects/egofound3r/assets/img/figures/{teaser,efficiency,framework}.webp`
- Create: `projects/egofound3r/videos/overview/overview.mp4`
- Create: `projects/egofound3r/videos/demo/0.mp4`

- [ ] Create the destination directories.
- [ ] Download each asset from `https://mint-sjtu.github.io/EgoFound3R.io/` with `curl -fL`.
- [ ] Confirm each file exists and has non-zero size.

### Task 2: Add publication metadata

**Files:**
- Create: `_publications/2026-10-12-egofound3r.md`

- [ ] Add title, arXiv venue/date, citation, BibTeX, paper/arXiv/code links, and `weburl: '/projects/egofound3r/'`.
- [ ] Set `header.teaser` to `/projects/egofound3r/assets/img/figures/teaser.webp`.
- [ ] Preserve author order and mark Wenjia Wang as `*`; retain Binhua Zuo and Bo Zhao as corresponding authors.
- [ ] Define `* Initial idea contributor.` and `† Corresponding authors.` in the award note.

### Task 3: Build the local project page

**Files:**
- Create: `projects/egofound3r/index.html`
- Create: `projects/egofound3r/assets/css/style.css`

- [ ] Copy the source page's visual hierarchy into a local standalone page.
- [ ] Use local paths for all downloaded figures, video files, and PDF.
- [ ] Include hero metadata, abstract, key results, method overview, local overview/demo video sections, BibTeX, and a link to the original page for the complete galleries.
- [ ] Keep the author marker as `* Initial idea contributor.` and retain both corresponding authors.
- [ ] Adapt stylesheet URLs and relative asset paths for `/projects/egofound3r/`.

### Task 4: Validate and preview

**Files:**
- Generated: `_site/`

- [ ] Check local HTML asset references with `rg` and filesystem checks.
- [ ] Run `bundle exec jekyll build --destination ./_site`.
- [ ] Start `./preview.sh` and inspect `/`, `/publications/`, `/projects/egofound3r/`, and `/cv/` in the browser.
- [ ] Fix any broken links, layout issues, or author-marker errors found during preview.
- [ ] Commit the implementation with `Add EgoFound3R publication and project page`.
