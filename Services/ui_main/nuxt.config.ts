export default defineNuxtConfig({
  ssr: true,

  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-icon',
    'nuxt-swiper',
    'nuxt-simple-robots',
  ],

  runtimeConfig: {
    public: {
      // baseURL: 'https://otruyenapi.com/v1/api',
      baseURL: 'http://4.230.96.180/api/otruyen' ,
    },
  },

  compatibilityDate: '2025-01-05',
});