export default {
  ssr: true,
  target: 'static',
  build: {
    publicPath: '/app'
  },
  router: {
    base: '/'
  },
  buildModules: ['@nuxtjs/tailwindcss']
}