/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/svelte/*.js"],
  theme: {
    extend: {},
  },
  plugins: [],
}

// npx tailwindcss -i ./static/template.tailwind.css -o ./static/main.css --watch