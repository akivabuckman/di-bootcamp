document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');
    const loginForm = document.getElementById('loginForm');
    const registerBtn = document.getElementById('registerBtn');
    const loginBtn = document.getElementById('loginBtn');
  
    registerForm.addEventListener('input', () => {
      const inputs = registerForm.querySelectorAll('input[required]');
      registerBtn.disabled = Array.from(inputs).some(input => !input.value);
    });
  
    loginForm.addEventListener('input', () => {
      const inputs = loginForm.querySelectorAll('input[required]');
      loginBtn.disabled = Array.from(inputs).some(input => !input.value);
    });
  });
  