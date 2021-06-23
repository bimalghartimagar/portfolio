<template>
  <div class="bg-green-500 h-screen">
    <TheNavBar />
    <Nuxt />
    <TheFooter />
  </div>
</template>

<script>
import TheFooter from '../components/TheFooter.vue'
import TheNavBar from '../components/TheNavBar.vue'

export default {
  components: {
    TheFooter,
    TheNavBar
  }
}
</script>
