from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicationVenueTest(unittest.TestCase):
    def test_publication_venue_markers_cover_all_display_contexts(self):
        template_path = ROOT / "_includes" / "publication-venue.html"
        self.assertTrue(template_path.exists(), "missing shared publication venue include")
        template = template_path.read_text(encoding="utf-8")

        self.assertIn("publication-type-marker--{{ venue_type }}", template)
        for venue_type in ("conference", "journal", "tech-report", "preprint"):
            self.assertIn(f"assign venue_type = '{venue_type}'", template)

        self.assertIn("contains 'arxiv'", template)
        self.assertIn("contains 'paper submitted'", template)
        self.assertIn("contains 'tech report'", template)
        self.assertIn("contains 'tpami'", template)

        for path in (
            ROOT / "_includes" / "archive-single.html",
            ROOT / "_includes" / "publication-detail.html",
        ):
            self.assertIn(
                "{% include publication-venue.html item=", path.read_text(encoding="utf-8")
            )

        homepage = (ROOT / "_pages" / "about.md").read_text(encoding="utf-8")
        self.assertEqual(
            homepage.count("publication-type-marker publication-type-marker--conference"), 3
        )

    def test_publication_marker_styles_define_every_type(self):
        styles = (ROOT / "assets" / "css" / "main.scss").read_text(encoding="utf-8")

        self.assertIn(".publication-type-marker {", styles)
        for venue_type in ("conference", "journal", "tech-report", "preprint"):
            self.assertIn(f".publication-type-marker--{venue_type}", styles)
