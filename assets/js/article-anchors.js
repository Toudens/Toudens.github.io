// Restore fragment targets inside the independently scrolling reading panel.
window.addEventListener("hashchange", () => {
  requestAnimationFrame(() => {
    const panel = document.querySelector(".toudens-page > .hextra-max-page-width > article");
    const target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
    if (panel && target && panel.contains(target)) {
      target.scrollIntoView({ block: "start", behavior: "instant" });
    }
  });
});
