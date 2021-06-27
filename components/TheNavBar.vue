<template>
  <nav
    class="grid gap-y-1 md:grid-flow-col text-center mx-4"
    :class="showMenu ? 'border-2 border-alabaster' : ''"
  >
    <div
      class="flex flex-row justify-between border-alabaster border-2 p-2"
      :class="showMenu ? 'border-t-0 border-b-0 border-l-0 border-r-0' : ''"
    >
      <div class="text-lg font-semibold">Menu</div>
      <div @click="toggleMenu()">
        <svg
          v-if="!showMenu"
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          />
        </svg>
        <svg
          v-if="showMenu"
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </div>
    </div>
    <!-- <transition name="slide"> -->
      <TheNavLinkList class="grid gap-y-1 mx-1" v-show="showMenu" />
    <!-- </transition> -->
  </nav>
</template>

<script>
import TheNavLinkList from "./TheNavLinkList.vue";
export default {
  components: { TheNavLinkList },
  data() {
    return {
      showMenu: false,
    };
  },

  methods: {
    toggleMenu: function () {
      this.showMenu = !this.showMenu;
    },
  },
};
</script>

<style scoped>

</style>
