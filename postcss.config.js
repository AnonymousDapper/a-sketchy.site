module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
    doiuse: {},
    ...(process.env.NODE_ENV === 'production' ? { cssnano: {} } : {})
  }
}