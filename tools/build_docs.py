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
RELEASE_VERSION = "v84 draft"
RELEASE_SLUG = "v84_draft"

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
        "version": "v19 draft",
        "pdf": "Volume_03_Book_03_17_Remote_Work_Automation_v19_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-18-enterprise-governance",
        "title": "Volume 03 - Book 03.18 Enterprise Governance",
        "version": "v20 draft",
        "pdf": "Volume_03_Book_03_18_Enterprise_Governance_v20_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-19-infrastructure",
        "title": "Volume 03 - Book 03.19 Infrastructure",
        "version": "v21 draft",
        "pdf": "Volume_03_Book_03_19_Infrastructure_v21_draft.pdf",
    },
    {
        "id": "volume-03-master-blueprint/book-03-20-autonomous-enterprise",
        "title": "Volume 03 - Book 03.20 Autonomous Enterprise",
        "version": "v22 draft",
        "pdf": "Volume_03_Book_03_20_Autonomous_Enterprise_v22_draft.pdf",
    },
    {
        "id": "volume-04-canonical-dictionary",
        "title": "Volume 04 - Canonical Dictionary",
        "version": "v23 draft",
        "pdf": "Volume_04_Canonical_Dictionary_v23_draft.pdf",
    },
    {
        "id": "volume-05-engineering-standards",
        "title": "Volume 05 - Engineering Standards",
        "version": "v24 draft",
        "pdf": "Volume_05_Engineering_Standards_v24_draft.pdf",
    },
    {
        "id": "volume-06-specifications/core",
        "title": "Volume 06 - Core Specifications",
        "version": "v25 draft",
        "pdf": "Volume_06_Core_Specifications_v25_draft.pdf",
    },
    {
        "id": "volume-06-specifications/dna-operating-system",
        "title": "Volume 06 - DNA Operating System Specifications",
        "version": "v26 draft",
        "pdf": "Volume_06_DNA_Operating_System_Specifications_v26_draft.pdf",
    },
    {
        "id": "volume-06-specifications/runtime-ecosystem",
        "title": "Volume 06 - Runtime Ecosystem Specifications",
        "version": "v27 draft",
        "pdf": "Volume_06_Runtime_Ecosystem_Specifications_v27_draft.pdf",
    },
    {
        "id": "volume-06-specifications/execution-os",
        "title": "Volume 06 - Execution OS Specifications",
        "version": "v28 draft",
        "pdf": "Volume_06_Execution_OS_Specifications_v28_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v29-knowledge-capability-workflow-specifications",
        "title": "Volume 06 Specifications - Knowledge Capability Workflow Specifications",
        "version": "v29 draft",
        "pdf": "Volume_06_Knowledge_Capability_Workflow_Specifications_v29_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v30-model-provider-plugin-connector-specifications",
        "title": "Volume 06 Specifications - Model Provider Plugin Connector Specifications",
        "version": "v30 draft",
        "pdf": "Volume_06_Model_Provider_Plugin_Connector_Specifications_v30_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v31-marketplace-opportunity-automation-specifications",
        "title": "Volume 06 Specifications - Marketplace Opportunity Automation Specifications",
        "version": "v31 draft",
        "pdf": "Volume_06_Marketplace_Opportunity_Automation_Specifications_v31_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v32-governance-infrastructure-security-specifications",
        "title": "Volume 06 Specifications - Governance Infrastructure Security Specifications",
        "version": "v32 draft",
        "pdf": "Volume_06_Governance_Infrastructure_Security_Specifications_v32_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v33-storage-dashboard-api-mcp-specifications",
        "title": "Volume 06 Specifications - Storage Dashboard API MCP Specifications",
        "version": "v33 draft",
        "pdf": "Volume_06_Storage_Dashboard_Api_Mcp_Specifications_v33_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v34-integration-notification-automation-analytics-specifications",
        "title": "Volume 06 Specifications - Integration Notification Automation Analytics Specifications",
        "version": "v34 draft",
        "pdf": "Volume_06_Integration_Notification_Automation_Analytics_Specifications_v34_draft.pdf",
    },
    {
        "id": "volume-06-specifications/v35-volume-06-completion-specifications",
        "title": "Volume 06 Specifications - Volume 06 Completion Specifications",
        "version": "v35 draft",
        "pdf": "Volume_06_Volume_06_Completion_Specifications_v35_draft.pdf",
    },
    {
        "id": "volume-07-development-guide/v36-development-guide-part-1",
        "title": "Volume 07 Development Guide - Development Guide Part 1",
        "version": "v36 draft",
        "pdf": "Volume_07_Development_Guide_Part_1_v36_draft.pdf",
    },
    {
        "id": "volume-07-development-guide/v37-development-guide-part-2",
        "title": "Volume 07 Development Guide - Development Guide Part 2",
        "version": "v37 draft",
        "pdf": "Volume_07_Development_Guide_Part_2_v37_draft.pdf",
    },
    {
        "id": "volume-07-development-guide/v38-development-guide-part-3",
        "title": "Volume 07 Development Guide - Development Guide Part 3",
        "version": "v38 draft",
        "pdf": "Volume_07_Development_Guide_Part_3_v38_draft.pdf",
    },
    {
        "id": "volume-07-development-guide/v39-development-guide-part-4",
        "title": "Volume 07 Development Guide - Development Guide Part 4",
        "version": "v39 draft",
        "pdf": "Volume_07_Development_Guide_Part_4_v39_draft.pdf",
    },
    {
        "id": "volume-07-development-guide/v40-development-guide-part-5",
        "title": "Volume 07 Development Guide - Development Guide Part 5",
        "version": "v40 draft",
        "pdf": "Volume_07_Development_Guide_Part_5_v40_draft.pdf",
    },
    {
        "id": "volume-08-operations-guide/v41-operations-guide-part-1",
        "title": "Volume 08 Operations Guide - Operations Guide Part 1",
        "version": "v41 draft",
        "pdf": "Volume_08_Operations_Guide_Part_1_v41_draft.pdf",
    },
    {
        "id": "volume-08-operations-guide/v42-operations-guide-part-2",
        "title": "Volume 08 Operations Guide - Operations Guide Part 2",
        "version": "v42 draft",
        "pdf": "Volume_08_Operations_Guide_Part_2_v42_draft.pdf",
    },
    {
        "id": "volume-08-operations-guide/v43-operations-guide-part-3",
        "title": "Volume 08 Operations Guide - Operations Guide Part 3",
        "version": "v43 draft",
        "pdf": "Volume_08_Operations_Guide_Part_3_v43_draft.pdf",
    },
    {
        "id": "volume-08-operations-guide/v44-operations-guide-part-4",
        "title": "Volume 08 Operations Guide - Operations Guide Part 4",
        "version": "v44 draft",
        "pdf": "Volume_08_Operations_Guide_Part_4_v44_draft.pdf",
    },
    {
        "id": "volume-08-operations-guide/v45-operations-guide-part-5",
        "title": "Volume 08 Operations Guide - Operations Guide Part 5",
        "version": "v45 draft",
        "pdf": "Volume_08_Operations_Guide_Part_5_v45_draft.pdf",
    },
    {
        "id": "volume-09-testing-guide/v46-testing-guide-part-1",
        "title": "Volume 09 Testing Guide - Testing Guide Part 1",
        "version": "v46 draft",
        "pdf": "Volume_09_Testing_Guide_Part_1_v46_draft.pdf",
    },
    {
        "id": "volume-09-testing-guide/v47-testing-guide-part-2",
        "title": "Volume 09 Testing Guide - Testing Guide Part 2",
        "version": "v47 draft",
        "pdf": "Volume_09_Testing_Guide_Part_2_v47_draft.pdf",
    },
    {
        "id": "volume-09-testing-guide/v48-testing-guide-part-3",
        "title": "Volume 09 Testing Guide - Testing Guide Part 3",
        "version": "v48 draft",
        "pdf": "Volume_09_Testing_Guide_Part_3_v48_draft.pdf",
    },
    {
        "id": "volume-09-testing-guide/v49-testing-guide-part-4",
        "title": "Volume 09 Testing Guide - Testing Guide Part 4",
        "version": "v49 draft",
        "pdf": "Volume_09_Testing_Guide_Part_4_v49_draft.pdf",
    },
    {
        "id": "volume-09-testing-guide/v50-testing-guide-part-5",
        "title": "Volume 09 Testing Guide - Testing Guide Part 5",
        "version": "v50 draft",
        "pdf": "Volume_09_Testing_Guide_Part_5_v50_draft.pdf",
    },
    {
        "id": "volume-10-enterprise-organization/v51-enterprise-organization-part-1",
        "title": "Volume 10 Enterprise Organization - Enterprise Organization Part 1",
        "version": "v51 draft",
        "pdf": "Volume_10_Enterprise_Organization_Part_1_v51_draft.pdf",
    },
    {
        "id": "volume-10-enterprise-organization/v52-enterprise-organization-part-2",
        "title": "Volume 10 Enterprise Organization - Enterprise Organization Part 2",
        "version": "v52 draft",
        "pdf": "Volume_10_Enterprise_Organization_Part_2_v52_draft.pdf",
    },
    {
        "id": "volume-10-enterprise-organization/v53-enterprise-organization-part-3",
        "title": "Volume 10 Enterprise Organization - Enterprise Organization Part 3",
        "version": "v53 draft",
        "pdf": "Volume_10_Enterprise_Organization_Part_3_v53_draft.pdf",
    },
    {
        "id": "volume-10-enterprise-organization/v54-enterprise-organization-part-4",
        "title": "Volume 10 Enterprise Organization - Enterprise Organization Part 4",
        "version": "v54 draft",
        "pdf": "Volume_10_Enterprise_Organization_Part_4_v54_draft.pdf",
    },
    {
        "id": "volume-10-enterprise-organization/v55-enterprise-organization-part-5",
        "title": "Volume 10 Enterprise Organization - Enterprise Organization Part 5",
        "version": "v55 draft",
        "pdf": "Volume_10_Enterprise_Organization_Part_5_v55_draft.pdf",
    },
    {
        "id": "volume-11-ai-society/v56-ai-society-part-1",
        "title": "Volume 11 AI Society - AI Society Part 1",
        "version": "v56 draft",
        "pdf": "Volume_11_Ai_Society_Part_1_v56_draft.pdf",
    },
    {
        "id": "volume-11-ai-society/v57-ai-society-part-2",
        "title": "Volume 11 AI Society - AI Society Part 2",
        "version": "v57 draft",
        "pdf": "Volume_11_Ai_Society_Part_2_v57_draft.pdf",
    },
    {
        "id": "volume-11-ai-society/v58-ai-society-part-3",
        "title": "Volume 11 AI Society - AI Society Part 3",
        "version": "v58 draft",
        "pdf": "Volume_11_Ai_Society_Part_3_v58_draft.pdf",
    },
    {
        "id": "volume-11-ai-society/v59-ai-society-part-4",
        "title": "Volume 11 AI Society - AI Society Part 4",
        "version": "v59 draft",
        "pdf": "Volume_11_Ai_Society_Part_4_v59_draft.pdf",
    },
    {
        "id": "volume-11-ai-society/v60-ai-society-part-5",
        "title": "Volume 11 AI Society - AI Society Part 5",
        "version": "v60 draft",
        "pdf": "Volume_11_Ai_Society_Part_5_v60_draft.pdf",
    },
    {
        "id": "volume-12-knowledge-system/v61-knowledge-system-part-1",
        "title": "Volume 12 Knowledge System - Knowledge System Part 1",
        "version": "v61 draft",
        "pdf": "Volume_12_Knowledge_System_Part_1_v61_draft.pdf",
    },
    {
        "id": "volume-12-knowledge-system/v62-knowledge-system-part-2",
        "title": "Volume 12 Knowledge System - Knowledge System Part 2",
        "version": "v62 draft",
        "pdf": "Volume_12_Knowledge_System_Part_2_v62_draft.pdf",
    },
    {
        "id": "volume-12-knowledge-system/v63-knowledge-system-part-3",
        "title": "Volume 12 Knowledge System - Knowledge System Part 3",
        "version": "v63 draft",
        "pdf": "Volume_12_Knowledge_System_Part_3_v63_draft.pdf",
    },
    {
        "id": "volume-12-knowledge-system/v64-knowledge-system-part-4",
        "title": "Volume 12 Knowledge System - Knowledge System Part 4",
        "version": "v64 draft",
        "pdf": "Volume_12_Knowledge_System_Part_4_v64_draft.pdf",
    },
    {
        "id": "volume-12-knowledge-system/v65-knowledge-system-part-5",
        "title": "Volume 12 Knowledge System - Knowledge System Part 5",
        "version": "v65 draft",
        "pdf": "Volume_12_Knowledge_System_Part_5_v65_draft.pdf",
    },
    {
        "id": "volume-13-capability-system/v66-capability-system-part-1",
        "title": "Volume 13 Capability System - Capability System Part 1",
        "version": "v66 draft",
        "pdf": "Volume_13_Capability_System_Part_1_v66_draft.pdf",
    },
    {
        "id": "volume-13-capability-system/v67-capability-system-part-2",
        "title": "Volume 13 Capability System - Capability System Part 2",
        "version": "v67 draft",
        "pdf": "Volume_13_Capability_System_Part_2_v67_draft.pdf",
    },
    {
        "id": "volume-13-capability-system/v68-capability-system-part-3",
        "title": "Volume 13 Capability System - Capability System Part 3",
        "version": "v68 draft",
        "pdf": "Volume_13_Capability_System_Part_3_v68_draft.pdf",
    },
    {
        "id": "volume-13-capability-system/v69-capability-system-part-4",
        "title": "Volume 13 Capability System - Capability System Part 4",
        "version": "v69 draft",
        "pdf": "Volume_13_Capability_System_Part_4_v69_draft.pdf",
    },
    {
        "id": "volume-13-capability-system/v70-capability-system-part-5",
        "title": "Volume 13 Capability System - Capability System Part 5",
        "version": "v70 draft",
        "pdf": "Volume_13_Capability_System_Part_5_v70_draft.pdf",
    },
    {
        "id": "volume-14-dna-operating-system/v71-dna-operating-system-part-1",
        "title": "Volume 14 DNA Operating System - DNA Operating System Part 1",
        "version": "v71 draft",
        "pdf": "Volume_14_Dna_Operating_System_Part_1_v71_draft.pdf",
    },
    {
        "id": "volume-14-dna-operating-system/v72-dna-operating-system-part-2",
        "title": "Volume 14 DNA Operating System - DNA Operating System Part 2",
        "version": "v72 draft",
        "pdf": "Volume_14_Dna_Operating_System_Part_2_v72_draft.pdf",
    },
    {
        "id": "volume-14-dna-operating-system/v73-dna-operating-system-part-3",
        "title": "Volume 14 DNA Operating System - DNA Operating System Part 3",
        "version": "v73 draft",
        "pdf": "Volume_14_Dna_Operating_System_Part_3_v73_draft.pdf",
    },
    {
        "id": "volume-14-dna-operating-system/v74-dna-operating-system-part-4",
        "title": "Volume 14 DNA Operating System - DNA Operating System Part 4",
        "version": "v74 draft",
        "pdf": "Volume_14_Dna_Operating_System_Part_4_v74_draft.pdf",
    },
    {
        "id": "volume-14-dna-operating-system/v75-dna-operating-system-part-5",
        "title": "Volume 14 DNA Operating System - DNA Operating System Part 5",
        "version": "v75 draft",
        "pdf": "Volume_14_Dna_Operating_System_Part_5_v75_draft.pdf",
    },
    {
        "id": "volume-15-runtime-ecosystem/v76-runtime-ecosystem-part-1",
        "title": "Volume 15 Runtime Ecosystem - Runtime Ecosystem Part 1",
        "version": "v76 draft",
        "pdf": "Volume_15_Runtime_Ecosystem_Part_1_v76_draft.pdf",
    },
    {
        "id": "volume-15-runtime-ecosystem/v77-runtime-ecosystem-part-2",
        "title": "Volume 15 Runtime Ecosystem - Runtime Ecosystem Part 2",
        "version": "v77 draft",
        "pdf": "Volume_15_Runtime_Ecosystem_Part_2_v77_draft.pdf",
    },
    {
        "id": "volume-15-runtime-ecosystem/v78-runtime-ecosystem-part-3",
        "title": "Volume 15 Runtime Ecosystem - Runtime Ecosystem Part 3",
        "version": "v78 draft",
        "pdf": "Volume_15_Runtime_Ecosystem_Part_3_v78_draft.pdf",
    },
    {
        "id": "volume-15-runtime-ecosystem/v79-runtime-ecosystem-part-4",
        "title": "Volume 15 Runtime Ecosystem - Runtime Ecosystem Part 4",
        "version": "v79 draft",
        "pdf": "Volume_15_Runtime_Ecosystem_Part_4_v79_draft.pdf",
    },
    {
        "id": "volume-15-runtime-ecosystem/v80-runtime-ecosystem-part-5",
        "title": "Volume 15 Runtime Ecosystem - Runtime Ecosystem Part 5",
        "version": "v80 draft",
        "pdf": "Volume_15_Runtime_Ecosystem_Part_5_v80_draft.pdf",
    },
    {
        "id": "volume-16-model-ecosystem/v81-model-ecosystem-part-1",
        "title": "Volume 16 Model Ecosystem - Model Ecosystem Part 1",
        "version": "v81 draft",
        "pdf": "Volume_16_Model_Ecosystem_Part_1_v81_draft.pdf",
    },
    {
        "id": "volume-16-model-ecosystem/v82-model-ecosystem-part-2",
        "title": "Volume 16 Model Ecosystem - Model Ecosystem Part 2",
        "version": "v82 draft",
        "pdf": "Volume_16_Model_Ecosystem_Part_2_v82_draft.pdf",
    },
    {
        "id": "volume-16-model-ecosystem/v83-model-ecosystem-part-3",
        "title": "Volume 16 Model Ecosystem - Model Ecosystem Part 3",
        "version": "v83 draft",
        "pdf": "Volume_16_Model_Ecosystem_Part_3_v83_draft.pdf",
    },
    {
        "id": "volume-16-model-ecosystem/v84-model-ecosystem-part-4",
        "title": "Volume 16 Model Ecosystem - Model Ecosystem Part 4",
        "version": RELEASE_VERSION,
        "pdf": "Volume_16_Model_Ecosystem_Part_4_v84_draft.pdf",
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
    source_files = markdown_files(volume_dir)
    if output.exists() and source_files:
        newest_source = max(path.stat().st_mtime for path in source_files)
        if output.stat().st_mtime >= newest_source:
            return output
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
    for index, path in enumerate(source_files):
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
