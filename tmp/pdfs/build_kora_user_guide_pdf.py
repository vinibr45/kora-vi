from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "output" / "pdf"
OUT_DIR.mkdir(parents=True, exist_ok=True)
PDF_PATH = OUT_DIR / "guia-didatico-kora.pdf"


def styles():
    base = getSampleStyleSheet()
    palette = {
        "ink": colors.HexColor("#17212B"),
        "muted": colors.HexColor("#536171"),
        "line": colors.HexColor("#D9E1EA"),
        "blue": colors.HexColor("#155E75"),
        "green": colors.HexColor("#0F766E"),
        "amber": colors.HexColor("#B45309"),
        "soft_blue": colors.HexColor("#EAF6FA"),
        "soft_green": colors.HexColor("#EAF7F4"),
        "soft_amber": colors.HexColor("#FFF3DF"),
    }
    base.add(
        ParagraphStyle(
            "TitleKora",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=32,
            textColor=palette["ink"],
            alignment=TA_CENTER,
            spaceAfter=12,
        )
    )
    base.add(
        ParagraphStyle(
            "SubtitleKora",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=12.5,
            leading=18,
            textColor=palette["muted"],
            alignment=TA_CENTER,
            spaceAfter=18,
        )
    )
    base.add(
        ParagraphStyle(
            "H1Kora",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=palette["blue"],
            spaceBefore=12,
            spaceAfter=8,
        )
    )
    base.add(
        ParagraphStyle(
            "H2Kora",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13.5,
            leading=17,
            textColor=palette["ink"],
            spaceBefore=8,
            spaceAfter=5,
        )
    )
    base.add(
        ParagraphStyle(
            "BodyKora",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=palette["ink"],
            spaceAfter=7,
        )
    )
    base.add(
        ParagraphStyle(
            "SmallKora",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            textColor=palette["muted"],
        )
    )
    base.add(
        ParagraphStyle(
            "CalloutKora",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=15,
            textColor=palette["blue"],
            spaceAfter=0,
        )
    )
    return base, palette


STYLES, PALETTE = styles()


def p(text, style="BodyKora"):
    return Paragraph(text, STYLES[style])


def bullet(text):
    return p(f"- {text}", "BodyKora")


def section(title):
    return p(title, "H1Kora")


def card(title, body, color):
    data = [[p(title, "CalloutKora")], [p(body, "BodyKora")]]
    t = Table(data, colWidths=[15.8 * cm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), color),
                ("BOX", (0, 0), (-1, -1), 0.75, PALETTE["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return KeepTogether([t, Spacer(1, 8)])


def table(rows, widths):
    converted = [[p(cell, "SmallKora") for cell in row] for row in rows]
    t = Table(converted, colWidths=widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALETTE["soft_blue"]),
                ("TEXTCOLOR", (0, 0), (-1, 0), PALETTE["ink"]),
                ("GRID", (0, 0), (-1, -1), 0.5, PALETTE["line"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(PALETTE["line"])
    canvas.line(1.8 * cm, height - 1.35 * cm, width - 1.8 * cm, height - 1.35 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(PALETTE["muted"])
    canvas.drawString(1.8 * cm, height - 1.1 * cm, "KORA - Guia didatico")
    canvas.drawRightString(width - 1.8 * cm, 1.05 * cm, f"Pagina {doc.page}")
    canvas.restoreState()


story = []

story.append(Spacer(1, 2.6 * cm))
story.append(p("Guia Didatico da KORA", "TitleKora"))
story.append(
    p(
        "Como entender, usar e evoluir a Knowledge-Orchestrated Reasoning Architecture.",
        "SubtitleKora",
    )
)
story.append(
    card(
        "Ideia central",
        "KORA organiza conhecimento, contexto, agentes, skills, ferramentas, avaliacoes e aprendizado para transformar tarefas em capacidades reutilizaveis.",
        PALETTE["soft_blue"],
    )
)
story.append(
    card(
        "Regra de ouro",
        "KORA Core define o metodo. O projeto define a realidade local.",
        PALETTE["soft_green"],
    )
)
story.append(PageBreak())

story.append(section("1. O Que E a KORA"))
story.append(
    p(
        "KORA significa Knowledge-Orchestrated Reasoning Architecture. Ela nao e um agente unico, nem uma colecao solta de prompts. E uma arquitetura reutilizavel para organizar trabalho agentico com fronteiras claras.",
    )
)
story.append(
    p(
        "Na pratica, KORA ajuda a decidir qual contexto usar, qual agente deve atuar, qual skill guia o processo, quais ferramentas sao permitidas, como avaliar a entrega e que aprendizados devem persistir.",
    )
)
story.append(
    card(
        "Para que serve",
        "Serve para projetos pessoais, negocios, produtos e ambientes de trabalho que precisam repetir bons processos sem misturar conhecimento geral com detalhes locais.",
        PALETTE["soft_amber"],
    )
)

story.append(section("2. Mapa Mental"))
rows = [
    ["Parte", "Funcao", "Exemplo"],
    ["Architecture", "Define principios, componentes, limites e fluxo.", "architecture/"],
    ["Knowledge", "Guarda conhecimento geral reutilizavel.", "knowledge/marketing/"],
    ["Projects", "Registra projetos e aponta para contexto local.", "projects/marcos-dev/"],
    ["Memory", "Guarda aprendizado operacional.", "memory/"],
    ["Context", "Seleciona o contexto certo para a tarefa.", "context/"],
    ["Orchestration", "Coordena tarefas, agentes, skills e tools.", "orchestration/"],
    ["Agents", "Definem papeis com escopo e responsabilidade.", "agents/kora-guide.md"],
    ["Skills", "Definem procedimentos reutilizaveis.", "skills/use-kora.md"],
    ["Tools", "Executam capacidades externas ou locais.", "tools/"],
    ["Evals", "Avaliam qualidade e riscos.", "evals/"],
    ["Learning", "Transforma resultados em melhoria.", "experiments/ e learning/"],
]
story.append(table(rows, [3.5 * cm, 7.0 * cm, 5.3 * cm]))
story.append(PageBreak())

story.append(section("3. Fluxo de Uso"))
story.append(p("O fluxo conceitual da KORA pode ser lido como uma esteira de decisao:"))
flow_rows = [
    ["Etapa", "Pergunta que ela responde"],
    ["Usuario / Tarefa", "O que precisa ser feito?"],
    ["Orquestracao", "Qual caminho resolve melhor?"],
    ["Camada de Contexto", "Quais fatos sao relevantes agora?"],
    ["Agente", "Quem deve assumir a responsabilidade?"],
    ["Skills e Tools", "Qual procedimento e quais capacidades executar?"],
    ["Resultado", "O que foi produzido?"],
    ["Avaliacao", "Isso esta bom, seguro e dentro do escopo?"],
    ["Learning", "O que deve virar memoria, conhecimento ou melhoria?"],
]
story.append(table(flow_rows, [4.5 * cm, 11.3 * cm]))
story.append(Spacer(1, 8))
story.append(
    card(
        "Importante",
        "Esse fluxo e um modelo arquitetural. Nem toda tarefa precisa passar por todas as etapas formalmente.",
        PALETTE["soft_blue"],
    )
)

story.append(section("4. Como Usar na Pratica"))
steps = [
    ("1. Nomeie a tarefa", "Explique o objetivo em uma frase simples."),
    ("2. Descubra o escopo", "Global pertence a KORA Core. Local pertence ao projeto. Hybrid usa padrao global com adaptacao local."),
    ("3. Selecione contexto", "Carregue apenas o necessario para a tarefa, evitando despejar todo o repositorio no raciocinio."),
    ("4. Escolha o caminho", "Execute direto, crie plano de capacidade, use skill existente, conecte projeto ou proponha integracao."),
    ("5. Produza e avalie", "Entregue o artefato e cheque qualidade, fronteiras, seguranca e utilidade."),
    ("6. Aprenda com o resultado", "Registre aprendizados somente quando forem uteis e bem classificados."),
]
for title, body in steps:
    story.append(p(title, "H2Kora"))
    story.append(p(body))

story.append(PageBreak())
story.append(section("5. Agentes Centrais"))
agent_rows = [
    ["Agente", "Quando usar"],
    ["KORA Guide", "Para explicar KORA, orientar uso e indicar o proximo workflow."],
    ["Capability Router", "Para decidir entre executar direto, criar skill, criar agente, usar tool, integrar ou automatizar."],
    ["KORA Architect", "Para proteger e evoluir a arquitetura sem poluir o Core."],
    ["Project Binder", "Para conectar um repositorio a KORA por meio de uma camada .kora/ local."],
    ["Context Curator", "Para selecionar e montar o contexto relevante de uma tarefa."],
    ["Knowledge Steward", "Para organizar conhecimento reutilizavel e proteger fronteiras."],
]
story.append(table(agent_rows, [4.5 * cm, 11.3 * cm]))

story.append(section("6. Caminhos Comuns"))
paths = [
    ["Situacao", "Workflow recomendado"],
    ["Quero entender a KORA", "Use KORA Guide ou skills/use-kora.md."],
    ["Quero conectar um projeto", "Use setup-kora-project ou bind-project-to-kora."],
    ["Quero criar conhecimento reutilizavel", "Use create-knowledge-entry e review-knowledge-entry."],
    ["Quero criar uma rotina repetivel", "Use create-skill antes de pensar em agente."],
    ["Quero automatizar algo", "Estabilize o processo, depois crie automation."],
    ["Quero integrar sistema externo", "Use assess-integration-need e depois create-integration."],
    ["Quero validar qualidade", "Crie ou rode evals."],
]
story.append(table(paths, [5.0 * cm, 10.8 * cm]))

story.append(PageBreak())
story.append(section("7. Erros Comuns"))
for item in [
    "Colocar detalhes especificos de um projeto dentro da KORA Core.",
    "Criar um agente quando uma skill simples resolveria.",
    "Criar integracao antes de testar um modo manual ou assistido.",
    "Automatizar um processo que ainda nao esta estavel.",
    "Tratar resultado de eval como verdade automatica.",
    "Promover aprendizado local para conhecimento global sem criterio.",
    "Carregar conhecimento demais em vez de selecionar contexto.",
]:
    story.append(bullet(item))

story.append(section("8. Mini Roteiro Para Uma Nova Tarefa"))
story.append(
    card(
        "Perguntas rapidas",
        "O que quero fazer? De qual projeto isso faz parte? Que contexto e necessario? Existe skill ou agente para isso? Precisa de ferramenta externa? Como vou avaliar se ficou bom? O que vale registrar depois?",
        PALETTE["soft_green"],
    )
)
story.append(p("Exemplo: gerar um PDF didatico sobre KORA."))
for item in [
    "Escopo: hybrid, porque usa KORA Core para explicar e gera um artefato local.",
    "Contexto: README, information-flow, boundaries, use-kora e bootstrap.",
    "Skill: PDF para criacao e verificacao visual.",
    "Output: PDF final em output/pdf/ e fonte renderizavel para revisoes futuras.",
    "Avaliacao: leitura, hierarquia visual, paginação, margens, legibilidade e ausencia de vazamento de segredos.",
]:
    story.append(bullet(item))

story.append(section("9. Onde Comecar"))
story.append(
    p(
        "Para estudar a KORA, comece por README.md, depois leia architecture/information-flow.md e architecture/boundaries.md. Em seguida, use skills/use-kora.md para decidir qual workflow seguir.",
    )
)
story.append(
    p(
        "Para trabalhar em um projeto real, mantenha a KORA Core limpa e registre as verdades locais no binding .kora/ do projeto.",
    )
)


doc = SimpleDocTemplate(
    str(PDF_PATH),
    pagesize=A4,
    rightMargin=1.8 * cm,
    leftMargin=1.8 * cm,
    topMargin=1.8 * cm,
    bottomMargin=1.6 * cm,
    title="Guia Didatico da KORA",
    author="KORA",
)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(PDF_PATH)
