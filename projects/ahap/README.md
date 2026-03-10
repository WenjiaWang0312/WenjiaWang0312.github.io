# Personal Project Homepage Template

This folder contains a project-page template adapted from the style of:

- EgoGrasp project page
- Nerfies project page

## Files

- `index.html`: page structure and all text content
- `assets/css/style.css`: page style and responsive layout
- `assets/images/*.svg`: placeholder figures/posters

## Quick customization

1. Edit `index.html`:
   - Replace page title/subtitle.
   - Replace author names, affiliations, and links.
   - Replace button links (`Paper`, `arXiv`, `Video`, `Code`).
   - Update abstract text and section captions.
   - Update BibTeX content.
2. Replace placeholder images in `assets/images/` with your own files, or modify image paths in `index.html`.
3. For demos, set real video paths in each `<video><source src=\"...\" /></video>` block.

## Local preview

From `homepage_template/`:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.
