
// ================================
// MOBILE NAVIGATION
// ================================

const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');

if (burger && menu) {
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');

    burger.setAttribute(
      'aria-expanded',
      open
    );
  });
}


// ================================
// PROJECT FILTER
// ================================

const buttons = document.querySelectorAll(
  '.filters button'
);

const cards = document.querySelectorAll(
  '[data-cat]'
);

buttons.forEach(btn => {
  btn.addEventListener('click', () => {

    buttons.forEach(b => {
      b.setAttribute(
        'aria-pressed',
        b === btn
      );
    });

    const filter = btn.dataset.filter;

    cards.forEach(card => {
      card.hidden = !(
        filter === 'all' ||
        card.dataset.cat.split(' ').includes(filter)
      );
    });

  });
});


// ================================
// CONTACT FORM
// ================================

// The contact form is submitted directly
// to Formspree using its HTML action.
//
// No JavaScript submit handler is needed.
// Do not use preventDefault() or mailto:.
