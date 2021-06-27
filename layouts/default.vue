<template>
  <div class="bg-green-500 min-h-screen pt-2">
    <TheNavBar />
    <main>
      <Nuxt />
    </main>
    <footer>
      <TheFooter />
    </footer>
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
