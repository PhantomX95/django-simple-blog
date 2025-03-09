function readCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = readCookie('data-bs-theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set theme based on cookie or system preference
    const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-bs-theme', initialTheme);
    
    // Update the switch button's state
    const themeSwitch = document.getElementById('themeSwitch');
    if (themeSwitch) {
        themeSwitch.checked = initialTheme === 'dark';
        
        // Add event listener for checkbox change
        themeSwitch.addEventListener('change', switchTheme);
    }
});

// Theme switcher function
function switchTheme() {
    const themeSwitch = document.getElementById('themeSwitch');
    const newTheme = themeSwitch.checked ? 'dark' : 'light';
    
    // Update the theme and save to cookie
    document.documentElement.setAttribute('data-bs-theme', newTheme);
    document.cookie = `data-bs-theme=${newTheme}; path=/; max-age=31536000`; // Expires in 1 year
}

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    const savedTheme = readCookie('data-bs-theme');
    
    // Only override if no cookie is set (user hasn't manually toggled)
    if (!savedTheme) {
        const newTheme = e.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-bs-theme', newTheme);
        
        // Update the switch button's state
        const themeSwitch = document.getElementById('themeSwitch');
        if (themeSwitch) {
            themeSwitch.checked = newTheme === 'dark';
        }
    }
});

// Bootstrap form validation
(() => {
  'use strict'
  const forms = document.querySelectorAll('.needs-validation')
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }
      form.classList.add('was-validated')
    }, false)
  })
})()

// CKEditor DarkMode
class DarkMode {
  static init() {
    this.editorInstances = new Set();
    this.isDark = localStorage.getItem('darkMode') === 'true';
    this.applyTheme();
  }

  static toggle() {
    this.isDark = !this.isDark;
    localStorage.setItem('darkMode', this.isDark);
    this.applyTheme();
    this.reinitializeEditors();
  }

  static applyTheme() {
    document.documentElement.style.setProperty('--ck-color-base-background', this.isDark ? '#1a1a1a' : '#ffffff');
    document.documentElement.style.setProperty('--ck-color-text', this.isDark ? '#ffffff' : '#000000');
    document.body.classList.toggle('dark-mode', this.isDark);
  }

  static reinitializeEditors() {
    this.editorInstances.forEach(editor => {
      editor.destroy().then(() => {
        ClassicEditor.create(editor.element, {
          ...editor.config,
          theme: this.isDark ? 'dark' : 'lark'
        }).then(newEditor => {
          this.editorInstances.add(newEditor);
        });
      });
    });
  }
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => DarkMode.init());