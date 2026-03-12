document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Handle all buttons with text containing "Comprar" or "Quero"
    const actionButtons = document.querySelectorAll('button');
    actionButtons.forEach(button => {
        const text = button.textContent.toLowerCase();
        if (text.includes('comprar') || text.includes('quero')) {
            button.addEventListener('click', () => {
                window.location.href = 'https://app.coinzz.com.br/checkout/1-unidade-qsndn-0';
            });
        }
    });
});
