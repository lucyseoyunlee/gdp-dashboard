from html import escape

import streamlit as st


PROFILE = {
    "name": "이름을 적어주세요",
    "affiliation": "학교 · 회사 · 소속을 적어주세요",
    "intro": "좋아하는 것을 깊이 파고들고, 새로운 가능성을 찾아 나아갑니다.",
    "goal": "나만의 목표와 그 목표를 향해 가는 이유를 적어보세요.",
    "interests": ["관심사 하나", "관심사 둘", "관심사 셋", "관심사 넷", "관심사 다섯"],
    "travels": [
        (
            "여행 지역 하나",
            "나라 · 도시",
            "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1000&q=85",
        ),
        (
            "여행 지역 둘",
            "나라 · 도시",
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1000&q=85",
        ),
        (
            "여행 지역 셋",
            "나라 · 도시",
            "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=1000&q=85",
        ),
    ],
    "books": ["읽은 책 제목 하나", "읽은 책 제목 둘", "읽은 책 제목 셋"],
    "music": ["좋아하는 음악 하나", "좋아하는 음악 둘", "좋아하는 음악 셋"],
}

COLORS = [
    "#ff595e",
    "#ff924c",
    "#ffca3a",
    "#c5ca30",
    "#8ac926",
    "#52b788",
    "#2ec4b6",
    "#00bbf9",
    "#4895ef",
    "#4361ee",
    "#6a4c93",
    "#b5179e",
    "#f72585",
    "#f9844a",
]

st.set_page_config(page_title="나를 소개합니다", page_icon="🌈", layout="wide")

palette_html = "".join(
    f'<span style="--swatch:{color}"></span>' for color in COLORS
)
interest_html = "".join(
    f'<span class="interest" style="--tile:{COLORS[index % len(COLORS)]}">{escape(item)}</span>'
    for index, item in enumerate(PROFILE["interests"])
)
travel_html = "".join(
    f'<article class="travel-card" style="--tile:{COLORS[index % len(COLORS)]}">'
    f'<img src="{escape(image)}" alt="{escape(place)} 풍경">'
    f'<div class="travel-caption"><span>{index + 1:02d} / JOURNEY</span>'
    f'<h3>{escape(place)}</h3><p>{escape(detail)}</p></div></article>'
    for index, (place, detail, image) in enumerate(PROFILE["travels"])
)
books_html = "".join(
    f'<article class="list-item" style="--tile:{COLORS[(index + 2) % len(COLORS)]}">'
    f'<span class="item-index">BOOK / {index + 1:02d}</span><h3>{escape(book)}</h3></article>'
    for index, book in enumerate(PROFILE["books"])
)
music_html = "".join(
    f'<article class="list-item" style="--tile:{COLORS[(index + 8) % len(COLORS)]}">'
    f'<span class="item-index">SOUND / {index + 1:02d}</span><h3>{escape(track)}</h3></article>'
    for index, track in enumerate(PROFILE["music"])
)

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    :root {{
      --ink: #171717; --paper: #fffdf6; --muted: #656565;
      --red: #ff595e; --orange: #ff924c; --yellow: #ffca3a; --chartreuse: #c5ca30;
      --lime: #8ac926; --green: #52b788; --teal: #2ec4b6; --cyan: #00bbf9;
      --sky: #4895ef; --blue: #4361ee; --violet: #6a4c93; --magenta: #b5179e;
      --pink: #f72585; --tangerine: #f9844a;
    }}
    .stApp {{ background: var(--paper); color: var(--ink); }}
    [data-testid="stHeader"] {{ background: transparent; }}
    [data-testid="stToolbar"], #MainMenu, footer {{ visibility: hidden; }}
    .block-container {{ max-width: 1180px; padding: 1rem 2rem 3rem; }}
    .profile-page {{ font-family: 'Space Grotesk', 'Noto Sans KR', sans-serif; color: var(--ink); }}
    .color-rail {{ display: grid; grid-template-columns: repeat(14, 1fr); height: 10px; overflow: hidden; border-radius: 2px; }}
    .color-rail span {{ background: var(--swatch); }}
    .masthead {{ display: flex; justify-content: space-between; align-items: center; padding: 22px 0 18px; border-bottom: 1px solid var(--ink); font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: 0; }}
    .masthead strong {{ font-size: 14px; }}
    .masthead nav {{ display: flex; gap: 24px; }}
    .masthead a {{ color: var(--ink); text-decoration: none; }}
    .hero {{ padding: 66px 0 48px; border-bottom: 1px solid var(--ink); animation: enter .7s ease-out both; }}
    .eyebrow, .section-kicker {{ font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: 0; text-transform: uppercase; }}
    .eyebrow {{ display: flex; align-items: center; gap: 9px; }}
    .eyebrow span {{ width: 10px; height: 10px; border-radius: 50%; background: var(--pink); box-shadow: 12px 0 0 var(--yellow), 24px 0 0 var(--cyan); margin-right: 24px; }}
    .hero h1 {{ max-width: 100%; margin: 20px 0 8px; font-size: 68px; line-height: 1.02; letter-spacing: 0; overflow-wrap: anywhere; }}
    .affiliation {{ font-size: 20px; font-weight: 600; margin: 12px 0; }}
    .intro {{ max-width: 700px; margin: 24px 0 0; color: #454545; font-size: 18px; line-height: 1.7; }}
    .hero-stamp {{ display: inline-block; margin-top: 32px; padding: 10px 16px; background: var(--yellow); border: 1px solid var(--ink); border-radius: 2px; font: 11px 'DM Mono', monospace; transform: rotate(-2deg); }}
    .section {{ padding: 56px 0; border-bottom: 1px solid var(--ink); animation: enter .7s ease-out both; }}
    .section-heading {{ display: flex; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: 24px; }}
    .section-heading h2 {{ margin: 5px 0 0; font-size: 38px; line-height: 1.1; letter-spacing: 0; }}
    .section-heading p {{ margin: 0; color: var(--muted); font: 11px 'DM Mono', monospace; }}
    .goal-panel {{ position: relative; padding: 32px; background: var(--cyan); border: 1px solid var(--ink); box-shadow: 7px 7px 0 var(--ink); }}
    .goal-panel::after {{ content: '✳'; position: absolute; top: 16px; right: 22px; color: var(--pink); font-size: 42px; }}
    .goal-panel p {{ max-width: 820px; margin: 0; font-size: 26px; font-weight: 600; line-height: 1.5; }}
    .interests {{ display: flex; flex-wrap: wrap; gap: 12px; }}
    .interest {{ display: inline-flex; min-height: 56px; align-items: center; padding: 12px 20px; background: var(--tile); border: 1px solid var(--ink); border-radius: 2px; box-shadow: 3px 3px 0 var(--ink); font-size: 17px; font-weight: 700; }}
    .travel-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }}
    .travel-card {{ min-width: 0; overflow: hidden; border: 1px solid var(--ink); background: var(--tile); box-shadow: 4px 4px 0 var(--ink); }}
    .travel-card img {{ display: block; width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }}
    .travel-caption {{ min-height: 122px; padding: 16px; }}
    .travel-caption span, .item-index {{ font: 10px 'DM Mono', monospace; }}
    .travel-caption h3 {{ margin: 9px 0 2px; font-size: 20px; }}
    .travel-caption p {{ margin: 0; font-size: 13px; }}
    .two-up {{ display: grid; grid-template-columns: 1fr 1fr; gap: 42px; }}
    .subsection {{ min-width: 0; }}
    .subsection-heading {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 16px; border-bottom: 1px solid var(--ink); }}
    .subsection-heading h2 {{ font-size: 28px; margin: 0 0 12px; }}
    .subsection-heading span {{ font: 10px 'DM Mono', monospace; }}
    .item-list {{ display: grid; gap: 10px; }}
    .list-item {{ min-height: 102px; padding: 16px; background: var(--tile); border: 1px solid var(--ink); box-shadow: 3px 3px 0 var(--ink); }}
    .list-item h3 {{ margin: 13px 0 0; font-size: 18px; overflow-wrap: anywhere; }}
    .footer {{ display: flex; justify-content: space-between; padding: 24px 0 4px; font: 10px 'DM Mono', monospace; }}
    @keyframes enter {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @media (max-width: 760px) {{
      .block-container {{ padding: .5rem 1rem 2rem; }}
      .masthead {{ align-items: flex-start; gap: 14px; flex-direction: column; }}
      .masthead nav {{ flex-wrap: wrap; gap: 12px 18px; }}
      .hero {{ padding: 46px 0 36px; }}
      .hero h1 {{ font-size: 42px; }}
      .intro {{ font-size: 16px; }}
      .section {{ padding: 40px 0; }}
      .section-heading h2 {{ font-size: 31px; }}
      .section-heading {{ align-items: flex-start; flex-direction: column; }}
      .goal-panel {{ padding: 24px 20px; }}
      .goal-panel p {{ font-size: 21px; }}
      .travel-grid, .two-up {{ grid-template-columns: 1fr; }}
      .two-up {{ gap: 36px; }}
      .travel-card img {{ aspect-ratio: 16 / 10; }}
    }}
    @media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation-duration: .01ms !important; }} }}
    </style>
    <div class="profile-page">
      <div class="color-rail" aria-hidden="true">{palette_html}</div>
      <div class="masthead"><strong>INTRODUCTION / 01</strong><nav>
        <a href="#goal">GOAL</a><a href="#interests">INTERESTS</a>
        <a href="#travel">TRAVEL</a><a href="#favorites">FAVORITES</a>
      </nav><span>PERSONAL ARCHIVE · 2026</span></div>

      <header class="hero" id="top">
        <div class="eyebrow"><span></span> 안녕하세요, 저는</div>
        <h1>{escape(PROFILE['name'])}</h1>
        <p class="affiliation">{escape(PROFILE['affiliation'])}</p>
        <p class="intro">{escape(PROFILE['intro'])}</p>
        <span class="hero-stamp">A LITTLE BIT OF EVERYTHING ✳</span>
      </header>

      <section class="section" id="goal">
        <div class="section-heading"><div><div class="section-kicker">01 / THE DIRECTION</div><h2>지금 향하는 곳</h2></div><p>ONE GOAL, MANY STEPS</p></div>
        <div class="goal-panel"><p>{escape(PROFILE['goal'])}</p></div>
      </section>

      <section class="section" id="interests">
        <div class="section-heading"><div><div class="section-kicker">02 / THINGS I LOVE</div><h2>요즘의 관심사</h2></div><p>THESE MAKE ME, ME</p></div>
        <div class="interests">{interest_html}</div>
      </section>

      <section class="section" id="travel">
        <div class="section-heading"><div><div class="section-kicker">03 / OUT THERE</div><h2>발걸음이 닿았던 곳</h2></div><p>POSTCARDS FROM MY MAP</p></div>
        <div class="travel-grid">{travel_html}</div>
      </section>

      <section class="section" id="favorites">
        <div class="two-up">
          <div class="subsection"><div class="subsection-heading"><h2>읽은 책</h2><span>04 / BOOKS</span></div><div class="item-list">{books_html}</div></div>
          <div class="subsection"><div class="subsection-heading"><h2>좋아하는 음악</h2><span>05 / ON REPEAT</span></div><div class="item-list">{music_html}</div></div>
        </div>
      </section>
      <footer class="footer"><span>END OF INTRODUCTION</span><a href="#top" style="color:inherit">BACK TO TOP ↑</a></footer>
    </div>
    """,
    unsafe_allow_html=True,
)
