// Theme toggle
const btn = document.getElementById('theme-toggle');
btn?.addEventListener('click', () => {
  document.body.classList.toggle('light');
  const theme = document.body.classList.contains('light') ? 'light' : 'dark';
  localStorage.setItem('site-theme', theme);
});

// Persist theme
document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('site-theme');
  if (saved === 'light') document.body.classList.add('light');
});

// mailto fallback for contact form
function mailtoFallback(e){
  e.preventDefault();
  const form = document.getElementById('contactForm');
  const name = form.elements['name'].value;
  const email = form.elements['email'].value;
  const message = form.elements['message'].value;
  const subject = encodeURIComponent('Portfolio contact from ' + name);
  const body = encodeURIComponent(`Name: ${name}%0AEmail: ${email}%0A%0A${message}`);
  window.location.href = `mailto:muni.mnpl@gmail.com?subject=${subject}&body=${body}`;
}
