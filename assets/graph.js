/* Quartz-style knowledge graph on top of D3 v7 (loaded from cdnjs).
   Local mode: neighbourhood of the current page (depth 1 or 2). Global: everything. */
(function () {
  "use strict";
  var panel = document.querySelector(".graph-panel");
  if (!panel || typeof d3 === "undefined") return;
  var COLORS = { note: "#cba6f7", post: "#f5c2e7", course: "#89dceb", tag: "#a6e3a1", current: "#F14369", link: "#6c7086", text: "#cdd6f4" };
  var mode = panel.dataset.mode || "local";
  var current = panel.dataset.current || location.pathname;
  var canvas = panel.querySelector(".graph-canvas");
  var depth = 1, showTags = true, data = null, sim = null;

  function load() {
    var src = panel.dataset.src || "/graph.json";
    var key = "graph-json:" + src;
    try {
      sessionStorage.removeItem("graph-json");
      var cached = sessionStorage.getItem(key);
      if (cached) {
        var d = JSON.parse(cached);
        var hasCurrent = d.nodes.some(function (n) { return n.id === current; });
        if (mode === "global" || hasCurrent) return Promise.resolve(d);
      }
    } catch (e) {}
    return fetch(src).then(function (r) { return r.json(); }).then(function (d) {
      try { sessionStorage.setItem(key, JSON.stringify(d)); } catch (e) {}
      return d;
    });
  }

  function subset(d) {
    var byId = {};
    d.nodes.forEach(function (n) { byId[n.id] = n; });
    var adj = {};
    d.links.forEach(function (l) {
      if (!byId[l.source] || !byId[l.target]) return;
      if (!showTags && (byId[l.source].type === "tag" || byId[l.target].type === "tag")) return;
      (adj[l.source] = adj[l.source] || []).push(l.target);
      (adj[l.target] = adj[l.target] || []).push(l.source);
    });
    var keep;
    if (mode === "global") {
      keep = {};
      d.nodes.forEach(function (n) { if (showTags || n.type !== "tag") keep[n.id] = true; });
    } else {
      keep = {}; keep[current] = true;
      var frontier = [current];
      for (var k = 0; k < depth; k++) {
        var next = [];
        frontier.forEach(function (id) {
          (adj[id] || []).forEach(function (m) { if (!keep[m]) { keep[m] = true; next.push(m); } });
        });
        frontier = next;
      }
    }
    var nodes = d.nodes.filter(function (n) { return keep[n.id]; }).map(function (n) { return Object.assign({}, n); });
    var links = d.links.filter(function (l) { return keep[l.source] && keep[l.target]; }).map(function (l) { return { source: l.source, target: l.target }; });
    return { nodes: nodes, links: links, adj: adj };
  }

  function render() {
    var g = subset(data);
    canvas.innerHTML = "";
    var width = canvas.clientWidth || 600, height = mode === "global" ? Math.max(520, window.innerHeight - 260) : 320;
    var svg = d3.select(canvas).append("svg").attr("viewBox", [0, 0, width, height]).attr("width", "100%").attr("height", height);
    var root = svg.append("g");
    var neighbours = {};
    g.links.forEach(function (l) { (neighbours[l.source] = neighbours[l.source] || {})[l.target] = true; (neighbours[l.target] = neighbours[l.target] || {})[l.source] = true; });
    var degree = {};
    g.links.forEach(function (l) { degree[l.source] = (degree[l.source] || 0) + 1; degree[l.target] = (degree[l.target] || 0) + 1; });
    var radius = function (n) { return (n.id === current ? 7 : 4) + Math.min(6, Math.sqrt(degree[n.id] || 0)); };
    var color = function (n) { return n.id === current ? COLORS.current : COLORS[n.type] || COLORS.note; };

    if (sim) sim.stop();
    sim = d3.forceSimulation(g.nodes)
      .force("link", d3.forceLink(g.links).id(function (d) { return d.id; }).distance(mode === "global" ? 40 : 60).strength(0.6))
      .force("charge", d3.forceManyBody().strength(mode === "global" ? -60 : -180))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collide", d3.forceCollide().radius(function (d) { return radius(d) + 4; }))
      .alphaDecay(mode === "global" ? 0.02 : 0.04);

    var link = root.append("g").attr("stroke", COLORS.link).attr("stroke-opacity", 0.6)
      .selectAll("line").data(g.links).join("line").attr("stroke-width", 1);
    var node = root.append("g").selectAll("g").data(g.nodes).join("g").attr("class", "gnode").style("cursor", "pointer");
    node.append("circle").attr("r", radius).attr("fill", color).attr("stroke", "#10101A").attr("stroke-width", 1.2);
    var label = node.append("text").text(function (d) { return d.title; })
      .attr("x", function (d) { return radius(d) + 3; }).attr("y", 4)
      .attr("fill", COLORS.text).attr("font-size", mode === "global" ? 9 : 11).attr("opacity", mode === "global" ? 0 : 0.9)
      .style("pointer-events", "none");

    node.on("mouseenter", function (e, d) {
      node.attr("opacity", function (o) { return o.id === d.id || (neighbours[d.id] && neighbours[d.id][o.id]) ? 1 : 0.15; });
      link.attr("stroke-opacity", function (l) { return l.source.id === d.id || l.target.id === d.id ? 1 : 0.08; })
          .attr("stroke", function (l) { return l.source.id === d.id || l.target.id === d.id ? COLORS.current : COLORS.link; });
      label.attr("opacity", function (o) { return o.id === d.id || (neighbours[d.id] && neighbours[d.id][o.id]) ? 1 : 0; });
    }).on("mouseleave", function () {
      node.attr("opacity", 1); link.attr("stroke-opacity", 0.6).attr("stroke", COLORS.link);
      label.attr("opacity", mode === "global" ? 0 : 0.9);
    }).on("click", function (e, d) { if (d.id !== current) location.href = d.id; });
    node.append("title").text(function (d) { return d.title; });

    node.call(d3.drag()
      .on("start", function (e, d) { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on("drag", function (e, d) { d.fx = e.x; d.fy = e.y; })
      .on("end", function (e, d) { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));
    svg.call(d3.zoom().scaleExtent([0.2, 6]).on("zoom", function (e) {
      root.attr("transform", e.transform);
      if (mode === "global") label.attr("opacity", e.transform.k > 1.6 ? 0.9 : 0);
    }));
    sim.on("tick", function () {
      link.attr("x1", function (d) { return d.source.x; }).attr("y1", function (d) { return d.source.y; })
          .attr("x2", function (d) { return d.target.x; }).attr("y2", function (d) { return d.target.y; });
      node.attr("transform", function (d) { return "translate(" + d.x + "," + d.y + ")"; });
    });
  }

  panel.querySelectorAll("button[data-depth]").forEach(function (b) {
    b.addEventListener("click", function () {
      depth = +b.dataset.depth;
      panel.querySelectorAll("button[data-depth]").forEach(function (x) { x.classList.toggle("active", x === b); });
      render();
    });
  });
  var tagToggle = panel.querySelector("input[data-toggle=tags]");
  if (tagToggle) tagToggle.addEventListener("change", function () { showTags = tagToggle.checked; render(); });
  var ro = typeof ResizeObserver !== "undefined" ? new ResizeObserver(function () { if (data) render(); }) : null;
  load().then(function (d) {
    data = d;
    render();
    if (ro) ro.observe(canvas);
  }).catch(function (err) { canvas.textContent = "graph unavailable"; console.error(err); });
})();
