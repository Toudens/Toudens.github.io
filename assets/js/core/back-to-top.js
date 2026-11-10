// The reading panel scrolls independently of the fixed page frame.
document.addEventListener("DOMContentLoaded", () => {
  const panel = document.querySelector(".toudens-page > .hextra-max-page-width > article");
  const button = document.getElementById("backToTop");
  if (!button) return;

  function updateButton() {
    const visible = (panel ? panel.scrollTop : window.scrollY) > 300;
    button.classList.toggle("hx:opacity-0", !visible);
    if (visible) button.removeAttribute("tabindex");
    else button.setAttribute("tabindex", "-1");
  }

  button.addEventListener("click", scrollUp);
  (panel || document).addEventListener("scroll", updateButton, { passive: true });
  updateButton();
});

function scrollUp() {
  const panel = document.querySelector(".toudens-page > .hextra-max-page-width > article");
  (panel || window).scrollTo({
    top: 0,
    left: 0,
    behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
  });
}
