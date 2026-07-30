(function () {
  var burger = document.getElementById('burger');
  var mobileMenu = document.getElementById('mobileMenu');
  if (!burger || !mobileMenu) return;

  burger.addEventListener('click', function () {
    mobileMenu.classList.toggle('open');
    burger.classList.toggle('open');
  });

  // Закрываем меню при клике на ссылку — иначе остаётся висеть поверх контента
  mobileMenu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      mobileMenu.classList.remove('open');
      burger.classList.remove('open');
    });
  });
})();