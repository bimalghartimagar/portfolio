<script>
import ContactMeForm from "../components/ContactMeForm.vue";

export default {
  components: { ContactMeForm },
};
</script>
<template>
  <div class="mt-5 flex justify-around flex-col lg:flex-row">
    <div
      class="grid grid-flow-row justify-evenly content-center text-center gap-5 lg:w-2/5"
    >
      <h1 class="text-3xl font-bold">
        Let's chat.<br />Let's create something together.
      </h1>
      <p class="text-xl font-semibold">
        Mail me at
        <a
          href="mailto:contact@bimalghartimagar.com.np"
          class="text-alabaster cursor-pointer hover:underline"
          >contact@bimalghartimagar.com.np</a
        >
      </p>
    </div>
    <contact-me-form class="mt-5 mx-5 lg:w-2/5" />
  </div>
</template>
