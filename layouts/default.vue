<template>
  <div class="bg-green-500">
    <TheNavBar />
    <Nuxt />
  </div>
</template>

<script>
import TheNavBar from '../components/TheNavBar.vue'

export default {
  components: {
    TheNavBar
  }
}
</script>