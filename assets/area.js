// Cat Panit Island — エリアページ共通スクリプト
(function () {
  // モバイルメニュー
  const header = document.querySelector(".site-header");
  const menuBtn = document.getElementById("menu-btn");
  if (header && menuBtn) {
    const setMenu = open => {
      header.classList.toggle("open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.setAttribute("aria-label", open ? "メニューを閉じる" : "メニューを開く");
      menuBtn.querySelector(".lbl").textContent = open ? "CLOSE" : "MENU";
    };
    menuBtn.addEventListener("click", () => setMenu(!header.classList.contains("open")));
    document.getElementById("site-nav").addEventListener("click", e => { if (e.target.closest("a")) setMenu(false); });
    document.addEventListener("keydown", e => { if (e.key === "Escape" && header.classList.contains("open")) { setMenu(false); menuBtn.focus(); } });
    matchMedia("(min-width: 1001px)").addEventListener("change", e => { if (e.matches) setMenu(false); });
  }

  // 身長チェック：.ride[data-min] の身長制限と入力値を比べる
  const heightEl = document.getElementById("height");
  const note = document.getElementById("finder-note");
  const rides = Array.from(document.querySelectorAll(".ride[data-min]"));
  if (!heightEl || !rides.length) return;
  const defaultNote = note ? note.textContent : "";
  function check() {
    const h = parseInt(heightEl.value, 10);
    const hasH = Number.isFinite(h) && h > 0;
    let ok = 0;
    rides.forEach(card => {
      const min = +card.dataset.min;
      const can = !hasH || h >= min;
      if (hasH && can) ok++;
      card.classList.toggle("no", !can);
      const v = card.querySelector(".verdict");
      if (!v) return;
      v.className = "verdict" + (hasH ? (can ? " ok" : " ng") : "");
      v.textContent = hasH ? (can ? "乗れます" : `あと${min - h}cmで乗れます`) : "";
    });
    if (note) note.textContent = hasH ? `身長${h}cmのお子さまは、このエリアの${rides.length}件のうち${ok}件に乗れます。` : defaultNote;
  }
  heightEl.addEventListener("input", check);
  check();
})();
