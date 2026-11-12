// Use a collapsible navigation panel when the reading area becomes narrow.
document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector(".toudens-menu-button");
  const sidebar = document.getElementById("toudens-sidebar");
  const backdrop = document.querySelector(".toudens-sidebar-backdrop");
  if (!button || !sidebar || !backdrop) return;

  const compact = window.matchMedia("(max-width: 1279px)");
  let open = false;

  function update() {
    const visible = !compact.matches || open;
    button.setAttribute("aria-expanded", String(visible));
    button.setAttribute("aria-label", visible ? "收起导航" : "展开导航");
    button.title = visible ? "收起导航" : "展开导航";
    sidebar.setAttribute("aria-hidden", String(!visible));
    sidebar.inert = !visible;
    backdrop.hidden = !compact.matches || !open;
  }

  function close(restoreFocus = true) {
    open = false;
    if (restoreFocus) button.focus();
    update();
  }

  button.addEventListener("click", (event) => {
    if (!compact.matches) return;
    if (open) close();
    else {
      open = true;
      update();
      // Allow inherited visibility to update before focusing a sidebar link.
      requestAnimationFrame(() => requestAnimationFrame(() => {
        if (open) sidebar.querySelector("a, button")?.focus();
      }));
    }
  });

  document.addEventListener("click", (event) => {
    if (compact.matches && open && !sidebar.contains(event.target) && !button.contains(event.target)) {
      close(backdrop.contains(event.target));
    }
  });

  sidebar.addEventListener("click", (event) => {
    if (compact.matches && open && event.target.closest("a[href]")) close();
  });

  document.addEventListener("keydown", (event) => {
    if (!compact.matches || !open) return;
    if (event.key === "Escape") {
      event.preventDefault();
      close();
    } else if (event.key === "Tab") {
      const items = [button, ...sidebar.querySelectorAll('a[href], button:not([disabled]), input, [tabindex="0"]')]
        .filter((item) => item.getClientRects().length > 0);
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        items[1]?.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  compact.addEventListener("change", () => {
    open = false;
    if (compact.matches && sidebar.contains(document.activeElement)) button.focus();
    update();
    if (!compact.matches && document.activeElement === button) sidebar.querySelector("a")?.focus();
  });
  update();
});
