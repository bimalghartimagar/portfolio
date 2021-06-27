<template>
  <div class="bg-green-500 min-h-screen lg:grid lg:justify-items-stretch lg:items-baseline pt-4">
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
