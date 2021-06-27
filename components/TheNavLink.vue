<template>
  <NuxtLink class=" font-semibold cursor-pointer" :to="link">{{ text }}</NuxtLink>
</template>

<script>
export default {
  props:{
    text: {
      type: String,
      required: true
    },
    link: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.nuxt-link-exact-active{
  background-color: #F1F2EB;
}
</style>

