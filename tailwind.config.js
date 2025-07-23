/**
 * Tailwind CSS Configuration
 * @see https://tailwindcss.com/docs/configuration
 */

/** @type {import('tailwindcss').Config} */
module.exports = {
  // Enable dark mode via a utility class on <html> (e.g., <html class="dark">)
  darkMode: 'class',
  // Paths to all of your template and script files
  content: [
    './web/templates/**/*.{html,js,ts}',
    './web/static/**/*.{html,js,ts}',
    'node_modules/flowbite/**/*.{js,ts}',
    'node_modules/@themesberg/flowbite/**/*.{js,ts}',
    'node_modules/taos/**/*.{js,ts}'
  ],
  theme: {
    extend: {
      // Custom keyframes for animations
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideInLeft: {
          '0%': { transform: 'translateX(-100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        slideInRight: {
          '0%': { transform: 'translateX(100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        slideInBottom: {
          '0%': { transform: 'translateY(100%)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' }
        },
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(40px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        },
        typing: {
          '0%': { width: '0' },
          '100%': { width: '100%' }
        },
        blink: {
          '0%, 100%': { borderColor: 'transparent' },
          '50%': { borderColor: 'yellow' }
        }
      },
      // Associate keyframes with animation utilities
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-in-left': 'slideInLeft 0.6s ease-out',
        'slide-in-right': 'slideInRight 0.6s ease-out',
        'slide-in-bottom': 'slideInBottom 0.7s ease-in',
        float: 'float 6s ease-in-out infinite',
        'fade-in-up': 'fadeInUp 1s ease-out both',
        typing: 'typing 2.5s steps(15) 1 normal both',
        blink: 'blink 0.8s step-end infinite'
      }
    }
  },
  // Third-party plugins
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/typography'),
    require('daisyui'),
    require('flowbite/plugin'),
    require('taos/plugin'),
    require('tailwindcss-animate')
  ],
  // DaisyUI configuration and custom theme
  daisyui: {
    themes: [
      {
        suazapawa: {
          primary: '#6366f1',    // Indigo
          secondary: '#38bdf8',  // Sky
          accent: '#f472b6',     // Pink
          neutral: '#3d4451',
          'base-100': '#ffffff',
          info: '#3abff8',
          success: '#36d399',
          warning: '#fbbd23',
          error: '#f87272'
        }
      },
      'light',
      'dark'
    ]
  }
};
