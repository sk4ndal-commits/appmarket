document.addEventListener('click', function (e) {
  var btn = document.getElementById('user-menu-button');
  var menu = document.getElementById('user-menu');
  if (!btn || !menu) return;

  // Click on the button toggles the menu
  if (btn.contains(e.target)) {
    var expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', (!expanded).toString());
    menu.classList.toggle('hidden');
    return;
  }

  // Click outside closes the menu
  if (!menu.contains(e.target)) {
    btn.setAttribute('aria-expanded', 'false');
    if (!menu.classList.contains('hidden')) {
      menu.classList.add('hidden');
    }
  }
});
