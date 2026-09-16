/* Click-to-zoom viewer for note and post images. No dependencies.
   Without JS the wrapping <a class="zoom"> opens the file in a new tab. */
(function () {
  "use strict";
  var links = Array.prototype.slice.call(document.querySelectorAll(".zoomable a.zoom"));
  if (!links.length) return;
  var box = document.createElement("div");
  box.className = "lightbox";
  box.hidden = true;
  box.innerHTML = '<figure><img alt=""><figcaption></figcaption></figure>' +
    '<button type="button" class="lb-close" aria-label="Close">×</button>' +
    '<button type="button" class="lb-prev" aria-label="Previous image">‹</button>' +
    '<button type="button" class="lb-next" aria-label="Next image">›</button>' +
    '<div class="lb-hint">scroll to zoom · drag to pan · double-click for 1:1 · esc to close</div>';
  document.body.appendChild(box);
  var img = box.querySelector("img"), cap = box.querySelector("figcaption");
  var idx = -1, scale = 1, tx = 0, ty = 0, fit = 1, dragging = false, moved = false, sx = 0, sy = 0, pinch = null;

  function apply() { img.style.transform = "translate(" + tx + "px," + ty + "px) scale(" + scale + ")"; }
  function fitScale() {
    var w = img.naturalWidth || 1, h = img.naturalHeight || 1;
    return Math.min((box.clientWidth - 40) / w, (box.clientHeight - 80) / h, 1);
  }
  function reset() { fit = fitScale(); scale = fit; tx = 0; ty = 0; apply(); }
  function show(i) {
    idx = (i + links.length) % links.length;
    var a = links[idx], src = a.getAttribute("href"), inner = a.querySelector("img");
    img.style.transform = "";
    img.src = src;
    var alt = inner ? inner.getAttribute("alt") || "" : "";
    cap.textContent = /invert_[BW]/.test(alt) ? "" : alt;
    img.classList.toggle("invert", /invert_B$/.test(alt));
    cap.hidden = !cap.textContent;
    box.hidden = false;
    document.body.classList.add("lightbox-open");
    if (img.complete) reset(); else img.onload = reset;
  }
  function close() { box.hidden = true; document.body.classList.remove("lightbox-open"); img.src = ""; }
  function zoomAt(factor, cx, cy) {
    var r = box.getBoundingClientRect();
    var px = cx - r.left - r.width / 2, py = cy - r.top - r.height / 2;
    var ns = Math.max(fit * 0.5, Math.min(scale * factor, 12));
    var k = ns / scale;
    tx = px - (px - tx) * k; ty = py - (py - ty) * k; scale = ns; apply();
  }

  links.forEach(function (a, i) {
    a.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault(); show(i);
    });
  });
  box.querySelector(".lb-close").addEventListener("click", close);
  box.querySelector(".lb-prev").addEventListener("click", function (e) { e.stopPropagation(); show(idx - 1); });
  box.querySelector(".lb-next").addEventListener("click", function (e) { e.stopPropagation(); show(idx + 1); });
  box.addEventListener("click", function (e) { if (e.target === box || e.target.tagName === "FIGURE") close(); });
  box.addEventListener("wheel", function (e) {
    e.preventDefault();
    zoomAt(e.deltaY < 0 ? 1.15 : 1 / 1.15, e.clientX, e.clientY);
  }, { passive: false });
  img.addEventListener("dblclick", function (e) {
    e.preventDefault();
    if (Math.abs(scale - 1) < 0.01 && fit < 1) reset(); else zoomAt(1 / scale, e.clientX, e.clientY);
  });
  img.addEventListener("pointerdown", function (e) {
    if (e.button !== 0) return;
    dragging = true; moved = false; sx = e.clientX - tx; sy = e.clientY - ty;
    img.setPointerCapture(e.pointerId); e.preventDefault();
  });
  img.addEventListener("pointermove", function (e) {
    if (!dragging) return;
    tx = e.clientX - sx; ty = e.clientY - sy; moved = true; apply();
  });
  img.addEventListener("pointerup", function () { dragging = false; });
  img.addEventListener("click", function (e) { e.stopPropagation(); });
  box.addEventListener("touchstart", function (e) {
    if (e.touches.length === 2) {
      pinch = { d: Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY), s: scale };
    }
  }, { passive: true });
  box.addEventListener("touchmove", function (e) {
    if (pinch && e.touches.length === 2) {
      e.preventDefault();
      var d = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
      var cx = (e.touches[0].clientX + e.touches[1].clientX) / 2, cy = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      zoomAt((pinch.s * d / pinch.d) / scale, cx, cy);
    }
  }, { passive: false });
  box.addEventListener("touchend", function () { pinch = null; }, { passive: true });
  document.addEventListener("keydown", function (e) {
    if (box.hidden) return;
    if (e.key === "Escape") close();
    else if (e.key === "ArrowRight") show(idx + 1);
    else if (e.key === "ArrowLeft") show(idx - 1);
    else if (e.key === "+" || e.key === "=") zoomAt(1.2, box.clientWidth / 2, box.clientHeight / 2);
    else if (e.key === "-") zoomAt(1 / 1.2, box.clientWidth / 2, box.clientHeight / 2);
    else if (e.key === "0") reset();
  });
  window.addEventListener("resize", function () { if (!box.hidden) reset(); });
})();
