document.addEventListener('DOMContentLoaded', () => {
    // スクロール時のアニメーション
    const fadeInSections = document.querySelectorAll('.fade-in-section');
    const introSection = document.querySelector('.section-intro');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1 // 10%が見えたら発火
    };

    const fadeInObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // 一度表示されたら監視を停止
            }
        });
    }, observerOptions);

    fadeInSections.forEach(section => {
        fadeInObserver.observe(section);
    });

    // ヘッダーのスクロール時のスタイル変更
    const header = document.querySelector('.header-container');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) { // 50pxスクロールしたら
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // モバイルメニューのトグル機能
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNavigation = document.getElementById('mainNavigation');

    menuToggle.addEventListener('click', () => {
        mainNavigation.classList.toggle('is-open');
    });

    // メニューリンククリックでメニューを閉じる
    mainNavigation.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mainNavigation.classList.remove('is-open');
        });
    });

    // スムーズスクロール
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});