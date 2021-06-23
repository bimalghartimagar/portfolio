<template>
  <div class="text-lg font-semibold cursor-pointer">{{ text }}</div>
</template>

<script>
export default {
  props:{
    text: {
      type: String,
      required: true
    }
  }
}
</script>
