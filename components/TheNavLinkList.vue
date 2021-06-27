<template>
  <div>
    <TheNavLink
      class="rounded-md p-1"
      v-for="menu in menus"
      :key="menu.link"
      :text="menu.name"
      :link="menu.link"
    />
  </div>
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
