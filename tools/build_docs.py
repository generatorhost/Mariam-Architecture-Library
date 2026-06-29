from __future__ import annotations

import hashlib
import json
import textwrap
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "architecture-library"
RELEASES = LIBRARY / "releases"
PDF_DIR = RELEASES / "pdf"
RELEASE_VERSION = "v19 draft"
RELEASE_SLUG = "v19_draft"

VOLUMES = [
    {
        "id": "volume-00-enterprise-constitution",
        "title": "Volume 00 - Enterprise Constitution",
        "version": "v1 draft",
        "pdf": "Volume_00_Enterprise_Constitution_v1_draft.pdf",
    },
    {
        "id": "volume-01-master-vision",
        "title": "Volume 01 - Master Vision",
        "version": "v1 draft",
        "pdf": "Volume_01_Master_Vision_v1_draft.pdf",
    },
    {
        "id": "volume-02-master-roadmap",
        "title": "Volume 02 - Master Roadmap",
        "version": "v2 draft",
        "pdf": "Volume_02_Master_Roadmap_v2_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-01-enterprise-core",
        "title": "Volume 03 - Book 03.01 Enterprise Core",
        "version": "v3 draft",
        "pdf": "Volume_03_Book_03_01_Enterprise_Core_v3_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-02-enterprise-organization",
        "title": "Volume 03 - Book 03.02 Enterprise Organization",
        "version": "v4 draft",
        "pdf": "Volume_03_Book_03_02_Enterprise_Organization_v4_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-03-ai-society",
        "title": "Volume 03 - Book 03.03 AI Society",
        "version": "v5 draft",
        "pdf": "Volume_03_Book_03_03_AI_Society_v5_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-04-knowledge-system",
        "title": "Volume 03 - Book 03.04 Knowledge System",
        "version": "v6 draft",
        "pdf": "Volume_03_Book_03_04_Knowledge_System_v6_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-05-capability-system",
        "title": "Volume 03 - Book 03.05 Capability System",
        "version": "v7 draft",
        "pdf": "Volume_03_Book_03_05_Capability_System_v7_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-06-dna-operating-system",
        "title": "Volume 03 - Book 03.06 DNA Operating System",
        "version": "v8 draft",
        "pdf": "Volume_03_Book_03_06_DNA_Operating_System_v8_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-07-runtime-ecosystem",
        "title": "Volume 03 - Book 03.07 Runtime Ecosystem",
        "version": "v9 draft",
        "pdf": "Volume_03_Book_03_07_Runtime_Ecosystem_v9_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-08-workflow-system",
        "title": "Volume 03 - Book 03.08 Workflow System",
        "version": "v10 draft",
        "pdf": "Volume_03_Book_03_08_Workflow_System_v10_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-09-swarm-intelligence",
        "title": "Volume 03 - Book 03.09 Swarm Intelligence",
        "version": "v11 draft",
        "pdf": "Volume_03_Book_03_09_Swarm_Intelligence_v11_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-10-model-ecosystem",
        "title": "Volume 03 - Book 03.10 Model Ecosystem",
        "version": "v12 draft",
        "pdf": "Volume_03_Book_03_10_Model_Ecosystem_v12_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-11-provider-ecosystem",
        "title": "Volume 03 - Book 03.11 Provider Ecosystem",
        "version": "v13 draft",
        "pdf": "Volume_03_Book_03_11_Provider_Ecosystem_v13_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-12-plugin-runtime",
        "title": "Volume 03 - Book 03.12 Plugin Runtime",
        "version": "v14 draft",
        "pdf": "Volume_03_Book_03_12_Plugin_Runtime_v14_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-13-connector-runtime",
        "title": "Volume 03 - Book 03.13 Connector Runtime",
        "version": "v15 draft",
        "pdf": "Volume_03_Book_03_13_Connector_Runtime_v15_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-14-marketplace",
        "title": "Volume 03 - Book 03.14 Marketplace",
        "version": "v16 draft",
        "pdf": "Volume_03_Book_03_14_Marketplace_v16_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-15-opportunity-intelligence",
        "title": "Volume 03 - Book 03.15 Opportunity Intelligence",
        "version": "v17 draft",
        "pdf": "Volume_03_Book_03_15_Opportunity_Intelligence_v17_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-16-freelance-automation",
        "title": "Volume 03 - Book 03.16 Freelance Automation",
        "version": "v18 draft",
        "pdf": "Volume_03_Book_03_16_Freelance_Automation_v18_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-17-remote-work-automation",
        "title": "Volume 03 - Book 03.17 Remote Work Automation",
        "version": RELEASE_VERSION,
        "pdf": "Volume_03_Book_03_17_Remote_Work_Automation_v19_draft.pdf",
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def markdown_files(volume_dir: Path) -> list[Path]:
    priority = {
        "README.md": 0,
        "INDEX.md": 1,
        "CHANGELOG.md": 2,
        "TRACEABILITY.md": 3,
        "ACCEPTANCE.md": 4,
    }
    return sorted(
        volume_dir.glob("*.md"),
        key=lambda path: (priority.get(path.name, 50), path.name.lower()),
    )


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "MariamTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=26,
            spaceAfter=10,
            textColor=colors.HexColor("#18202f"),
        ),
        "h1": ParagraphStyle(
            "MariamH1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=17,
            leading=22,
            spaceBefore=10,
            spaceAfter=8,
            textColor=colors.HexColor("#24324a"),
        ),
        "h2": ParagraphStyle(
            "MariamH2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            spaceBefore=9,
            spaceAfter=5,
            textColor=colors.HexColor("#31415c"),
        ),
        "body": ParagraphStyle(
            "MariamBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13.5,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "MariamBullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=3,
        ),
        "meta": ParagraphStyle(
            "MariamMeta",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#4b5565"),
            spaceAfter=3,
        ),
    }


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("**", "")
        .replace("`", "")
    )


def markdown_to_story(path: Path, styles: dict[str, ParagraphStyle]) -> list:
    story = []
    in_table = False
    table_rows: list[list[str]] = []

    def flush_table() -> None:
        nonlocal table_rows, in_table
        if not table_rows:
            return
        cleaned = [row for row in table_rows if not all(set(cell) <= {"-", " "} for cell in row)]
        if cleaned:
            table = Table(cleaned, hAlign="LEFT", repeatRows=1)
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#edf1f7")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#18202f")),
                        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#c7cedb")),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 4),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ]
                )
            )
            story.append(table)
            story.append(Spacer(1, 5))
        table_rows = []
        in_table = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            flush_table()
            story.append(Spacer(1, 3))
            continue

        if line.startswith("|") and line.endswith("|"):
            in_table = True
            table_rows.append([escape(cell.strip()) for cell in line.strip("|").split("|")])
            continue
        if in_table:
            flush_table()

        if line.startswith("# "):
            story.append(Paragraph(escape(line[2:]), styles["h1"]))
        elif line.startswith("## "):
            story.append(Paragraph(escape(line[3:]), styles["h2"]))
        elif line.startswith("- "):
            story.append(Paragraph("&#8226; " + escape(line[2:]), styles["bullet"]))
        elif line.startswith("**") and ":**" in line:
            story.append(Paragraph(escape(line), styles["meta"]))
        else:
            wrapped = " ".join(textwrap.wrap(line, width=110)) if len(line) > 110 else line
            story.append(Paragraph(escape(wrapped), styles["body"]))

    flush_table()
    return story


def build_pdf(volume: dict[str, str]) -> Path:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    volume_dir = LIBRARY / volume["id"]
    output = PDF_DIR / volume["pdf"]
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=17 * mm,
        title=volume["title"],
        author="Mariam Architecture Library",
    )
    story = [Paragraph(volume["title"], styles["title"]), Paragraph(f"Version {volume['version']}", styles["meta"])]
    for index, path in enumerate(markdown_files(volume_dir)):
        if index:
            story.append(PageBreak())
        story.append(Paragraph(path.name, styles["meta"]))
        story.extend(markdown_to_story(path, styles))
    doc.build(story)
    return output


def release_inputs() -> list[Path]:
    paths: list[Path] = []
    paths.append(ROOT / "README.md")
    paths.extend(sorted(LIBRARY.rglob("*.md")))
    paths.extend(sorted(RELEASES.glob("*.json")))
    paths.extend(sorted(PDF_DIR.glob("*.pdf")))
    unique = {path.resolve(): path for path in paths if path.exists()}
    return sorted(unique.values(), key=lambda path: path.relative_to(ROOT).as_posix())


def build_zip() -> Path:
    zip_path = RELEASES / f"Mariam_Architecture_Library_{RELEASE_SLUG}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in release_inputs():
            archive.write(path, path.relative_to(ROOT).as_posix())
    return zip_path


def build_manifest(artifacts: list[Path]) -> Path:
    manifest_path = RELEASES / "MANIFEST.json"
    entries = []
    for path in sorted(artifacts, key=lambda item: item.relative_to(ROOT).as_posix()):
        entries.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    manifest = {
        "name": "Mariam Architecture Library",
        "version": RELEASE_VERSION,
        "status": "draft",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": entries,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest_path


def main() -> None:
    RELEASES.mkdir(parents=True, exist_ok=True)
    pdfs = [build_pdf(volume) for volume in VOLUMES]
    manifest = build_manifest(pdfs)
    zip_path = build_zip()
    manifest = build_manifest(pdfs + [zip_path])
    for pdf in pdfs:
        print(f"Generated {pdf.relative_to(ROOT)}")
    print(f"Generated {zip_path.relative_to(ROOT)}")
    print(f"Generated {manifest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
