# EgoFound3R Publication and Project Page

## Goal

Add EgoFound3R to the publications collection and create a local project page that follows the source page's research presentation while keeping the repository lightweight.

## Content

- Add a publication entry dated 2026-10-12 with the original title, arXiv metadata, paper/code links, and a local `weburl` of `/projects/egofound3r/`.
- Preserve the author order and original corresponding-author markers for Binhua Zuo and Bo Zhao.
- Mark Wenjia Wang with `*` and define `* Initial idea contributor.` on both the publication entry and project page.
- Use the paper teaser as the publication card image.

## Local project page

Create `projects/egofound3r/index.html` with a self-contained page shell based on the repository's existing project pages:

- Hero title, authors, affiliations, arXiv/PDF/code/video/BibTeX links.
- Local teaser, abstract, key-results cards, efficiency figure, method figure, and BibTeX.
- Local overview video and one representative demo video.
- A concise note linking to the original project page for the complete demo and comparison galleries.

Download only these source assets into `projects/egofound3r/`:

- `assets/img/figures/teaser.webp`
- `assets/img/figures/efficiency.webp`
- `assets/img/figures/framework.webp`
- `videos/overview/overview.mp4`
- `videos/demo/0.mp4`
- `assets/EgoFound3R.pdf`

Copy the source stylesheet and adapt relative paths so the page works under the local project directory. Keep external font/icon CDNs only where they are already used by the source page.

## Validation

- Confirm all local asset references resolve.
- Build the Jekyll site with `bundle exec jekyll build --destination ./_site`.
- Check the publication card and local project page paths in the generated site.
- Verify author markers and links match the source metadata.
