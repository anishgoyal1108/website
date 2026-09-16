/* Subject filter on the Notes index. Everything is visible without JS. */
(function () {
  var buttons = document.querySelectorAll(".notes-filter button[data-group]");
  var groups = document.querySelectorAll(".notes-group[data-group]");
  if (!buttons.length) return;
  function select(g) {
    buttons.forEach(function (b) { b.classList.toggle("active", b.dataset.group === g); });
    groups.forEach(function (s) { s.hidden = g !== "all" && s.dataset.group !== g; });
    try { if (g === "all") history.replaceState(null, "", location.pathname); else history.replaceState(null, "", "#" + g); } catch (e) {}
  }
  buttons.forEach(function (b) { b.addEventListener("click", function () { select(b.dataset.group); }); });
  var h = location.hash.replace("#", "");
  if (h && document.querySelector('.notes-group[data-group="' + h + '"]')) select(h);
})();
