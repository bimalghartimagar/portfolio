<script>
import ContactMeForm from "../components/ContactMeForm.vue";

export default {
  components: { ContactMeForm },
};
</script>
<template>
  <div class="flex justify-around">
    <div class="border-2  w-2/5 grid grid-flow-row justify-evenly items-center text-center">
      <h1 class="text-4xl">Let's chat.</h1>
      <p class="text-3xl">Let's create something together.</p>
      <p class="text-3xl">Mail me at <a href="mailto:contact@bimalghartimagar.com.np" class="text-blue-800">contact@bimalghartimagar.com.np</a>.</p>
    </div>
    <contact-me-form class="w-2/5" />
  </div>
</template>
