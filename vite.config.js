import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 3000,
    open: '/prototype.html', // automatically open the prototype
  },
  plugins: [
    {
      name: 'rewrite-prototype',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (req.url === '/prototype' || req.url === '/') {
            req.url = '/prototype.html'
          }
          next()
        })
      }
    }
  ]
})
