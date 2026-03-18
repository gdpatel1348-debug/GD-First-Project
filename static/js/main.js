// Main JS interactions for EcoCredit India Platform

console.log("EcoCredit System Initialized.");

document.addEventListener('DOMContentLoaded', () => {
    // Basic interaction for buttons
    const buttons = document.querySelectorAll('.action-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (e.target.innerText === 'MINT CREDITS') {
                e.target.innerText = 'VERIFYING...';
                setTimeout(() => {
                    e.target.innerText = 'CREDITS MINTED';
                    e.target.style.background = 'var(--emerald-green)';
                    e.target.style.color = '#000';
                }, 2000);
            } else if (e.target.innerText === 'BUY') {
                e.target.innerText = 'PROCESSING...';
                setTimeout(() => {
                    e.target.innerText = 'PURCHASED';
                    e.target.style.background = 'var(--gold)';
                    e.target.style.color = '#000';
                }, 1500);
            }
        });
    });
});
