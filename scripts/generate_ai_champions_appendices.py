from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


PAGE_WIDTH, PAGE_HEIGHT = A4
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"


def styles():
    sheet = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=sheet["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#111827"),
            spaceAfter=8,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=sheet["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#1D4ED8"),
            spaceAfter=6,
            spaceBefore=10,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=sheet["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#111827"),
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=sheet["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#4B5563"),
            spaceAfter=3,
        ),
    }


def base_doc(path: Path, title: str):
    OUT.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=16 * mm,
        bottomMargin=14 * mm,
        title=title,
        author="Codex",
    )
    return doc


def make_table(data, widths, header_bg="#E5E7EB", body_bg=None, font_size=8):
    header_style = ParagraphStyle(
        "TableHeader",
        fontName="Helvetica-Bold",
        fontSize=font_size,
        leading=font_size + 2,
        textColor=colors.HexColor("#111827"),
    )
    body_style = ParagraphStyle(
        "TableBody",
        fontName="Helvetica",
        fontSize=font_size,
        leading=font_size + 2,
        textColor=colors.HexColor("#111827"),
    )
    wrapped = []
    for row_index, row in enumerate(data):
        style = header_style if row_index == 0 else body_style
        wrapped.append([Paragraph(str(cell).replace("\n", "<br/>"), style) for cell in row])

    table = Table(wrapped, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(header_bg)),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("LEADING", (0, 0), (-1, -1), font_size + 2),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if body_bg:
        style.append(("BACKGROUND", (0, 1), (-1, -1), colors.HexColor(body_bg)))
    table.setStyle(TableStyle(style))
    return table


def build_architecture_pdf():
    s = styles()
    path = OUT / "AI_Champions_Appendix_Q9_Architecture.pdf"
    doc = base_doc(path, "AI Champions Appendix Q9")

    content = [
        Paragraph("AI Champions Phase 1 - Appendix Q9", s["title"]),
        Paragraph(
            "System architecture for UMBRAMED's hybrid clinical LLM and deterministic safety layer.",
            s["body"],
        ),
        Spacer(1, 6),
    ]

    diagram = [
        ["Data inputs", "Hybrid reasoning core", "Decision outputs"],
        [
            "Diraya retrospective data\n- patient notes\n- lab results\n- medication history\n- protocol labels",
            "1. Clinical LLM\nMistral/Llama fine-tuning\n\n2. Patient state encoder\nContext extraction\n\n3. Deterministic safety engine\nInteractions, contraindications,\ndosing and guideline checks",
            "Physician-facing output only if:\n- renewal is clinically appropriate\n- zero safety-critical violations\n- uncertain cases escalated to review",
        ],
    ]
    content.append(
        make_table(
            diagram,
            [56 * mm, 78 * mm, 40 * mm],
            header_bg="#DBEAFE",
            body_bg="#F8FAFC",
            font_size=8,
        )
    )
    content.append(Spacer(1, 10))

    content.append(Paragraph("Validation benchmark matrix", s["subtitle"]))
    benchmark = [
        ["Dimension", "Baseline", "Target Phase 1 result", "Evidence source"],
        [
            "Renewal appropriateness accuracy",
            "Prototype 89%",
            ">95% on complex cases",
            "Retrospective 6,500-patient validation set",
        ],
        [
            "Safety-critical false negatives",
            "Unknown",
            "Zero",
            "Deterministic engine plus held-out contraindication suite",
        ],
        [
            "Interaction detection sensitivity",
            "Rule-based only systems vary",
            "100% on known contraindications and interactions",
            "DrugBank, AEMPS, BNF cross-check",
        ],
        [
            "Operational relevance",
            "Alerts only",
            "Actionable renewal recommendation with physician oversight",
            "Workflow evaluation against Diraya renewal process",
        ],
    ]
    content.append(
        make_table(benchmark, [43 * mm, 30 * mm, 42 * mm, 55 * mm], header_bg="#DCFCE7", font_size=7)
    )
    content.append(Spacer(1, 8))
    content.append(
        Paragraph(
            "Design principle: the LLM never ships a recommendation directly to the clinician. Every output must independently pass the deterministic verification layer. If the rule engine is uncertain or finds a conflict, the case is forced into physician review.",
            s["small"],
        )
    )

    doc.build(content)
    return path


def build_team_pdf():
    s = styles()
    path = OUT / "AI_Champions_Appendix_Q10_Team_CVs.pdf"
    doc = base_doc(path, "AI Champions Appendix Q10")
    content = [
        Paragraph("AI Champions Phase 1 - Appendix Q10", s["title"]),
        Paragraph("Short bios and CV-style summaries for the core project team.", s["body"]),
        Spacer(1, 6),
        Paragraph("Sami Halawa Ribas - Project Lead and AI Architect", s["subtitle"]),
    ]

    sami_points = [
        "Role in Phase 1: overall project leadership, clinical LLM design, hybrid integration, technical whitepaper authorship.",
        "Experience: 10+ years in AI/ML product development with previous B2B SaaS exits and domain-specific LLM implementation work.",
        "Relevant strengths: healthcare data pipeline engineering, privacy-aware AI architecture, product execution, and regulatory-conscious software delivery.",
        "Current fit for this grant: founder responsible for the UMBRAMED prototype and the proposed hybrid clinical LLM plus deterministic safety architecture.",
    ]
    for point in sami_points:
        content.append(Paragraph("• " + point, s["body"]))

    content.append(Spacer(1, 8))
    content.append(Paragraph("Dr. Valerio Trigos Dominguez - Clinical Lead and Validation Director", s["subtitle"]))
    valerio_points = [
        "Role in Phase 1: clinical oversight, validation design, workflow supervision, and interpretation of retrospective prescription renewal cases.",
        "Clinical position: active Family Medicine specialist in the Andalusian Public Health System.",
        "Relevant experience: 10+ years of clinical practice, daily use of Diraya EHR, and management of a 6,500-patient panel.",
        "Academic and professional background: Licenciatura en Medicina, Universidad de Cadiz (2008-2014), with additional postgraduate emergency medicine training and scientific publication experience.",
        "Current fit for this grant: the project is grounded in his direct observation of the renewal workflow bottleneck that UMBRAMED addresses.",
    ]
    for point in valerio_points:
        content.append(Paragraph("• " + point, s["body"]))

    content.append(Spacer(1, 10))
    summary = [
        ["Team member", "Contribution to grant", "Availability"],
        ["Sami Halawa Ribas", "Technical lead, architecture, ML execution, reporting", "60% FTE over 6 months"],
        ["Dr. Valerio Trigos Dominguez", "Clinical lead, validation supervision, domain expertise", "30% FTE over 6 months"],
    ]
    content.append(make_table(summary, [52 * mm, 90 * mm, 34 * mm], header_bg="#FDE68A"))
    doc.build(content)
    return path


def build_gantt_pdf():
    s = styles()
    path = OUT / "AI_Champions_Appendix_Q14_Gantt.pdf"
    doc = base_doc(path, "AI Champions Appendix Q14")
    content = [
        Paragraph("AI Champions Phase 1 - Appendix Q14", s["title"]),
        Paragraph("Six-month delivery plan aligned to the work packages in the application.", s["body"]),
        Spacer(1, 6),
    ]

    gantt = [
        ["Work package", "Lead", "M1", "M2", "M3", "M4", "M5", "M6", "Key output"],
        ["WP1 Clinical LLM development", "Sami", "X", "X", "X", "X", "", "", "Trained model and benchmarks"],
        ["WP2 Safety engine", "Sami + ML Eng", "X", "X", "X", "", "", "", "Rule engine and test suite"],
        ["WP3 Hybrid integration + validation", "Valerio + Sami", "", "", "X", "X", "X", "X", "Integrated prototype and study"],
        ["WP4 Whitepaper + Phase 2 prep", "Sami", "", "", "", "", "X", "X", "Technical whitepaper and Phase 2 plan"],
        ["Project management", "Sami", "X", "X", "X", "X", "X", "X", "Reporting and risk control"],
    ]
    content.append(make_table(gantt, [40 * mm, 28 * mm, 9 * mm, 9 * mm, 9 * mm, 9 * mm, 9 * mm, 9 * mm, 60 * mm], header_bg="#E9D5FF", font_size=7))
    content.append(Spacer(1, 10))

    milestones = [
        ["Milestone", "Timing", "Dependency"],
        ["M1 Clinical LLM v1 trained", "Month 2", "Needed before full integration"],
        ["M2 Safety engine validated", "Month 3", "Needed before hybrid validation"],
        ["M3 Hybrid prototype integrated", "Month 4", "Needed before validation study"],
        ["M4 Validation study complete", "Month 5", "Needed before whitepaper"],
        ["M5 Whitepaper submitted and Phase 2 prepared", "Month 6", "Project closeout"],
    ]
    content.append(make_table(milestones, [66 * mm, 26 * mm, 78 * mm], header_bg="#FECACA"))
    content.append(Spacer(1, 8))
    content.append(
        Paragraph(
            "Critical dependency: ML Engineer recruitment must land by Month 2. If hiring slips, Sami covers initial implementation while recruitment continues.",
            s["small"],
        )
    )
    doc.build(content)
    return path


def build_risk_pdf():
    s = styles()
    path = OUT / "AI_Champions_Appendix_Q15_Risk_Register.pdf"
    doc = base_doc(path, "AI Champions Appendix Q15")
    content = [
        Paragraph("AI Champions Phase 1 - Appendix Q15", s["title"]),
        Paragraph("Risk register derived from the scored risk section of the application.", s["body"]),
        Spacer(1, 6),
    ]

    risks = [
        ["Risk", "Likelihood", "Impact", "Mitigation", "Residual"],
        [
            "LLM accuracy on complex polypharmacy cases stays below target",
            "High",
            "High",
            "Curriculum learning, expanded training data, ensemble fallback, safety layer catches unsafe output",
            "Medium",
        ],
        [
            "Safety rule coverage misses rare combinations",
            "Medium",
            "High",
            "DrugBank and guideline cross-check, pharmacist review, uncertain cases escalated to physician",
            "Low",
        ],
        [
            "Diraya retrospective data quality issues reduce validation reliability",
            "Medium",
            "Medium",
            "Month 1 data audit, cleaning, exclusion thresholds, large sample size preserves statistical power",
            "Low",
        ],
        [
            "Health-system adoption remains slow after technical validation",
            "Medium",
            "Medium",
            "Generate trust-focused evidence, co-design with practising clinician, de-risk in Phase 2 pilots",
            "Medium",
        ],
        [
            "Key-person dependency on Sami and Dr. Trigos",
            "Medium",
            "Medium",
            "Recruit ML Engineer, document validation methodology, use independent clinical reviewer support",
            "Medium",
        ],
    ]
    content.append(
        make_table(
            risks,
            [40 * mm, 17 * mm, 16 * mm, 76 * mm, 18 * mm],
            header_bg="#FCA5A5",
            font_size=7,
        )
    )
    content.append(Spacer(1, 10))
    content.append(Paragraph("Critical inputs", s["subtitle"]))
    for item in [
        "Retrospective Diraya data secured through Dr. Trigos",
        "Commercially available GPU infrastructure",
        "Open-weight foundation models such as Mistral or Llama",
    ]:
        content.append(Paragraph("• " + item, s["body"]))

    content.append(Spacer(1, 6))
    content.append(Paragraph("Regulatory boundary", s["subtitle"]))
    content.append(
        Paragraph(
            "Phase 1 remains pre-regulatory and focuses on feasibility. CE marking and clinical ethics approvals are deferred to later prospective deployment phases.",
            s["body"],
        )
    )

    doc.build(content)
    return path


def main():
    files = [
        build_architecture_pdf(),
        build_team_pdf(),
        build_gantt_pdf(),
        build_risk_pdf(),
    ]
    for path in files:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
