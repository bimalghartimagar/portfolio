<template>
  <div>
    <div>
      <div class="font-semibold text-4xl mb-2">{{ repo.name }}</div>
      <div class="text-xl mb-2 break-words">{{ repo.description }}</div>
    </div>
    <div class="text-xl">
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
