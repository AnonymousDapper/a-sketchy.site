/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./frontend/src/*.svelte"],
  darkMode: 'class',
  theme: {
    fontFamily: {
      sans: ['Philosopher', 'sans-serif'],
      serif: ['Zilla Slab', 'serif']
    },
    container: {
      center: true
    }
  },
  plugins: [],
}

// npx tailwindcss -i static/template.tailwind.css -o static/main.css --watch