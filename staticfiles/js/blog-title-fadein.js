// blog-post.html用 タイトル横からフェードイン
// 対象: About, 予約管理で業務を効率化

document.addEventListener('DOMContentLoaded', function() {
  // タイトル用
  const titleSelectors = [
    'h2.heading_h1', // About
    'h2.heading_h2'  // 予約管理で業務を効率化
  ];
  const titleTexts = [
    'About',
    '予約管理で業務を効率化'
  ];
  let titleTargets = [];
  titleSelectors.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (titleTexts.includes(el.textContent.trim())) {
        titleTargets.push(el);
      }
    });
  });

  // 画像用
  const imageTargets = Array.from(document.querySelectorAll('img'));

  // 共通スタイル適用
  [...titleTargets, ...imageTargets].forEach(el => {
    el.style.opacity = 0;
    el.style.transform = 'translateX(-40px)';
    el.style.transition = 'opacity 1.2s, transform 1.2s';
  });

  // スクロールで表示されたらフェードイン
  const fadeInOnScroll = () => {
    [...titleTargets, ...imageTargets].forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        el.style.opacity = 1;
        el.style.transform = 'translateX(0)';
      }
    });
  };

  window.addEventListener('scroll', fadeInOnScroll);
  window.addEventListener('resize', fadeInOnScroll);
  fadeInOnScroll(); // 初回実行
});
