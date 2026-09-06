from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "output" / "images" / "kora-instrucoes"
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
MARGIN = 110

COLORS = {
    "bg": "#F7FAFC",
    "ink": "#17212B",
    "muted": "#536171",
    "line": "#D9E1EA",
    "blue": "#155E75",
    "blue_soft": "#EAF6FA",
    "green": "#0F766E",
    "green_soft": "#EAF7F4",
    "amber": "#B45309",
    "amber_soft": "#FFF3DF",
    "white": "#FFFFFF",
}


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


F_TITLE = font(78, True)
F_SUBTITLE = font(34)
F_H2 = font(36, True)
F_BODY = font(30)
F_SMALL = font(24)
F_LABEL = font(26, True)


def wrap_text(text, width):
    return textwrap.wrap(text, width=width, break_long_words=False)


def draw_wrapped(draw, xy, text, fnt, fill, width, line_gap=10):
    x, y = xy
    lines = wrap_text(text, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def rounded(draw, box, fill, outline=None, width=3, radius=28):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def base(title, subtitle):
    img = Image.new("RGB", (W, H), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 18), fill=COLORS["blue"])
    draw.text((MARGIN, 70), "KORA", font=F_LABEL, fill=COLORS["blue"])
    draw.text((MARGIN, 120), title, font=F_TITLE, fill=COLORS["ink"])
    draw_wrapped(draw, (MARGIN, 220), subtitle, F_SUBTITLE, COLORS["muted"], 78, 8)
    draw.line((MARGIN, 305, W - MARGIN, 305), fill=COLORS["line"], width=3)
    return img, draw


def footer(draw):
    draw.text((MARGIN, H - 70), "Knowledge-Orchestrated Reasoning Architecture", font=F_SMALL, fill=COLORS["muted"])
    draw.text((W - MARGIN - 260, H - 70), "output/images/kora-instrucoes", font=F_SMALL, fill=COLORS["muted"])


def card(draw, x, y, w, h, title, body, accent, soft):
    rounded(draw, (x, y, x + w, y + h), COLORS["white"], COLORS["line"], 3, 26)
    draw.rectangle((x, y, x + 14, y + h), fill=accent)
    draw.text((x + 38, y + 30), title, font=F_H2, fill=accent)
    draw_wrapped(draw, (x + 38, y + 88), body, F_BODY, COLORS["ink"], 42, 8)
    draw.rounded_rectangle((x + w - 92, y + 26, x + w - 32, y + 86), radius=18, fill=soft)


def image_01():
    img, draw = base(
        "Como pensar com a KORA",
        "A KORA transforma tarefas em capacidades reutilizaveis sem misturar metodo, contexto e execucao.",
    )
    card(
        draw,
        MARGIN,
        360,
        790,
        250,
        "KORA Core",
        "Guarda arquitetura, principios, agentes, skills, tools, evals e conhecimento reutilizavel.",
        COLORS["blue"],
        COLORS["blue_soft"],
    )
    card(
        draw,
        W - MARGIN - 790,
        360,
        790,
        250,
        "Projeto Local",
        "Guarda a realidade especifica: identidade, stack, decisoes, operacao, arquivos e contexto vivo.",
        COLORS["green"],
        COLORS["green_soft"],
    )
    draw.line((W // 2 - 170, 500, W // 2 + 170, 500), fill=COLORS["amber"], width=8)
    draw.polygon([(W // 2 + 170, 500), (W // 2 + 130, 476), (W // 2 + 130, 524)], fill=COLORS["amber"])
    draw.text((W // 2 - 205, 540), "binding .kora/", font=F_LABEL, fill=COLORS["amber"])
    card(
        draw,
        370,
        690,
        1180,
        175,
        "Regra de ouro",
        "KORA Core define o metodo. O projeto define a realidade local.",
        COLORS["amber"],
        COLORS["amber_soft"],
    )
    footer(draw)
    return img


def image_02():
    img, draw = base(
        "Fluxo de uma tarefa",
        "Use este caminho para decidir o que carregar, quem atua, quais ferramentas entram e como aprender com o resultado.",
    )
    steps = [
        ("1", "Tarefa", "O que precisa ser feito?"),
        ("2", "Orquestracao", "Qual caminho resolve melhor?"),
        ("3", "Contexto", "Quais fatos importam agora?"),
        ("4", "Agente", "Quem assume a responsabilidade?"),
        ("5", "Skill + Tool", "Como executar com seguranca?"),
        ("6", "Eval + Learning", "Ficou bom? O que persiste?"),
    ]
    x0, y0 = MARGIN, 385
    box_w, box_h, gap = 520, 160, 55
    for idx, (num, title, body) in enumerate(steps):
        row = idx // 3
        col = idx % 3
        x = x0 + col * (box_w + gap)
        y = y0 + row * 230
        rounded(draw, (x, y, x + box_w, y + box_h), COLORS["white"], COLORS["line"], 3, 26)
        draw.ellipse((x + 28, y + 34, x + 92, y + 98), fill=COLORS["blue"])
        draw.text((x + 50, y + 48), num, font=F_LABEL, fill=COLORS["white"])
        draw.text((x + 120, y + 30), title, font=F_H2, fill=COLORS["ink"])
        draw_wrapped(draw, (x + 120, y + 82), body, F_SMALL, COLORS["muted"], 29, 6)
        if col < 2:
            draw.line((x + box_w + 12, y + 80, x + box_w + gap - 12, y + 80), fill=COLORS["amber"], width=5)
            draw.polygon([(x + box_w + gap - 12, y + 80), (x + box_w + gap - 36, y + 64), (x + box_w + gap - 36, y + 96)], fill=COLORS["amber"])
    footer(draw)
    return img


def image_03():
    img, draw = base(
        "Onde cada coisa mora",
        "A forca da KORA esta nas fronteiras: cada tipo de informacao tem um lugar proprio.",
    )
    columns = [
        ("Metodo", ["architecture/", "docs/", "orchestration/"], COLORS["blue"], COLORS["blue_soft"]),
        ("Conhecimento", ["knowledge/", "memory/", "learning/"], COLORS["green"], COLORS["green_soft"]),
        ("Execucao", ["agents/", "skills/", "tools/"], COLORS["amber"], COLORS["amber_soft"]),
        ("Projeto", ["projects/", ".kora/ local", "evals/"], "#7C3AED", "#F1EBFF"),
    ]
    x, y = MARGIN, 370
    col_w, col_h, gap = 385, 470, 40
    for title, items, accent, soft in columns:
        rounded(draw, (x, y, x + col_w, y + col_h), COLORS["white"], COLORS["line"], 3, 26)
        draw.rounded_rectangle((x + 28, y + 28, x + col_w - 28, y + 92), radius=18, fill=soft)
        draw.text((x + 50, y + 43), title, font=F_H2, fill=accent)
        yy = y + 135
        for item in items:
            draw.ellipse((x + 45, yy + 10, x + 61, yy + 26), fill=accent)
            draw.text((x + 82, yy), item, font=F_BODY, fill=COLORS["ink"])
            yy += 78
        x += col_w + gap
    footer(draw)
    return img


def image_04():
    img, draw = base(
        "Roteiro rapido de uso",
        "Antes de criar agentes, integracoes ou automacoes, passe por estas perguntas.",
    )
    prompts = [
        ("Objetivo", "O que quero produzir ou decidir?"),
        ("Escopo", "E global, local ou hybrid?"),
        ("Contexto", "Quais arquivos e fatos bastam?"),
        ("Capacidade", "Existe skill, agente ou tool pronta?"),
        ("Qualidade", "Como vou avaliar se ficou bom?"),
        ("Aprendizado", "O que merece ser registrado?"),
    ]
    x, y = MARGIN, 350
    for i, (title, body) in enumerate(prompts):
        row, col = divmod(i, 2)
        bx = x + col * 840
        by = y + row * 185
        rounded(draw, (bx, by, bx + 780, by + 135), COLORS["white"], COLORS["line"], 3, 24)
        draw.text((bx + 34, by + 26), title, font=F_H2, fill=COLORS["blue"])
        draw_wrapped(draw, (bx + 34, by + 78), body, F_SMALL, COLORS["ink"], 42, 6)
    card(
        draw,
        MARGIN,
        900,
        W - 2 * MARGIN,
        100,
        "Lembrete",
        "Execute simples quando for simples. Crie capacidade quando o processo se repetir.",
        COLORS["green"],
        COLORS["green_soft"],
    )
    footer(draw)
    return img


images = [
    ("01-como-pensar-com-kora.png", image_01()),
    ("02-fluxo-de-uma-tarefa.png", image_02()),
    ("03-onde-cada-coisa-mora.png", image_03()),
    ("04-roteiro-rapido-de-uso.png", image_04()),
]

for filename, img in images:
    path = OUT_DIR / filename
    img.save(path, "PNG", optimize=True)
    print(path)
