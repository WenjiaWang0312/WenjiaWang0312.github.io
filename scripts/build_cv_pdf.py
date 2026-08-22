#!/usr/bin/env python3
"""Build the downloadable CV from the site's structured CV data."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def latex_escape(value: object) -> str:
    text = str(value or "")
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def latex_url(value: object) -> str:
    return str(value or "").replace("%", r"\%").replace("#", r"\#")


def parse_front_matter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    values: dict[str, object] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not match:
            continue
        key, raw_value = match.groups()
        raw_value = raw_value.strip()
        if raw_value.startswith("|"):
            continue
        if len(raw_value) >= 2 and raw_value[0] == raw_value[-1] and raw_value[0] in "'\"":
            raw_value = raw_value[1:-1]
        if raw_value.lower() in {"true", "false"}:
            values[key] = raw_value.lower() == "true"
        elif raw_value.isdigit():
            values[key] = int(raw_value)
        else:
            values[key] = raw_value
    return values


def selected_publications(root: Path) -> list[dict[str, object]]:
    publications = []
    for path in sorted((root / "_publications").glob("*.md")):
        metadata = parse_front_matter(path)
        if metadata.get("cv") is True:
            metadata["source"] = path
            publications.append(metadata)
    return sorted(publications, key=lambda item: int(item.get("cv_order", 9999)))


def profile_url(basics: dict[str, object], network: str) -> str:
    for profile in basics.get("profiles", []):
        if str(profile.get("network", "")).lower() == network.lower():
            return str(profile.get("url", ""))
    return ""


def render_header(basics: dict[str, object]) -> str:
    name = latex_escape(basics.get("name", ""))
    location = basics.get("location", {})
    city = latex_escape(location.get("city", ""))
    contact_items = []

    if city:
        contact_items.append(
            r"        \mbox{{\color{black}\footnotesize\faMapMarker*}\hspace*{0.13cm}"
            + city
            + r"}%"
        )
    email = str(basics.get("email", ""))
    if email:
        contact_items.append(
            r"        \mbox{\hrefWithoutArrow{"
            + latex_url(email)
            + r"}{\color{black}{\footnotesize\faEnvelope[regular]}\hspace*{0.13cm}"
            + latex_escape(email)
            + r"}}%"
        )
    phone = str(basics.get("phone", ""))
    if phone:
        phone_target = re.sub(r"[^0-9+]", "", phone)
        contact_items.append(
            r"        \mbox{\hrefWithoutArrow{tel:"
            + phone_target
            + r"}{\color{black}{\footnotesize\faPhone*}\hspace*{0.13cm}"
            + latex_escape(phone)
            + r"}}%"
        )
    website = str(basics.get("website", ""))
    if website:
        contact_items.append(
            r"        \mbox{\hrefWithoutArrow{"
            + latex_url(website)
            + r"}{\color{black}{\footnotesize\faLink}\hspace*{0.13cm}Homepage}}%"
        )
    github = profile_url(basics, "GitHub")
    if github:
        contact_items.append(
            r"        \mbox{\hrefWithoutArrow{"
            + latex_url(github)
            + r"}{\color{black}{\footnotesize\faGithub}\hspace*{0.13cm}Github}}%"
        )

    lines = [
        r"    \placelastupdatedtext",
        r"    \begin{header}",
        rf"        \textbf{{\fontsize{{24 pt}}{{24 pt}}\selectfont {name}}}",
        "",
        r"        \vspace{0.3 cm}",
        "",
        r"        \normalsize",
    ]
    for index, item in enumerate(contact_items):
        lines.append(item)
        if index < len(contact_items) - 1:
            lines.extend([r"        \kern 0.25 cm%", r"        \AND%"])
    lines.extend(["    \\end{header}", "", r"    \vspace{0.3 cm - 0.3 cm}"])
    return "\n".join(lines)


def format_date(value: object) -> str:
    text = str(value or "")
    match = re.match(r"^(\d{4})-(\d{2})(.*)$", text)
    if not match:
        return text
    year, month, suffix = match.groups()
    month_name = datetime.strptime(month, "%m").strftime("%b")
    return f"{month_name} {year}{suffix}"


def format_range(start: object, end: object) -> str:
    start_text = format_date(start)
    end_text = format_date(end)
    if start_text and end_text:
        return f"{start_text} -- {end_text}"
    return start_text or end_text


def render_biography(paragraphs: list[object]) -> str:
    lines = [r"    \section{Biography}", ""]
    for paragraph in paragraphs:
        lines.extend([latex_escape(paragraph), ""])
    return "\n".join(lines).rstrip()


def render_education(entries: list[dict[str, object]]) -> str:
    lines = [r"    \section{Education}", ""]
    for entry in entries:
        lines.extend(
            [
                r"        \begin{twocolentry}{",
                rf"        \textit{{{latex_escape(format_range(entry.get('startDate'), entry.get('endDate')))}}}}}",
                r"            \textbf{" + latex_escape(entry.get("institution", "")) + "}",
                "",
                r"            \textit{" + latex_escape(entry.get("area", "")) + "}",
            ]
        )
        if entry.get("detail"):
            lines.extend(["", r"            \textit{" + latex_escape(entry["detail"]) + "}"])
        lines.extend([r"        \end{twocolentry}", ""])
    return "\n".join(lines).rstrip()


def authors_to_tex(value: object) -> str:
    text = html.unescape(str(value or ""))
    text = text.replace("<strong>", "BOLDSTARTTOKEN").replace("</strong>", "BOLDENDTOKEN")
    text = re.sub(r"<big>.*?</big>", "CORRESPONDINGTOKEN", text)
    text = re.sub(r"<[^>]+>", "", text).replace("#", "")
    text = text.replace("†", "DAGGERTOKEN")
    text = latex_escape(text)
    return (
        text.replace("BOLDSTARTTOKEN", r"\textbf{")
        .replace("BOLDENDTOKEN", "}")
        .replace("CORRESPONDINGTOKEN", r"~\Letter")
        .replace("DAGGERTOKEN", r"\textsuperscript{\ensuremath{\dagger}}")
    )


def render_publications(entries: list[dict[str, object]]) -> str:
    lines = [r"    \section{Selected Publications}", ""]
    for index, entry in enumerate(entries):
        venue = latex_escape(entry.get("venue", ""))
        year = str(entry.get("date", ""))[:4]
        venue_year = f"{venue}{year}" if venue else year
        lines.extend(
            [
                r"        \begin{samepage}",
                r"            \begin{twocolentry}{",
                f"                {venue_year}",
                r"            }",
                r"                \textbf{" + latex_escape(entry.get("title", "")) + "}",
                "",
                r"                \vspace{0.10 cm}",
                r"                \small " + authors_to_tex(entry.get("authors", "")),
                r"            \end{twocolentry}",
                "",
                r"             \vspace{-0.15 cm}",
                r"        \end{samepage}",
            ]
        )
        if index < len(entries) - 1:
            lines.extend([r"        {\color{gray!40}\noindent\rule{0.98\textwidth}{0.3pt}}", ""])
    return "\n".join(lines).rstrip()


def render_work(entries: list[dict[str, object]]) -> str:
    lines = [r"    \section{Experience}", ""]
    for entry in entries:
        location = latex_escape(entry.get("location", ""))
        organization = latex_escape(entry.get("name", ""))
        if location:
            organization += ", " + location
        lines.extend(
            [
                r"        \begin{twocolentry}{",
                rf"        \textit{{{latex_escape(format_range(entry.get('startDate'), entry.get('endDate')))}}}}}",
                r"            \textbf{" + organization + "}",
                "",
                r"            \textit{" + latex_escape(entry.get("position", "")) + "}",
                r"        \end{twocolentry}",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def render_service(service: dict[str, list[object]]) -> str:
    conference = ",~".join(latex_escape(item) for item in service.get("conference", []))
    journal = ",~".join(latex_escape(item) for item in service.get("journal", []))
    lines = [r"    \section{Academic Service}", ""]
    if conference:
        lines.extend(
            [
                r"        \begin{onecolentry}",
                r"            \textbf{Conference Reviewer:} ~" + conference + ".",
                r"        \end{onecolentry}",
                "",
            ]
        )
    if journal:
        lines.extend(
            [
                r"        \begin{onecolentry}",
                r"            \textbf{Journal Reviewer:} ~" + journal + ".",
                r"        \end{onecolentry}",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def render_document(cv: dict[str, object], publications: list[dict[str, object]], template: str) -> str:
    document_start = template.find(r"\begin{document}")
    if document_start < 0:
        raise ValueError("CV template is missing \\begin{document}")
    preamble = template[:document_start]
    updated = datetime.now().strftime("%b %Y")
    preamble = re.sub(
        r"Last updated in [^}]+",
        f"Last updated in {updated}",
        preamble,
        count=1,
    )

    basics = cv.get("basics", {})
    body = [
        r"\begin{document}",
        r"""    \newcommand{\AND}{\unskip
        \cleaders\copy\ANDbox\hskip\wd\ANDbox
        \ignorespaces
    }
    \newsavebox\ANDbox
    \sbox\ANDbox{}""",
        render_header(basics),
        render_biography(cv.get("biography", [])),
        render_education(cv.get("education", [])),
        render_publications(publications),
        render_work(cv.get("work", [])),
        render_service(cv.get("academic_service", {})),
    ]
    return preamble + "\n" + "\n\n".join(body) + "\n\n\\end{document}\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--tectonic", default="tectonic")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    output = (args.output or root / "files" / "wenjiawang_cv.pdf").resolve()
    cv = json.loads((root / "_data" / "cv.json").read_text(encoding="utf-8"))
    template = (root / "assets" / "cv.tex").read_text(encoding="utf-8")
    publications = selected_publications(root)
    if not publications:
        raise ValueError("No publications marked with cv: true")

    tectonic = shutil.which(args.tectonic) or args.tectonic
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="cv-build-") as temp_dir:
        temp_root = Path(temp_dir)
        source = temp_root / "cv.tex"
        source.write_text(render_document(cv, publications, template), encoding="utf-8")
        subprocess.run(
            [tectonic, "--outdir", str(temp_root), str(source)],
            cwd=root,
            check=True,
        )
        shutil.copy2(temp_root / "cv.pdf", output)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
