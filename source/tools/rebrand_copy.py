"""One-shot copy pass: ТАШМА (Macedonian) -> NECTRA (English). Fails loudly if any source string is missing."""
from pathlib import Path

PAGE = Path(__file__).resolve().parents[2] / "public" / "index.html"

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' fill='%23050403'/%3E%3Cpath d='M32 10l19 11v22L32 54 13 43V21z' "
           "fill='none' stroke='%23d9a441' stroke-width='2.5'/%3E%3C/svg%3E")

REPLACEMENTS = (
    ('<html lang="mk">', '<html lang="en">'),
    ("<title>ТАШМА · Природен органски мед</title>", "<title>NECTRA · Raw Organic Honey</title>"),
    ('content="ТАШМА. Суров, нефилтриран органски мед од ридовите на Македонија. Од кошница до тегла."',
     'content="NECTRA. Raw, unheated, unfiltered organic honey. From flower to jar. Untouched."'),
    # wordmark: clean sans, wide tracking (the hero/product h2 keep their size, change face)
    ("  .loader__mark { font-family: var(--serif); font-size: 40px; letter-spacing: 6px; }",
     "  .wordmark { font-family: var(--sans) !important; font-weight: 500; letter-spacing: 0.42em !important; padding-left: 0.42em; }\n"
     "  .loader__mark { font-family: var(--serif); font-size: 34px; letter-spacing: 6px; }"),
    ('<div class="loader__mark">ТАШМА</div>', '<div class="loader__mark wordmark">NECTRA</div>'),
    ('aria-label="Главна навигација"', 'aria-label="Main navigation"'),
    ('<a href="#top">ТАШМА</a>', '<a href="#top" class="wordmark">NECTRA</a>'),
    ('<a href="#newsletter">Контакт</a>', '<a href="#newsletter">Contact</a>'),
    # hero
    ('aria-label="Ритуал на медот"', 'aria-label="From flower to jar"'),
    ('<h1 class="hero-copy__brand" data-from="0.15" data-to="0.25">ТАШМА</h1>',
     '<h1 class="hero-copy__brand wordmark" data-from="0.15" data-to="0.25">NECTRA</h1>'),
    (">Природен органски мед.</p>", ">Raw organic honey.</p>"),
    (">ОД КОШНИЦА ДО ТЕГЛА</h2>", ">FROM FLOWER TO JAR</h2>"),
    (">Една капка. Илјада цветови.</p>", ">One drop. A thousand flowers.</p>"),
    # explainer
    ('aria-label="Потекло, процес, чистота"', 'aria-label="Origin, process, purity"'),
    ('alt="Мед се точи во тегла ТАШМА"', 'alt="Honey pouring into a NECTRA jar"'),
    ('alt="Медот се врти во теглата" data-panel="1"', 'alt="Honey swirling in the jar" data-panel="1"'),
    ('alt="Раце ја држат теглата ТАШМА" data-panel="2"', 'alt="Hands holding a NECTRA jar" data-panel="2"'),
    ("01 / Потекло</div>", "01 / Origin</div>"),
    ("<h2>ПОТЕКЛО</h2>", "<h2>ORIGIN</h2>"),
    ("„Од ридовите, не од фабрика.“", "“From wild hills, not a factory.”"),
    ("Меѓу ливадите и шумите, таму каде што пчелите сами го бираат цветот.",
     "Meadows and forests where the bees choose their own flowers. Nothing planted for them, nothing sprayed."),
    ("02 / Процес</div>", "02 / Process</div>"),
    ("<h2>ПРОЦЕС</h2>", "<h2>PROCESS</h2>"),
    ("„Полека, како што налага природата.“", "“Slow, the way nature intended.”"),
    ("Без загревање и без филтрирање под притисок. Медот се точи каков што е.",
     "Never heated. Never pressure-filtered. The honey is poured exactly as the hive made it."),
    ("03 / Чистота</div>", "03 / Purity</div>"),
    ("<h2>ЧИСТОТА</h2>", "<h2>PURITY</h2>"),
    ("„100% природно. Ништо повеќе.“", "“100% natural. Nothing else.”"),
    ("Само мед. Без додаден шеќер, без конзерванси, без боја.",
     "Just honey. No added sugar, no preservatives, no colouring."),
    # rail
    ('aria-label="Колекција"', 'aria-label="Collection"'),
    ('alt="Саќе под топла светлина"', 'alt="Honeycomb under warm light"'),
    ('<div class="eyebrow">Колекција</div>', '<div class="eyebrow">Collection</div>'),
    ("<h2>МЕДОТ ТАШМА</h2>", "<h2>NECTRA HONEY</h2>"),
    ('alt="Мед капе од саќето"', 'alt="Honey dripping from the comb"'),
    ("<h2>СУРОВ</h2>", "<h2>RAW</h2>"),
    ("Директно од саќето, недопрен.", "Straight from the comb. Untouched."),
    ('alt="Мед се врти во теглата">', 'alt="Honey swirling in the jar">'),
    ("<h2>НЕФИЛТРИРАН</h2>", "<h2>UNFILTERED</h2>"),
    ("Секоја капка ја чува природата во себе.", "Every drop keeps the pollen, enzymes and flavour of its flowers."),
    ('alt="Раце ја држат теглата ТАШМА">', 'alt="Hands holding a NECTRA jar">'),
    ("<h2>НАШ</h2>", "<h2>UNTOUCHED</h2>"),
    ("Од нашите кошници до вашата трпеза.", "From our hives to your table, and nothing in between."),
    # rituals
    ('aria-label="Ритуал"', 'aria-label="Ritual"'),
    (">ТОЧИ</h2>", ">POUR</h2>"),
    ("„Златна нишка, право од саќето.“", "“A golden thread, straight from the comb.”"),
    (">ЗЕМИ</h2>", ">TAKE</h2>"),
    ("„Полна лажица, без брзање.“", "“A full spoon. No hurry.”"),
    (">ВКУСИ</h2>", ">TASTE</h2>"),
    ("„Мигот кога сè застанува.“", "“The moment everything slows down.”"),
    # statement + columns
    ('aria-label="Изјава"', 'aria-label="Statement"'),
    ("<h2>Природна сладост,<br>недопрена.</h2>", "<h2>Natural sweetness,<br>untouched.</h2>"),
    ('<div class="eyebrow">ТАШМА. Од првата берба.</div>', '<div class="eyebrow">NECTRA. From the first harvest.</div>'),
    ('aria-label="Собран од дивото"', 'aria-label="Gathered from the wild"'),
    ("<h2>Собран од дивината.</h2>", "<h2>Gathered from the wild.</h2>"),
    # product
    ('aria-label="Производ"', 'aria-label="Product"'),
    ('alt="Тегла ТАШМА, природен органски мед"', 'alt="NECTRA jar, raw organic honey"'),
    ('<div class="eyebrow">Единствениот</div>', '<div class="eyebrow">The only one</div>'),
    ("<h2>ТАШМА</h2>", '<h2 class="wordmark">NECTRA</h2>'),
    ('<p class="product__sub">Природен органски мед</p>', '<p class="product__sub">Raw organic honey</p>'),
    ("Суров, нефилтриран мед од кошници во ридовите. Наточен полека, без загревање, за да ја задржи секоја нота од цветот од кој потекнува.",
     "Raw, unfiltered honey from hives in the hills. Poured slowly and never heated, so it keeps every note of the flowers it came from."),
    # newsletter
    ('aria-label="Билтен"', 'aria-label="Newsletter"'),
    ("<h2>Придружи се на ритуалот.</h2>", "<h2>Join the ritual.</h2>"),
    ("Нови берби, приказни од кошниците и рецепти. Само кога има што да се каже.",
     "New harvests, stories from the hives, and recipes. Only when there is something worth saying."),
    ('placeholder="твојата е-пошта"', 'placeholder="your email"'),
    ('aria-label="Е-пошта"', 'aria-label="Email"'),
    (">Пријави се</button>", ">Subscribe</button>"),
    ("Благодариме. Ќе се слушнеме кога ќе биде време за берба.", "Thank you. We'll be in touch when the next harvest is ready."),
    # footer
    ('<div class="footer__brand">ТАШМА</div>', '<div class="footer__brand wordmark">NECTRA</div>'),
    ("© 2026 ТАШМА · Природен органски мед · Сите права задржани", "© 2026 NECTRA · Raw organic honey · All rights reserved"),
)


def main():
    html = PAGE.read_text(encoding="utf-8")
    missing = [old for old, _ in REPLACEMENTS if old not in html]
    if missing:
        raise SystemExit("missing source strings:\n" + "\n".join(missing))
    for old, new in REPLACEMENTS:
        html = html.replace(old, new)
    marker = '<link rel="icon" href="'
    start = html.index(marker) + len(marker)
    end = html.index('"', start)
    html = html[:start] + FAVICON + html[end:]
    PAGE.write_text(html, encoding="utf-8")
    print(f"applied {len(REPLACEMENTS)} replacements")


if __name__ == "__main__":
    main()
