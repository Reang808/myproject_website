// タイトル文字を横からフェードインさせるスクリプト
// 対象: 業務効率化の新時代, 集客力を高める, About, Service, Contact

document.addEventListener('DOMContentLoaded', function() {
  // 対象タイトルのセレクタリスト
  const selectors = [
    'h1.heading-responsive_xlarge.margin-bottom_none', // 業務効率化の新時代, 集客力を高める
    'h2.heading_h1', // About, Contact
    'h1.heading_h1'  // Service
  ];

  // 対象テキスト
  const targetTexts = [
    '業務効率化の新時代',
    '集客力を高める',
    'About',
    'Service',
    'Contact'
  ];

  // すべての対象要素を取得
  let targets = [];
  selectors.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (targetTexts.includes(el.textContent.trim())) {
        targets.push(el);
      }
    });
  });

  // スタイルを適用
  targets.forEach(el => {
    el.style.opacity = 0;
    el.style.transform = 'translateX(-40px)';
    el.style.transition = 'opacity 1.2s, transform 1.2s';
  });

  // スクロールで表示されたらフェードイン
  const fadeInOnScroll = () => {
    targets.forEach(el => {
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
