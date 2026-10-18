// Mobile menu
const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');
if (burger && menu) {
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
}

// Project filter (projects.html)
const buttons = document.querySelectorAll('.filters button');
const cards = document.querySelectorAll('[data-cat]');
buttons.forEach(btn => btn.addEventListener('click', () => {
  buttons.forEach(b => b.setAttribute('aria-pressed', b === btn));
  const f = btn.dataset.filter;
  cards.forEach(c => { c.hidden = !(f === 'all' || c.dataset.cat.split(' ').includes(f)); });
}));

// Contact form -> opens the visitor's email app
const form = document.querySelector('#contact-form');
if (form) {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const d = new FormData(form);
    const subject = encodeURIComponent('Hello from ' + d.get('name'));
    const body = encodeURIComponent(d.get('message') + '\n\n' + d.get('name') + ' (' + d.get('email') + ')');
    window.location.href = 'mailto:zahramufida1410@gmail.com?subject=' + subject + '&body=' + body;
  });
}
