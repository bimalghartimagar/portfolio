<template>
  <nav class="flex justify-center pt-8" :class="`grid-cols-${menus.length}`">
    <TheNavLink class="mx-4" v-for="menu in menus" :key="menu" :text="menu" />
  </nav>
</template>

<script>
import TheNavLink from './TheNavLink.vue'
export default {
  components: { TheNavLink },
  data () {
    return {
      menus: ['Home', 'About me', 'Projects', 'Resume', 'Contact']
    }
  }
}
</script>
