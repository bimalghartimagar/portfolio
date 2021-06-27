<template>
  <div class="mt-5">
    <aside class="w-60 text-center justify-self-end hidden">
      <div class="rounded-full py-1.5 px-3 my-2 bg-alabaster">All</div>
      <div class="rounded-full py-1.5 px-3 my-2 bg-alabaster">Backend</div>
      <div class="rounded-full py-1.5 px-3 my-2 bg-alabaster">Frontend</div>
    </aside>
    <h3 class="text-2xl text-center mb-2 font-semibold">Github Repos, latest first.</h3>
    <section class="mx-auto md:grid md:grid-cols-2 lg:grid lg:grid-cols-3">
        <ListItem
          class="p-4 m-4 rounded-md bg-alabaster flex flex-col justify-between ring-4 ring-black"
          v-for="repo in repos"
          :key="repo.url"
          :repo="repo"
        />
    </section>
  </div>
</template>

<script>
import ListItem from "../components/ListItem.vue";
export default {
  components: { ListItem },
  data() {
    return {
      repos: [],
    };
  },
  async fetch() {
    this.repos = await fetch(
      "https://api.github.com/users/bimalghartimagar/repos"
    )
      .then((res) => res.json())
      .then(
        (data) =>
          (this.repos = data
            .filter((item) => item.fork === false)
            .map(({ created_at, url, name, description, tags_url }) => ({
              created_at,
              url,
              name,
              description,
              tags_url,
            }))
            .sort((a,b)=>{
              if (a.created_at>b.created_at) return -1
              else if (a.created_at<b.created_at) return 1
              else return 0
            }))
      );
  },
};
</script>