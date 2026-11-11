/* USN Lab Wiki: "On this page" outline, search, mobile menu. No libraries. */
(function () {
  "use strict";

  /* ---------- On this page ---------- */
  var toc = document.querySelector(".toc");
  var content = document.querySelector(".content");
  if (toc && content) {
    var heads = content.querySelectorAll("h2[id], h3[id]");
    if (heads.length >= 3) {
      var list = toc.querySelector("ol");
      var links = [];
      heads.forEach(function (h) {
        var li = document.createElement("li");
        if (h.tagName === "H3") li.className = "sub";
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        list.appendChild(li);
        links.push(a);
      });
      toc.hidden = false;
      document.body.classList.add("has-toc");

      var setActive = function () {
        var y = window.scrollY + 120, current = 0;
        heads.forEach(function (h, i) { if (h.offsetTop <= y) current = i; });
        links.forEach(function (a, i) { a.classList.toggle("is-active", i === current); });
      };
      window.addEventListener("scroll", setActive, { passive: true });
      setActive();
    }
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.querySelector(".menu-btn");
  var scrim = document.querySelector(".scrim");
  var setMenu = function (open) {
    document.body.classList.toggle("nav-open", open);
    if (menuBtn) menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (scrim) scrim.hidden = !open;
  };
  if (menuBtn) menuBtn.addEventListener("click", function () { setMenu(!document.body.classList.contains("nav-open")); });
  if (scrim) scrim.addEventListener("click", function () { setMenu(false); });

  /* ---------- Search ---------- */
  var box = document.querySelector(".search");
  if (!box) return;
  var input = box.querySelector("input");
  var out = box.querySelector(".search-results");
  var index = null, loading = null, selected = -1;

  var fold = function (s) {
    return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/ø/g, "o").replace(/æ/g, "ae");
  };
  var esc = function (s) {
    return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  };
  var load = function () {
    if (!loading) {
      loading = fetch(box.getAttribute("data-index"))
        .then(function (r) { return r.json(); })
        .then(function (data) {
          index = data.map(function (p) { p.t = fold(p.title); p.x = fold(p.text); return p; });
        })
        .catch(function () { index = []; });
    }
    return loading;
  };

  var snippet = function (p, terms) {
    var i = p.x.indexOf(terms[0]);
    if (i < 0) return esc(p.text.slice(0, 140)) + "…";
    var start = Math.max(0, i - 60);
    var s = p.text.slice(start, start + 160);
    var html = esc(s);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
      html = html.replace(re, "<mark>$1</mark>");
    });
    return (start > 0 ? "…" : "") + html + "…";
  };

  var render = function () {
    var q = fold(input.value.trim());
    selected = -1;
    if (!q || !index) { out.hidden = true; out.innerHTML = ""; return; }
    var terms = q.split(/\s+/).filter(Boolean);
    var hits = index.map(function (p) {
      var score = 0;
      for (var k = 0; k < terms.length; k++) {
        var t = terms[k], inT = p.t.indexOf(t) >= 0, n = p.x.split(t).length - 1;
        if (!inT && !n) return null;
        score += (inT ? 20 : 0) + Math.min(n, 10);
      }
      return { p: p, score: score };
    }).filter(Boolean).sort(function (a, b) { return b.score - a.score; }).slice(0, 8);

    if (!hits.length) {
      out.innerHTML = '<p class="search-empty">No results for “' + esc(input.value) + '”</p>';
    } else {
      out.innerHTML = hits.map(function (h) {
        var tag = h.p.lang === "nb" ? '<span class="lang">NO</span>' : "";
        var url = h.p.url + (h.p.url.indexOf("#") < 0 ? "#:~:text=" + encodeURIComponent(input.value.trim().split(/\s+/)[0]) : "");
        return '<a class="search-hit" href="' + esc(url) + '"><b>' + esc(h.p.title) + "</b>" + tag +
          "<span>" + snippet(h.p, terms) + "</span></a>";
      }).join("");
    }
    out.hidden = false;
  };

  input.addEventListener("focus", load);
  input.addEventListener("input", function () { load().then(render); });
  input.addEventListener("keydown", function (e) {
    var hits = out.querySelectorAll(".search-hit");
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      if (!hits.length) return;
      e.preventDefault();
      selected = (selected + (e.key === "ArrowDown" ? 1 : -1) + hits.length) % hits.length;
      hits.forEach(function (h, i) { h.classList.toggle("is-selected", i === selected); });
      hits[selected].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter") {
      var target = hits[selected >= 0 ? selected : 0];
      if (target) { e.preventDefault(); window.location.href = target.href; }
    } else if (e.key === "Escape") {
      input.value = ""; render(); input.blur();
    }
  });
  document.addEventListener("click", function (e) { if (!box.contains(e.target)) out.hidden = true; });

  var focusSearch = function () { setMenu(false); input.focus(); input.select(); };
  document.addEventListener("keydown", function (e) {
    var tag = (e.target.tagName || "").toLowerCase();
    if (e.key === "/" && tag !== "input" && tag !== "textarea") { e.preventDefault(); focusSearch(); }
  });
  document.querySelectorAll("[data-focus-search]").forEach(function (b) { b.addEventListener("click", focusSearch); });
})();
