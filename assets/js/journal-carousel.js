(() => {
  const carousel = document.querySelector('[data-carousel]');
  if (!carousel) return;

  const track = carousel.querySelector('.journal-track');
  const slides = [...carousel.querySelectorAll('[data-slide]')];
  const controls = carousel.querySelector('[data-carousel-controls]');
  const dots = [...carousel.querySelectorAll('[data-carousel-go]')];
  const current = carousel.querySelector('[data-carousel-current]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let active = 0;
  let scheduled = false;

  const update = () => {
    scheduled = false;
    const left = track.getBoundingClientRect().left;
    active = slides.reduce((nearest, slide, index) =>
      Math.abs(slide.getBoundingClientRect().left - left) <
      Math.abs(slides[nearest].getBoundingClientRect().left - left) ? index : nearest, 0);
    current.textContent = String(active + 1).padStart(2, '0');
    dots.forEach((dot, index) => {
      if (index === active) dot.setAttribute('aria-current', 'true');
      else dot.removeAttribute('aria-current');
    });
    slides.forEach((slide, index) => {
      slide.querySelector('a').tabIndex = index === active ? 0 : -1;
    });
  };

  const go = (index) => {
    const target = (index + slides.length) % slides.length;
    const left = slides[target].getBoundingClientRect().left - track.getBoundingClientRect().left + track.scrollLeft;
    track.scrollTo({ left, behavior: reducedMotion.matches ? 'instant' : 'smooth' });
  };

  carousel.querySelector('[data-carousel-prev]').addEventListener('click', () => go(active - 1));
  carousel.querySelector('[data-carousel-next]').addEventListener('click', () => go(active + 1));
  dots.forEach((dot, index) => dot.addEventListener('click', () => go(index)));
  track.addEventListener('keydown', (event) => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    const focusedLink = document.activeElement.closest('.journal-story');
    const target = event.key === 'Home' ? 0 : event.key === 'End' ? slides.length - 1 :
      (active + (event.key === 'ArrowRight' ? 1 : -1) + slides.length) % slides.length;
    go(target);
    if (focusedLink) slides[target].querySelector('a').focus({ preventScroll: true });
  });
  track.addEventListener('scroll', () => {
    if (!scheduled) {
      scheduled = true;
      requestAnimationFrame(update);
    }
  }, { passive: true });
  new ResizeObserver(() => {
    track.scrollTo({ left: slides[active].offsetLeft - slides[0].offsetLeft, behavior: 'instant' });
    update();
  }).observe(track);

  // Browsing stays manual: a reader never loses a title to an autoplay timer.
  controls.hidden = slides.length < 2;
  update();
})();
