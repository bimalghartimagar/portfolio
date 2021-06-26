<template>
  <nav class="flex justify-center pt-8" :class="`grid-cols-${menus.length}`">
    <TheNavLink
      class="mx-4 text-4xl"
      v-for="menu in menus"
      :key="menu.link"
      :text="menu.name"
      :link="menu.link"
    />
  </nav>
</template>

<script>
import TheNavLink from "./TheNavLink.vue";
export default {
  components: { TheNavLink },
  data() {
    return {
      menus: [
        { name: "Home", link: "/" },
        { name: "About me", link: "aboutme" },
        { name: "Projects", link: "projects" },
        { name: "Resume", link: "resume" },
        { name: "Contact", link: "contact" },
      ],
    };
  },
};
</script>
