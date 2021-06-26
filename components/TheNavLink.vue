<template>
  <NuxtLink class="text-lg font-semibold cursor-pointer" :to="link">{{ text }}</NuxtLink>
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
