// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {
  var menuBtn = document.getElementById('menu-toggle');
  var mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', function () {
      mobileMenu.classList.toggle('hidden');
    });
  }

  // FAQ accordion
  document.querySelectorAll('[data-accordion-trigger]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var panel = document.getElementById(btn.getAttribute('data-accordion-trigger'));
      var icon = btn.querySelector('[data-accordion-icon]');
      if (!panel) return;
      var isOpen = panel.style.maxHeight && panel.style.maxHeight !== '0px';
      panel.style.maxHeight = isOpen ? '0px' : panel.scrollHeight + 'px';
      if (icon) icon.classList.toggle('rotate-180', !isOpen);
    });
  });
});
