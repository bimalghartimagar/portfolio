export default {
  head: {
    htmlAttrs: {
      lang: 'en'
    },
    title: 'Bimal\'s portfolio',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: 'Software Engineer Developer Portfolio'
      }
    ]
  },
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