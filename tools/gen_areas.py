"""4つのエリアページ (area-*.html) を生成する。出力は静的HTML。"""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
SITE = "https://kawaitest.github.io/cat-panit-island/"  # 公開URL（OGP・canonical用）

AREAS = [
    {"id": 1, "slug": "harbor", "name": "ハーバー・ニャウン", "en": "HARBOR NYAOWN"},
    {"id": 2, "slug": "forest", "name": "マタタビの森", "en": "MATATABI FOREST"},
    {"id": 3, "slug": "hills", "name": "キャットタワー・ヒルズ", "en": "CAT TOWER HILLS"},
    {"id": 4, "slug": "kotatsu", "name": "こたつビレッジ", "en": "KOTATSU VILLAGE"},
]
PIN = {1: (300, 320), 2: (196, 236), 3: (310, 160), 4: (420, 240)}
ZONE = {1: (300, 330, 120, 52), 2: (186, 240, 82, 92), 3: (310, 120, 130, 82), 4: (430, 245, 84, 92)}

ICON = {
    "coaster": '<path d="M4 40 C 14 6, 22 6, 30 26 S 46 44, 56 12" fill="none" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/>',
    "wheel": '<circle cx="30" cy="24" r="18" fill="none" stroke="var(--ink)" stroke-width="4"/><path d="M30 24 L18 46 M30 24 L42 46" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/><circle cx="30" cy="6" r="4" fill="var(--paw)"/><circle cx="48" cy="24" r="4" fill="var(--paw)"/><circle cx="12" cy="24" r="4" fill="var(--paw)"/>',
    "fall": '<rect x="25" y="2" width="10" height="44" rx="3" fill="var(--ink)"/><path d="M20 10 L24 2 L28 10 M32 10 L36 2 L40 10" fill="var(--ink)"/><rect x="16" y="22" width="28" height="8" rx="3" fill="var(--tabby)"/>',
    "boat": '<path d="M6 30 H54 L46 42 H14 Z" fill="var(--ink)"/><path d="M4 46 q7 -5 13 0 t13 0 t13 0 t13 0" fill="none" stroke="var(--sea)" stroke-width="3"/>',
    "ghost": '<path d="M14 46 V22 a16 16 0 0 1 32 0 V46 l-6 -5 -5 5 -5 -5 -5 5 -5 -5 Z" fill="var(--ink)"/><circle cx="24" cy="24" r="3" fill="var(--tabby)"/><circle cx="36" cy="24" r="3" fill="var(--tabby)"/>',
    "cat": '<path d="M12 44 L14 10 L24 20 Q30 18 36 20 L46 10 L48 44 Q30 52 12 44 Z" fill="var(--ink)"/><circle cx="23" cy="32" r="3" fill="var(--surface)"/><circle cx="37" cy="32" r="3" fill="var(--surface)"/>',
}

WAGON = {"genre": "フードワゴン", "name": "肉球チュロスワゴン", "sig": "肉球チュロス", "yen": "500円",
         "desc": "肉球のかたちのチュロス。シナモン、いちごミルク、季節限定の3種類。このエリアにも1台出ています。",
         "feats": ["食べ歩き", "季節限定あり"], "price": "400〜700円", "hours": "開園〜閉園"}

CONTENT = {
    1: {
        "walk": "1",
        "lead": "フェリーを降りるとすぐの、島の玄関口。カラフルな港町に、ショップと食堂、観覧車、そして本物のスタッフ猫に会える「ねこ事務所」が並びます。朝いちばんと帰りぎわに立ち寄りたいエリアです。",
        "highlights": [
            ("スタッフ猫に会える「ねこ事務所」", "園で暮らす6匹のスタッフ猫が毎日11:00〜15:00に出勤。窓ごしに、お昼寝やお仕事のようすを見られます。"),
            ("肉球ゴンドラの観覧車", "ニャンダフル・ホイールの頂上からは、島がねこのかたちをしているのがよくわかります。夕暮れどきが特におすすめ。"),
            ("パレードのスタート地点", "14:00のハーバーパレードは中央桟橋から出発。桟橋前の広場は、出発の瞬間をいちばん近くで見られる場所です。"),
        ],
        "rides": [
            ("ニャンダフル・ホイール", "観覧車", 0, 1, "約15分", "肉球型のゴンドラから、島のねこのかたちが見渡せます。", "wheel"),
        ],
        "shops": [
            {"genre": "レストラン", "name": "ねこ船長のシーフード食堂", "sig": "ねこまんま海鮮丼", "yen": "2,200円",
             "desc": "その朝ねこ岬港にあがった魚を使う、島でいちばん大きな食堂。窓から桟橋とフェリーが見えます。",
             "feats": ["屋内席180", "お子さまメニュー", "予約可"], "price": "1,600〜2,800円", "hours": "11:00〜閉園1時間前"},
            {"genre": "ベーカリー・カフェ", "name": "毛糸玉ベーカリー＆カフェ", "sig": "毛糸玉メロンパン", "yen": "450円",
             "desc": "毛糸玉のようにくるくる巻いた生地のメロンパン。朝いちばんの焼きたては開園から30分ほどで売り切れます。",
             "feats": ["テイクアウト", "テラス席", "朝食メニュー"], "price": "300〜1,200円", "hours": "開園〜閉園"},
            WAGON,
        ],
        "shows": [
            ("11:00", "ねこ船長のごあいさつ", "中央桟橋　約15分"),
            ("14:00", "ハーバーパレード「ニャー・ボヤージュ」", "中央桟橋を出発し、マタタビの森へ　約30分"),
            ("17:30", "肉球ナイトイルミネーション", "港の灯台と桟橋がライトアップ　閉園まで"),
        ],
        "facilities": [
            ("ねこ事務所", "スタッフ猫に会える建物。11:00〜15:00。抱っこやおやつはご遠慮ください。"),
            ("インフォメーション", "メインゲートすぐ。迷子・落とし物・ベビーカー貸出（仮）の受付。"),
            ("おみやげショップ「にくきゅう商店」", "島でいちばん大きなショップ。閉園30分後まで営業（仮）。"),
            ("フェリー乗り場", "20分おきに運航。島発の最終便は閉園30分後です。"),
        ],
        "tips": [
            ("メロンパンは開園直後に", "毛糸玉メロンパンの焼きたては、開園から30分ほどで売り切れることが多いです。"),
            ("おみやげは帰りにまとめて", "ショップは閉園後もしばらく開いています。荷物になるものは最後に買うのがおすすめです。"),
            ("帰りのフェリーは1本早めに", "閉園直後の便は混み合います。イルミネーションを観覧車から見て、1本早い便で帰るのもおすすめです。"),
        ],
    },
    2: {
        "walk": "5",
        "lead": "マタタビの香る川と森が広がる、ファミリー向けのエリア。リバーボートや生け垣の大迷路、はじめてのコースターにぴったりのライドがあり、お弁当を広げられるピクニック広場もあります。",
        "highlights": [
            ("はじめてのコースターに", "ネズミおいかけライドは身長100cmから。スピードもひかえめで、コースターデビューにぴったりです。"),
            ("木の上のねこを探そう", "マタタビ・リバーボートの岸辺には、木の上や茂みにねこの像が隠れています。全部で何匹見つけられるかな。"),
            ("お弁当OKのピクニック広場", "芝生の広場は、持ち込みのお弁当も食べられる休憩スポット。デリのピクニックセットも人気です。"),
        ],
        "rides": [
            ("ネズミおいかけライド", "ファミリーコースター", 100, 2, "約2分", "森を逃げまわるネズミを追いかける、はじめてのコースターにぴったりの一台。", "coaster"),
            ("マタタビ・リバーボート", "ボートライド", 0, 1, "約12分", "マタタビの香る川をゆっくり一周。岸辺の木の上にねこが隠れています。", "boat"),
            ("迷い猫ラビリンス", "迷路", 0, 1, "約20分", "迷子の子ねこ5匹を見つけてゴールを目指す、生け垣の大迷路。", "cat"),
        ],
        "shops": [
            {"genre": "デリ・テイクアウト", "name": "マタタビ・ピクニックデリ", "sig": "森のきのこホットサンド", "yen": "900円",
             "desc": "ピクニック広場のとなりにあるデリ。バスケット入りの「ピクニックセット」はふたり分から注文できます。",
             "feats": ["テイクアウト", "ピクニックセット", "ベジメニュー"], "price": "500〜3,200円", "hours": "10:30〜17:00"},
            WAGON,
        ],
        "shows": [
            ("14:15", "ハーバーパレード「ニャー・ボヤージュ」通過", "森の入口〜ピクニック広場　パレードの終点です"),
            ("17:30", "肉球ナイトイルミネーション", "川沿いの小道に肉球の灯りがともります　閉園まで"),
        ],
        "facilities": [
            ("ピクニック広場", "芝生とベンチのある休憩エリア。お弁当の持ち込みOK。"),
            ("森のトイレ・おむつ替え", "ピクニック広場の奥。おむつ替え台があります（仮）。"),
            ("コインロッカー", "迷路の入口そば。リバーボートで濡れたくないものを預けられます（仮）。"),
        ],
        "tips": [
            ("お昼はピクニック広場で", "土日祝の12:00〜13:30はレストランが混み合います。広場でお弁当を食べればゆっくりできます。"),
            ("パレードは森で待つと見やすい", "ハーバー側より森の沿道のほうが空いていて、お子さまも前で見やすいです。"),
            ("迷路は午前中に", "午後は日差しが強くなります。迷い猫ラビリンスは涼しい午前中がおすすめです。"),
        ],
    },
    3: {
        "walk": "10",
        "lead": "ねこの耳にあたる二つの丘に、島でいちばんのスリルライドが集まるエリア。高さ60mのキャットタワーから落ちるフリーフォールと、爪とぎ板のレールを駆け抜けるコースターが待っています。",
        "highlights": [
            ("高さ60mのキャットタワー", "島でいちばん高い建物。キャットタワー・ドロップは、ねこが飛び降りるように一気に落下します。"),
            ("最高時速90kmのコースター", "ツメとぎコースターは、爪とぎ板のようなギザギザのレールを駆け抜ける島いちばんの絶叫ライドです。"),
            ("夜はもっとこわいゴーストハウス", "夜鳴きゴーストハウスは、日が暮れると演出が変わります。光る目に見つめられる、真夜中の路地裏へ。"),
        ],
        "rides": [
            ("キャットタワー・ドロップ", "フリーフォール", 130, 3, "約2分", "高さ60mのキャットタワーのてっぺんから、ねこが飛び降りるように一気に落下。", "fall"),
            ("ツメとぎコースター", "ジェットコースター", 120, 3, "約3分", "爪とぎ板のギザギザ型レールを最高時速90kmで駆け抜けます。", "coaster"),
            ("夜鳴きゴーストハウス", "お化け屋敷", 0, 2, "約10分", "真夜中の路地裏で、光る目があなたを見ています。小学生未満は保護者同伴。", "ghost"),
        ],
        "shops": [
            {"genre": "ハンバーガー", "name": "キャットタワー・グリル", "sig": "タワーバーガーとツメとぎポテト", "yen": "1,600円",
             "desc": "パティを3段に重ねたタワーバーガーに、ギザギザにカットしたポテトがつきます。絶叫ライドのあとの腹ごしらえに。",
             "feats": ["屋内席120", "モバイルオーダー"], "price": "1,000〜2,000円", "hours": "11:00〜閉園"},
            WAGON,
        ],
        "shows": [
            ("17:30", "肉球ナイトイルミネーション", "キャットタワーが肉球色にライトアップ　閉園まで"),
        ],
        "facilities": [
            ("ライドフォト受付", "キャットタワー・ドロップとツメとぎコースターの落下の瞬間の写真を買えます（仮）。"),
            ("手荷物置き場", "各ライドの乗り場に無料の荷物棚があります。帽子やメガネは預けてください。"),
            ("展望デッキ", "二つの丘をつなぐ橋の上。島全体と本土のねこ岬港が見渡せます（仮）。"),
        ],
        "tips": [
            ("人気ライドは朝いちばんに", "開園直後はハーバー側に人が集まります。まっすぐヒルズへ向かうと待ち時間が短くなります。"),
            ("強風の日は休止することがあります", "キャットタワー・ドロップは風が強いと運休します。当日の運営状況はインフォメーションで確認してください。"),
            ("お昼はモバイルオーダーで", "キャットタワー・グリルはモバイルオーダーで並ばずに受け取れます。"),
        ],
    },
    4: {
        "walk": "8",
        "lead": "小さなお子さま向けの、あたたかい屋内エリア。毛糸玉のコーヒーカップ、こたつのメリーゴーラウンド、巨大ダンボールの秘密基地。全席こたつの茶屋もあって、雨の日でも寒い日でもゆっくり遊べます。",
        "highlights": [
            ("ぜんぶ屋内、雨でもOK", "アトラクションもシアターも茶屋も、すべて屋根の下。雨の日や冬の寒い日にもおすすめです。"),
            ("小さなお子さまにやさしい", "身長制限のないライドが中心。授乳室やおむつ替えの場所も、こたつ茶屋のとなりにあります。"),
            ("12月1日から「こたつ祭り」", "冬季イベント「こたつ祭り」がこたつビレッジを中心に開催されます。詳細はお知らせで発表します。"),
        ],
        "rides": [
            ("毛糸玉コーヒーカップ", "回転ライド", 0, 1, "約3分", "ころころ転がる毛糸玉のカップ。ハンドルを回すほど速くなります。", "cat"),
            ("こたつメリーゴーラウンド", "メリーゴーラウンド", 0, 1, "約3分", "こたつの周りを、まるくなったねこたちがゆっくり回ります。", "cat"),
            ("ダンボール探検隊", "屋内プレイエリア", 90, 1, "自由", "巨大ダンボールのトンネルと秘密基地。対象は身長90cm以上・小学生まで。", "cat"),
        ],
        "shops": [
            {"genre": "和食・甘味", "name": "こたつ茶屋", "sig": "こたつ鍋うどんとみかん大福", "yen": "1,400円",
             "desc": "全席こたつのお座敷で、ひと休みできる茶屋。小さなお子さま連れでもゆっくり座れます。",
             "feats": ["お座敷", "お子さまメニュー", "授乳室となり"], "price": "600〜1,800円", "hours": "11:00〜18:00"},
            WAGON,
        ],
        "shows": [
            ("16:00", "こたつシアター「みかんの大冒険」", "屋内シアター　約20分"),
            ("17:30", "肉球ナイトイルミネーション", "村の屋根に肉球の灯りがともります　閉園まで"),
        ],
        "facilities": [
            ("授乳室・おむつ替え", "こたつ茶屋のとなり。調乳用のお湯もあります（仮）。"),
            ("ベビーカー置き場", "各アトラクションの入口にあります。"),
            ("屋内シアター", "約200席（仮）。ショーの30分前から入場できます。"),
        ],
        "tips": [
            ("シアターは15:30から並ぶと安心", "こたつシアターは座席に限りがあります。開演の30分前から入場できます。"),
            ("こたつ茶屋でひと休み", "歩き疲れたら、こたつのお座敷で休憩を。靴を脱いで足を伸ばせます。"),
            ("雨の日は混み合います", "雨の日は島じゅうのお客さまが集まります。午前中の早い時間がおすすめです。"),
        ],
    },
}

LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true">
        <circle cx="20" cy="20" r="20" fill="var(--sea)"/>
        <path d="M9 30 L10 12 L16 18 Q20 16.5 24 18 L30 12 L31 30 Q20 35 9 30 Z" fill="var(--surface)"/>
        <circle cx="15.5" cy="24" r="1.7" fill="var(--ink)"/><circle cx="24.5" cy="24" r="1.7" fill="var(--ink)"/>
        <path d="M18.6 27.2 L21.4 27.2 L20 28.6 Z" fill="var(--paw)"/>
      </svg>'''

LAND = "M118 268 C 100 186, 158 128, 226 118 L 246 46 L 292 108 Q 310 106 330 108 L 376 46 L 392 120 C 470 134, 512 204, 492 276 C 472 346, 384 372, 300 368 C 202 366, 134 330, 118 268 Z"


def href(a):
    return f"area-{a['slug']}.html"


def paws(n):
    return f'<span class="paws" aria-label="スリル度{n}">{"●" * n}<span class="off">{"●" * (3 - n)}</span></span>'


def map_svg(cur):
    zx, zy, rx, ry = ZONE[cur]
    parts = [f'''<svg viewBox="0 0 600 420" role="img" aria-label="島のエリアマップ。現在のエリア：{AREAS[cur-1]['name']}">
          <defs><clipPath id="island"><path d="{LAND}"/></clipPath></defs>
          <rect class="sea" x="0" y="0" width="600" height="420" rx="18"/>
          <path class="tail" d="M478 300 C 545 300, 565 355, 520 378"/>
          <path class="tail-in" d="M478 300 C 545 300, 565 355, 520 378"/>
          <path class="land" d="{LAND}"/>
          <ellipse class="zone" cx="{zx}" cy="{zy}" rx="{rx}" ry="{ry}" clip-path="url(#island)"/>
          <rect class="pier" x="286" y="366" width="12" height="40" rx="3"/>
          <text class="ferry" x="306" y="402">フェリー乗り場</text>''']
    for a in AREAS:
        x, y = PIN[a["id"]]
        lbl_cls = "lbl" if a["id"] == cur else "lbl dim"
        if a["id"] == cur:
            parts.append(f'<g class="pin here" aria-current="page"><circle cx="{x}" cy="{y}" r="22"/><text x="{x}" y="{y+5}">{a["id"]}</text></g>')
        else:
            parts.append(f'<a class="pin" href="{href(a)}" aria-label="エリア{a["id"]} {a["name"]}へ"><circle cx="{x}" cy="{y}" r="18"/><text x="{x}" y="{y+5}">{a["id"]}</text></a>')
        parts.append(f'<text class="{lbl_cls}" x="{x}" y="{y+38}">{a["name"]}</text>')
    parts.append("</svg>")
    return "\n          ".join(parts)


def page(a):
    c = CONTENT[a["id"]]
    aid = a["id"]
    cur_attr = ' aria-current="page"'
    nav_areas = "\n".join(
        f'        <li><a href="{href(x)}"{cur_attr if x["id"] == aid else ""}>{x["name"]}</a></li>' for x in AREAS)

    highlights = "\n".join(f'          <li><h3>{t}</h3><p>{d}</p></li>' for t, d in c["highlights"])

    rides = []
    for name, kind, mn, thrill, dur, desc, ic in c["rides"]:
        rides.append(f'''        <article class="ride" data-min="{mn}">
          <div class="ride-art"><svg viewBox="0 0 60 50" aria-hidden="true">{ICON[ic]}</svg></div>
          <div class="ride-body"><h3>{name}</h3><p class="kind">{kind}</p></div>
          <p class="desc">{desc}</p>
          <div>
            <dl>
              <dt>身長制限</dt><dd>{f"{mn}cm以上" if mn else "なし"}</dd>
              <dt>スリル度</dt><dd>{paws(thrill)}</dd>
              <dt>所要時間</dt><dd>{dur}</dd>
            </dl>
            <p class="verdict" aria-live="polite"></p>
          </div>
        </article>''')

    shops = []
    for s in c["shops"]:
        feats = "".join(f"<li>{f}</li>" for f in s["feats"])
        shops.append(f'''        <article class="shop">
          <div class="shop-top"><span class="genre">{s["genre"]}</span><span>{a["name"]}</span></div>
          <div class="shop-body">
            <h3>{s["name"]}</h3>
            <div class="signature"><span class="lbl">名物</span><b>{s["sig"]}</b><span class="yen">{s["yen"]}</span></div>
            <p class="desc">{s["desc"]}</p>
            <ul class="feats">{feats}</ul>
            <div class="shop-meta"><span><b>価格帯</b>{s["price"]}</span><span><b>営業</b>{s["hours"]}</span></div>
          </div>
        </article>''')

    shows = "\n".join(f'            <li><span class="t">{t}</span><div><b>{b}</b><small>{s}</small></div></li>' for t, b, s in c["shows"])
    facilities = "\n".join(f'            <li><b>{b}</b><span>{s}</span></li>' for b, s in c["facilities"])
    tips = "\n".join(f'        <li><div><b>{b}</b><span>{s}</span></div></li>' for b, s in c["tips"])

    switch = []
    for x in AREAS:
        inner = f'<span class="num">{x["id"]}</span><span>{x["name"]}<small>{x["en"].title()}</small></span>'
        if x["id"] == aid:
            switch.append(f'        <li class="s{x["id"]}"><span class="current" aria-current="page">{inner}</span></li>')
        else:
            switch.append(f'        <li class="s{x["id"]}"><a href="{href(x)}">{inner}</a></li>')
    switch = "\n".join(switch)

    foot_areas = "".join(f'<a href="{href(x)}">{x["name"]}</a>' for x in AREAS)
    n_rides, n_shops = len(c["rides"]), len(c["shops"])

    return f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{a["name"]} | Cat Panit Island</title>
<meta name="description" content="Cat Panit Island エリア{aid}「{a["name"]}」のアトラクション・グルメ・ショー・施設のご案内。">
<link rel="canonical" href="{SITE}{href(a)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cat Panit Island">
<meta property="og:locale" content="ja_JP">
<meta property="og:title" content="{a["name"]}｜Cat Panit Island">
<meta property="og:description" content="Cat Panit Island エリア{aid}「{a["name"]}」のアトラクション・グルメ・ショー・施設のご案内。">
<meta property="og:url" content="{SITE}{href(a)}">
<meta property="og:image" content="{SITE}assets/ogp.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="ねこの顔のかたちをした島のイラスト">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=Zen+Maru+Gothic:wght@400;500;700&family=Fredoka:wght@500;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body data-area="{aid}">
<div class="draft-ribbon"><div class="wrap">これはホームページの素案です。料金・営業時間・施設などはすべて仮の内容です。</div></div>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Cat Panit Island トップへ">
      {LOGO}
      <span class="brand-name">Cat Panit Island<small>キャット・パニット・アイランド</small></span>
    </a>
    <a class="mobile-ticket" href="index.html#tickets">チケット</a>
    <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="メニューを開く"><span class="bars" aria-hidden="true"></span><span class="lbl" aria-hidden="true">MENU</span></button>
    <nav class="nav" id="site-nav" aria-label="メインメニュー">
      <ul>
{nav_areas}
        <li><a href="index.html#hours">営業時間</a></li>
        <li><a href="index.html#access">アクセス</a></li>
        <li class="nav-cta"><a href="index.html#tickets">チケット</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="top">
  <section class="area-hero">
    <nav class="crumbs wrap" aria-label="パンくずリスト">
    </nav>
    <div class="wrap">
      <div>
        <p class="area-no"><b>{aid}</b>AREA {aid:02d} — {a["en"]}</p>
        <h1>{a["name"]}</h1>
        <p class="lead">{c["lead"]}</p>
        <dl class="facts">
          <div><dt>アトラクション</dt><dd>{n_rides}<small>件</small></dd></div>
          <div><dt>グルメ</dt><dd>{n_shops}<small>店</small></dd></div>
          <div><dt>メインゲートから</dt><dd>{c["walk"]}<small>分</small></dd></div>
        </dl>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#rides">アトラクションを見る</a>
          <a class="btn btn-ghost" href="#gourmet">グルメを見る</a>
        </div>
      </div>
      <div class="map">
        {map_svg(aid)}
      </div>
    </div>
    <svg class="wave" viewBox="0 0 1200 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 24 C 150 0, 300 48, 450 24 S 750 0, 900 24 S 1100 48, 1200 20 L1200 48 L0 48 Z"/></svg>
  </section>

  <section class="block" id="highlights">
    <div class="wrap">
      <div class="sec-head"><div><p class="en">Highlights</p><h2>このエリアの見どころ</h2></div></div>
      <ol class="highlights">
{highlights}
      </ol>
    </div>
  </section>

  <section class="block alt" id="rides">
    <div class="wrap">
      <div class="sec-head">
        <div><p class="en">Attractions</p><h2>アトラクション</h2></div>
        <p>お子さまの身長を入れると、乗れるアトラクションがひと目でわかります。スリル度は肉球の数で表しています。</p>
      </div>
      <div class="finder">
        <div class="height-input">
          <label for="height">身長</label>
          <input id="height" type="number" inputmode="numeric" min="60" max="200" step="1" placeholder="例 110">
          <span>cm</span>
        </div>
        <p class="finder-note" id="finder-note" aria-live="polite">このエリアには{n_rides}件のアトラクションがあります。</p>
      </div>
      <div class="rides">
{chr(10).join(rides)}
      </div>
    </div>
  </section>

  <section class="block" id="gourmet">
    <div class="wrap">
      <div class="sec-head"><div><p class="en">Gourmet</p><h2>グルメ・レストラン</h2></div></div>
      <div class="gourmet-grid">
{chr(10).join(shops)}
      </div>
    </div>
  </section>

  <section class="block alt" id="shows">
    <div class="wrap">
      <div class="sec-head"><div><p class="en">Shows &amp; Facilities</p><h2>ショー・施設</h2></div></div>
      <div class="two-col">
        <div>
          <h3 class="sub-h">このエリアのショー</h3>
          <ul class="schedule">
{shows}
          </ul>
        </div>
        <div>
          <h3 class="sub-h">施設・サービス</h3>
          <ul class="facilities">
{facilities}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="block" id="tips">
    <div class="wrap">
      <div class="sec-head"><div><p class="en">Tips</p><h2>楽しみ方のコツ</h2></div></div>
      <ul class="tips">
{tips}
      </ul>
    </div>
  </section>

  <section class="block alt" id="other-areas">
    <div class="wrap">
      <div class="sec-head"><div><p class="en">Area Guide</p><h2>ほかのエリアへ</h2></div></div>
      <ul class="area-switch">
{switch}
      </ul>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <a class="brand" href="index.html">
        {LOGO}
        <span class="brand-name">Cat Panit Island<small>キャット・パニット・アイランド</small></span>
      </a>
      <nav class="foot-links" aria-label="フッターメニュー">
        {foot_areas}<a href="index.html#rides">アトラクション一覧</a><a href="index.html#gourmet">グルメ・レストラン</a>
        <a href="index.html#tickets">チケット</a><a href="index.html#hours">営業時間</a><a href="index.html#access">アクセス</a><a href="index.html#faq">よくある質問</a>
      </nav>
    </div>
    <p class="copy">© 2026 Cat Panit Island（素案）</p>
  </div>
</footer>

<script src="assets/area.js"></script>
</body>
</html>
'''


for a in AREAS:
    p = OUT / href(a)
    p.write_text(page(a), encoding="utf-8")
    print("wrote", p)
