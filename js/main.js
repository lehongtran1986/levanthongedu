// Mobile nav toggle
function initPage() {
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

  // Assessment/registration form submission
  var assessmentForm = document.getElementById('assessment-form');
  if (assessmentForm) {
    assessmentForm.addEventListener('submit', function (event) {
      event.preventDefault();

      var endpoint = assessmentForm.getAttribute('data-endpoint');
      var submitBtn = document.getElementById('assessment-submit-btn');
      var errorMsg = document.getElementById('assessment-form-error');
      var successBox = document.getElementById('assessment-success');

      if (errorMsg) errorMsg.classList.add('hidden');

      var formData = new FormData(assessmentForm);
      var payload = {
        studentName: formData.get('studentName') || '',
        grade: formData.get('grade') || '',
        school: formData.get('school') || '',
        parentPhone: formData.get('parentPhone') || '',
        subjects: formData.getAll('subjects'),
        target: formData.get('target') || '',
        contactTime: formData.get('contactTime') || ''
      };

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Đang gửi...';
      }

      fetch(endpoint, {
        method: 'POST',
        mode: 'no-cors',
        body: JSON.stringify(payload)
      })
        .then(function () {
          assessmentForm.classList.add('hidden');
          if (successBox) successBox.classList.remove('hidden');
        })
        .catch(function () {
          if (errorMsg) errorMsg.classList.remove('hidden');
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Đăng ký ngay';
          }
        });
    });
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPage);
} else {
  initPage();
}
