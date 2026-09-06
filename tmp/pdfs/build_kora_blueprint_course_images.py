from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "output" / "images" / "kora-mini-curso-blueprint"
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
M = 96

COLORS = {
    "bg": "#0B1220",
    "panel": "#101C2F",
    "panel2": "#13243A",
    "grid": "#1F3552",
    "line": "#4DA3FF",
    "cyan": "#67E8F9",
    "green": "#5EEAD4",
    "amber": "#FCD34D",
    "pink": "#F9A8D4",
    "purple": "#C4B5FD",
    "white": "#F8FAFC",
    "muted": "#A7B7CC",
    "danger": "#FDA4AF",
}


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except OSError:
            pass
    return ImageFont.load_default()


F = {
    "eyebrow": font(24, True),
    "title": font(70, True),
    "subtitle": font(32),
    "h1": font(42, True),
    "h2": font(32, True),
    "body": font(27),
    "small": font(22),
    "tiny": font(18),
    "mono": font(22),
}


def wrap(text, width):
    return textwrap.wrap(text, width=width, break_long_words=False)


def draw_wrapped(draw, x, y, text, fnt, fill, width, gap=8):
    for line in wrap(text, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def blueprint_base(title, subtitle, number):
    img = Image.new("RGB", (W, H), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    for x in range(0, W, 48):
        draw.line((x, 0, x, H), fill=COLORS["grid"], width=1)
    for y in range(0, H, 48):
        draw.line((0, y, W, y), fill=COLORS["grid"], width=1)
    for x in range(0, W, 240):
        draw.line((x, 0, x, H), fill="#294567", width=2)
    for y in range(0, H, 240):
        draw.line((0, y, W, y), fill="#294567", width=2)

    draw.rectangle((0, 0, W, 14), fill=COLORS["line"])
    draw.text((M, 58), f"KORA MINI CURSO  |  SLIDE {number:02d}", font=F["eyebrow"], fill=COLORS["cyan"])
    draw.text((M, 104), title, font=F["title"], fill=COLORS["white"])
    draw_wrapped(draw, M, 194, subtitle, F["subtitle"], COLORS["muted"], 86, 7)
    draw.line((M, 286, W - M, 286), fill=COLORS["line"], width=3)
    draw.text((M, H - 60), "Knowledge-Orchestrated Reasoning Architecture", font=F["tiny"], fill=COLORS["muted"])
    draw.text((W - M - 210, H - 60), "KORA Blueprint", font=F["tiny"], fill=COLORS["muted"])
    return img, draw


def box(draw, x, y, w, h, title, body="", color=None, fill=None):
    color = color or COLORS["cyan"]
    fill = fill or COLORS["panel"]
    draw.rounded_rectangle((x, y, x + w, y + h), radius=18, fill=fill, outline=color, width=3)
    draw.rectangle((x, y, x + 10, y + h), fill=color)
    draw.text((x + 28, y + 22), title, font=F["h2"], fill=color)
    if body:
        draw_wrapped(draw, x + 28, y + 72, body, F["body"], COLORS["white"], max(18, int(w / 18)), 7)


def small_box(draw, x, y, w, h, title, color):
    draw.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=COLORS["panel2"], outline=color, width=2)
    draw.text((x + 18, y + 18), title, font=F["small"], fill=COLORS["white"])


def arrow(draw, start, end, color=None):
    color = color or COLORS["amber"]
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=5)
    if abs(x2 - x1) >= abs(y2 - y1):
        if x2 >= x1:
            pts = [(x2, y2), (x2 - 24, y2 - 14), (x2 - 24, y2 + 14)]
        else:
            pts = [(x2, y2), (x2 + 24, y2 - 14), (x2 + 24, y2 + 14)]
    else:
        if y2 >= y1:
            pts = [(x2, y2), (x2 - 14, y2 - 24), (x2 + 14, y2 - 24)]
        else:
            pts = [(x2, y2), (x2 - 14, y2 + 24), (x2 + 14, y2 + 24)]
    draw.polygon(pts, fill=color)


def slide_01():
    img, d = blueprint_base(
        "KORA em Blueprint",
        "Um mini curso visual para entender estrutura, camadas, pastas, agentes, skills, ferramentas e aprendizado.",
        1,
    )
    box(d, 180, 390, 650, 250, "O problema", "Tarefas ficam soltas quando contexto, metodo e execucao se misturam.", COLORS["danger"])
    box(d, 1090, 390, 650, 250, "A resposta", "KORA cria uma arquitetura para transformar tarefas em capacidades reutilizaveis.", COLORS["green"])
    arrow(d, (850, 515), (1065, 515), COLORS["amber"])
    box(d, 430, 740, 1060, 130, "Regra de ouro", "KORA Core define o metodo. O projeto define a realidade local.", COLORS["cyan"])
    return img


def slide_02():
    img, d = blueprint_base(
        "Arquitetura macro",
        "A KORA separa responsabilidades para evitar que um agente vire um prompt gigante ou um deposito de tudo.",
        2,
    )
    layers = [
        ("User / Task", "Pedido inicial ou objetivo de trabalho.", COLORS["white"]),
        ("Orchestration", "Decide o caminho de execucao.", COLORS["cyan"]),
        ("Context Layer", "Seleciona conhecimento, projeto e memoria.", COLORS["green"]),
        ("Agent", "Assume um papel com limites claros.", COLORS["purple"]),
        ("Skills + Tools", "Procedimentos e capacidades executaveis.", COLORS["amber"]),
        ("Evaluation", "Checa qualidade, risco e aderencia.", COLORS["pink"]),
        ("Learning", "Decide o que deve persistir.", COLORS["green"]),
    ]
    y = 330
    for i, (name, body, color) in enumerate(layers):
        box(d, 540, y, 840, 82, name, "", color)
        d.text((820, y + 27), body, font=F["small"], fill=COLORS["muted"])
        if i < len(layers) - 1:
            arrow(d, (960, y + 88), (960, y + 122), COLORS["line"])
        y += 118
    return img


def slide_03():
    img, d = blueprint_base(
        "Camadas da KORA",
        "Pense em camadas: cada uma responde uma pergunta diferente e protege uma fronteira.",
        3,
    )
    items = [
        ("1. Conhecimento", "O que sabemos de forma reutilizavel?", COLORS["green"]),
        ("2. Contexto do projeto", "Como isso se aplica neste projeto?", COLORS["cyan"]),
        ("3. Memoria", "O que aprendemos operando?", COLORS["purple"]),
        ("4. Orquestracao", "Qual caminho usar agora?", COLORS["amber"]),
        ("5. Execucao", "Quem age e com quais ferramentas?", COLORS["pink"]),
    ]
    x = 180
    for idx, (title, body, color) in enumerate(items):
        y = 340 + idx * 118
        box(d, x + idx * 46, y, 1280 - idx * 92, 92, title, "", color)
        d.text((x + idx * 46 + 360, y + 31), body, font=F["small"], fill=COLORS["white"])
    box(d, 1260, 430, 430, 280, "Leitura correta", "A camada de cima nao deve engolir a de baixo. Ela usa, coordena ou avalia.", COLORS["cyan"])
    return img


def slide_04():
    img, d = blueprint_base(
        "Mapa de pastas",
        "O repositorio KORA Core e organizado por responsabilidade, nao por modismo tecnico.",
        4,
    )
    folders = [
        ("architecture/", "Principios, fronteiras e fluxo", COLORS["cyan"]),
        ("docs/", "Especificacoes formais", COLORS["cyan"]),
        ("knowledge/", "Conhecimento geral reutilizavel", COLORS["green"]),
        ("projects/", "Registro e ponte com projetos", COLORS["green"]),
        ("context/", "Selecao de contexto", COLORS["purple"]),
        ("memory/", "Aprendizado operacional", COLORS["purple"]),
        ("orchestration/", "Coordenacao de tarefas", COLORS["amber"]),
        ("agents/", "Contratos de papeis", COLORS["pink"]),
        ("skills/", "Procedimentos reutilizaveis", COLORS["pink"]),
        ("tools/", "Capacidades executaveis", COLORS["amber"]),
        ("integrations/", "Sistemas externos", COLORS["amber"]),
        ("automations/", "Rotinas repetiveis", COLORS["amber"]),
        ("evals/", "Criterios e cenarios de avaliacao", COLORS["green"]),
        ("experiments/", "Testes e aprendizado", COLORS["green"]),
    ]
    for i, (name, body, color) in enumerate(folders):
        col = i % 2
        row = i // 2
        x = 150 + col * 830
        y = 340 + row * 82
        small_box(d, x, y, 760, 58, name, color)
        d.text((x + 280, y + 19), body, font=F["tiny"], fill=COLORS["muted"])
    return img


def slide_05():
    img, d = blueprint_base(
        "KORA Core vs Projeto",
        "A fronteira mais importante: o Core guarda metodo; o projeto guarda a verdade local.",
        5,
    )
    box(d, 150, 360, 720, 420, "KORA Core", "Arquitetura\nConhecimento reutilizavel\nAgentes centrais\nSkills globais\nTools e integracoes propostas\nEvals reutilizaveis", COLORS["cyan"])
    box(d, 1050, 360, 720, 420, "Projeto + .kora/", "Identidade do projeto\nStack e convencoes\nDecisoes locais\nMemoria local\nAgentes locais\nSkills locais\nOutputs reais", COLORS["green"])
    arrow(d, (890, 565), (1030, 565), COLORS["amber"])
    d.text((900, 605), "binding", font=F["small"], fill=COLORS["amber"])
    box(d, 420, 835, 1080, 96, "Pergunta de escopo", "Isso e uma regra reutilizavel ou uma verdade deste projeto especifico?", COLORS["amber"])
    return img


def slide_06():
    img, d = blueprint_base(
        "Agentes centrais",
        "Agentes sao papeis com fronteiras, contexto permitido, skills e responsabilidades de saida.",
        6,
    )
    agents = [
        ("KORA Guide", "Explica e orienta o uso."),
        ("Capability Router", "Escolhe o melhor caminho."),
        ("KORA Architect", "Protege a arquitetura."),
        ("Project Binder", "Conecta projetos via .kora/."),
        ("Context Curator", "Seleciona o contexto certo."),
        ("Knowledge Steward", "Cuida do conhecimento reutilizavel."),
    ]
    cx, cy, r = 960, 610, 115
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=COLORS["panel2"], outline=COLORS["cyan"], width=4)
    d.text((cx - 63, cy - 18), "KORA", font=F["h1"], fill=COLORS["white"])
    positions = [(210, 360), (690, 330), (1170, 330), (1410, 560), (930, 810), (330, 700)]
    colors = [COLORS["cyan"], COLORS["green"], COLORS["purple"], COLORS["amber"], COLORS["pink"], COLORS["green"]]
    for (title, body), (x, y), color in zip(agents, positions, colors):
        box(d, x, y, 390, 130, title, body, color)
        arrow(d, (x + 195, y + 130), (cx, cy), color)
    return img


def slide_07():
    img, d = blueprint_base(
        "Skills, tools e integracoes",
        "Essas tres coisas parecem parecidas, mas cada uma tem um papel diferente.",
        7,
    )
    box(d, 165, 380, 460, 330, "Skill", "Procedimento reutilizavel.\nExemplo: select-context, use-kora, create-integration.", COLORS["green"])
    box(d, 730, 380, 460, 330, "Tool", "Capacidade executavel.\nExemplo: gerar imagem, renderizar PDF, chamar API.", COLORS["amber"])
    box(d, 1295, 380, 460, 330, "Integration", "Ponte com sistema externo.\nExemplo: Claude, Canva, GitHub, Google Drive.", COLORS["cyan"])
    arrow(d, (625, 545), (710, 545), COLORS["line"])
    arrow(d, (1190, 545), (1275, 545), COLORS["line"])
    box(d, 375, 800, 1170, 110, "Sequencia saudavel", "Primeiro estabilize o procedimento. Depois crie tool. Depois automatize.", COLORS["purple"])
    return img


def slide_08():
    img, d = blueprint_base(
        "Automacoes e qualidade",
        "Automacao so entra bem quando o workflow ja e claro, repetivel e avaliavel.",
        8,
    )
    steps = [
        ("Processo manual", COLORS["cyan"]),
        ("Skill estavel", COLORS["green"]),
        ("Tool aprovada", COLORS["amber"]),
        ("Automation", COLORS["pink"]),
        ("Eval", COLORS["purple"]),
        ("Learning", COLORS["green"]),
    ]
    x, y = 170, 500
    for i, (name, color) in enumerate(steps):
        box(d, x + i * 285, y, 230, 120, name, "", color)
        if i < len(steps) - 1:
            arrow(d, (x + i * 285 + 235, y + 60), (x + (i + 1) * 285 - 10, y + 60), COLORS["line"])
    box(d, 360, 750, 1200, 130, "Criterio", "Se nao da para explicar, revisar e parar com seguranca, ainda nao esta pronto para automatizar.", COLORS["amber"])
    return img


def slide_09():
    img, d = blueprint_base(
        "Como iniciar uma tarefa",
        "Use este checklist antes de pedir para a KORA agir em um projeto real.",
        9,
    )
    checks = [
        ("1", "Objetivo", "O que precisa ser produzido?"),
        ("2", "Projeto", "Qual repositorio ou contexto local?"),
        ("3", "Escopo", "Core, local ou hybrid?"),
        ("4", "Contexto", "Quais arquivos realmente importam?"),
        ("5", "Capacidade", "Skill, agente, tool, integracao ou automacao?"),
        ("6", "Validacao", "Como saber que ficou bom?"),
    ]
    for i, (num, title, body) in enumerate(checks):
        row, col = divmod(i, 3)
        x = 150 + col * 570
        y = 360 + row * 245
        d.ellipse((x, y, x + 78, y + 78), fill=COLORS["line"])
        d.text((x + 27, y + 18), num, font=F["h2"], fill=COLORS["bg"])
        box(d, x + 105, y - 15, 405, 125, title, body, COLORS["cyan" if i % 2 == 0 else "green"])
    return img


def slide_10():
    img, d = blueprint_base(
        "Exemplo: gerar um PDF didatico",
        "Um caso real mostra como a arquitetura vira trabalho concreto.",
        10,
    )
    steps = [
        ("Pedido", "Documento PDF para ensinar KORA."),
        ("Contexto", "README, fluxo, fronteiras, use-kora."),
        ("Skill", "PDF: criar, renderizar, validar."),
        ("Output", "guia-didatico-kora.pdf."),
        ("Learning", "PDFs precisam de fonte renderizavel e QA visual."),
    ]
    y = 350
    for i, (title, body) in enumerate(steps):
        color = [COLORS["cyan"], COLORS["green"], COLORS["amber"], COLORS["pink"], COLORS["purple"]][i]
        box(d, 310, y, 1300, 88, title, "", color)
        d.text((560, y + 28), body, font=F["small"], fill=COLORS["white"])
        if i < len(steps) - 1:
            arrow(d, (960, y + 92), (960, y + 122), COLORS["line"])
        y += 124
    return img


def slide_11():
    img, d = blueprint_base(
        "Resumo do mini curso",
        "Se lembrar destes cinco pontos, voce ja consegue usar a KORA sem baguncar a arquitetura.",
        11,
    )
    points = [
        "KORA e arquitetura, nao apenas prompt.",
        "Core guarda metodo; projeto guarda realidade.",
        "Agente tem papel; skill tem procedimento; tool executa.",
        "Automacao vem depois que o processo esta estavel.",
        "Learning so vira conhecimento quando passa por criterio.",
    ]
    y = 365
    for i, point in enumerate(points, 1):
        color = [COLORS["cyan"], COLORS["green"], COLORS["amber"], COLORS["pink"], COLORS["purple"]][i - 1]
        d.ellipse((250, y - 4, 320, y + 66), fill=color)
        d.text((275, y + 13), str(i), font=F["h2"], fill=COLORS["bg"])
        d.text((365, y + 12), point, font=F["h2"], fill=COLORS["white"])
        y += 120
    box(d, 420, 890, 1080, 90, "Proximo passo", "Escolha uma tarefa real e deixe a KORA roteirizar o caminho.", COLORS["green"])
    return img


slides = [
    ("01-kora-em-blueprint.png", slide_01()),
    ("02-arquitetura-macro.png", slide_02()),
    ("03-camadas-da-kora.png", slide_03()),
    ("04-mapa-de-pastas.png", slide_04()),
    ("05-core-vs-projeto.png", slide_05()),
    ("06-agentes-centrais.png", slide_06()),
    ("07-skills-tools-integracoes.png", slide_07()),
    ("08-automacoes-e-qualidade.png", slide_08()),
    ("09-como-iniciar-uma-tarefa.png", slide_09()),
    ("10-exemplo-pdf-didatico.png", slide_10()),
    ("11-resumo-do-mini-curso.png", slide_11()),
]

for name, img in slides:
    path = OUT_DIR / name
    img.save(path, "PNG", optimize=True)
    print(path)
