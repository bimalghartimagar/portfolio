<template>
  <div>
    <div>
      <div class="font-semibold text-5xl mb-4">{{ repo.name }}</div>
      <div class="text-3xl mb-4">{{ repo.description }}</div>
    </div>
    <div class="text-2xl">
      {{ getDate(repo.created_at) }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    repo: {
      type: Object,
      required: false,
    },
  },

  methods:{
    getDate(date){
      return date.split('T')[0]
    }
  }
};
</script>
