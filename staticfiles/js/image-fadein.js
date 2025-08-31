// imagesのimg要素をフェードインさせるスクリプト
// ページ内のimgタグすべてに適用します

document.addEventListener('DOMContentLoaded', function() {
  const images = document.querySelectorAll('img');
  images.forEach(img => {
    img.style.opacity = 0;
    img.style.transition = 'opacity 1.2s';
  });

  const fadeInOnScroll = () => {
    images.forEach(img => {
      const rect = img.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        img.style.opacity = 1;
      }
    });
  };

  window.addEventListener('scroll', fadeInOnScroll);
  window.addEventListener('resize', fadeInOnScroll);
  fadeInOnScroll(); // 初回実行
});
