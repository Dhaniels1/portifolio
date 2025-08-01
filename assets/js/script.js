document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            // Previne o envio real do formulário
            event.preventDefault();

            // Pega os campos do formulário
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();

            // Validação simples: verifica se os campos não estão vazios 
            if (name === '' || email === '' || subject === '' || message === '') {
                alert('Por favor, preencha todos os campos do formulário.');
                return; // Interrompe a execução se a validação falhar
            }

            // Exibe a mensagem de sucesso [cite: 10]
            const successMessage = document.getElementById('success-message');
            successMessage.classList.remove('hidden');

            // Limpa o formulário após o "envio"
            contactForm.reset();

            // Opcional: esconde a mensagem de sucesso após alguns segundos
            setTimeout(() => {
                successMessage.classList.add('hidden');
            }, 5000); // 5 segundos
        });
    }
});