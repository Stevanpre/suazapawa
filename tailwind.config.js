// tailwind.config.js
module.exports = {
  content: [
    "./web/templates/**/*.html",
    "./web/static/**/*.js",
    "./node_modules/flowbite/**/*.js",
    "./node_modules/flowbite/**/*.ts",
    "./node_modules/@themesberg/flowbite/**/*.js",
    "./node_modules/taos/**/*.js"
  ],
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-in-left': 'slideInLeft 0.6s ease-out',
        'slide-in-right': 'slideInRight 0.6s ease-out',
        'slide-in-bottom': 'slideInBottom 0.7s ease-in',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideInLeft: {
          '0%': { transform: 'translateX(-100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideInRight: {
          '0%': { transform: 'translateX(100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideInBottom: {
          '0%': { transform: 'translateY(100%)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [
    require("flowbite/plugin"),
    require("tailwindcss-animate"),
    require("taos/plugin"),
    require("daisyui"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio")
  ],
  daisyui: {
    themes: [
      {
        suazapawa: {
          primary: "#6366f1",    // Indigo
          secondary: "#38bdf8",  // Sky
          accent: "#f472b6",     // Pink
          neutral: "#3d4451",
          "base-100": "#ffffff",
          info: "#3abff8",
          success: "#36d399",
          warning: "#fbbd23",
          error: "#f87272",
        },
      },
      "light",
      "dark"
    ],
  },
};
