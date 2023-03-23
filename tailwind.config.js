/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
      './sci_home_2023/templates/**/*.html',
      './templates/pages/**/*.html',
      './sci_home_2023/templates/base/**/*.html',
      
  ],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'midnight': '#020223',
      },
      fontFamily: {
        'poppins': ['Poppins', 'sans-serif']
      },
    },
  },
  plugins: [
  ],
}
