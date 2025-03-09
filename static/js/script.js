document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    
    form.addEventListener("submit", (e) => {
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm_password").value;

        // Requisitos de validação
        const isValidLength = password.length >= 6;
        const hasUppercase = /[A-Z]/.test(password);
        const hasNumber = /\d/.test(password);
        const hasSpecialChar = /[!@#$%^&*]/.test(password);

        // Verifica se as senhas coincidem
        if (password !== confirmPassword) {
            e.preventDefault();
            alert("As senhas não coincidem!");
            return;
        }

        // Verifica os requisitos de validação da senha
        if (!isValidLength || !hasUppercase || !hasNumber || !hasSpecialChar) {
            e.preventDefault();
            let errorMessage = "A senha deve atender aos seguintes requisitos:\n";
            if (!isValidLength) errorMessage += "- No mínimo 6 dígitos\n";
            if (!hasUppercase) errorMessage += "- Pelo menos 1 letra maiúscula\n";
            if (!hasNumber) errorMessage += "- Pelo menos 1 número\n";
            if (!hasSpecialChar) errorMessage += "- Pelo menos 1 caractere especial (!@#$%^&*)\n";
            alert(errorMessage);
            return;
        }

    });
});