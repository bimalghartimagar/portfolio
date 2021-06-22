export default {
  target: 'server',
  build: {
    publicPath: '/app'
  },
  router: {
    base: '/'
  },
  buildModules: ['@nuxtjs/tailwindcss']
}