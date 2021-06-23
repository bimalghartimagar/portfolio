<template>
  <div
    class="home max-h-full grid grid-cols-1 md:grid-cols-2 justify-items-center items-center font-lato h-screen "
  >
    <div class="title-wrapper p-4 text-center">
      <img
        class="w-96 h-96 py-2 mx-auto"
        src="~/assets/images/profile-outline.png"
        alt="Profile"
      />
      <div class="py-2 text-7xl font-semibold">Hi, I'm Bimal.</div>
      <div class="py-2 text-4xl">I design and build web applications.</div>
      <div class="py-2 text-4xl">
        I work as a software engineer at
        <a
          class="cursor-pointer text-alabaster"
          href="https://www.endpoint.com"
          target="_blank"
          referrerpolicy="no-referrer"
          >Endpoint<svg
            class="h-6 w-6 stroke-current stroke-1 inline-block"
            fill="none"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
            /></svg
        ></a>
      </div>
    </div>
    <div>
      <img class="stroke-current w-3/5 h-3/5 mx-auto" src="~/assets/images/work-illustration.svg" />
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Lato:400,700&display=swap");
</style>
