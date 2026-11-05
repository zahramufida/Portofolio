
// Mobile menu
const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');

if (burger && menu) {
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
}

// Project filter
const buttons = document.querySelectorAll('.filters button');
const cards = document.querySelectorAll('[data-cat]');

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    buttons.forEach(b => {
      b.setAttribute('aria-pressed', b === btn);
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

// Contact form is handled by FormSubmit.
// Do not prevent the default form submission.
