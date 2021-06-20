<template>
  <div
    class="home font-lato h-screen grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 justify-items-center items-center bg-green-500"
  >
    <div class="title-wrapper p-4 text-center">
      <img
        class="w-64 h-64 py-2 mx-auto"
        src="~/assets/images/profile-outline.png"
        alt="Profile"
      />
      <div class="py-2 xl:text-5xl lg:text-4xl md:text-4xl sm:text-8xl font-semibold">Hi, I'm Bimal.</div>
      <div class="py-2 xl:text-4xl lg:text-2xl md:text-2xl sm:text-5xl">I design and build web applications.</div>
      <div class="py-2 xl:text-3xl lg:text-2xl md:text-2xl sm:text-5xl">
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
      <img class="stroke-current w-4/5 h-4/5 mx-auto" src="~/assets/images/work-illustration.svg" />
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Lato:400,700&display=swap");
</style>
