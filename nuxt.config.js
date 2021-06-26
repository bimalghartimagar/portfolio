export default {
  ssr: true,
  target: 'static',
  build: {
    publicPath: '/app'
  },
  router: {
    base: '/portfolio'
  },
  buildModules: ['@nuxtjs/tailwindcss']
}