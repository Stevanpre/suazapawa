/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./web/templates/**/*.html",
    "./web/static/js/**/*.js",
    "./node_modules/flowbite/**/*.js",
    "./node_modules/flowbite/**/*.ts"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/typography'),
    require('flowbite/plugin'),
    require('taos/plugin'),
    require('daisyui'),
    require('tailwindcss-animate'),
  ],
  daisyui: {
    // 💡 Aquí defines el tema por defecto
    themes: [
      {
        mytheme: {
          ...require("daisyui/src/theming/themes")["[data-theme=light]"]
        }
      }
    ],
    darkTheme: "false", // ❌ evitar que se use "dark" automáticamente
    base: true,
    styled: true,
    utils: true,
    logs: false,
    rtl: false,
    prefix: "",
  }
}
