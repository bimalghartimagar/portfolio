<template>
  <form @submit.prevent="onSubmit">
    <div class="grid grid-cols-1 gap-6">
      <label class="block">
        <span class="text-gray-700">Full name</span>
        <input
          type="text"
          name="name"
          v-model="name"
          class="
            mt-1
            block
            w-full
            rounded-md
            border-gray-300
            shadow-sm
            focus:border-indigo-300
            focus:ring focus:ring-indigo-200 focus:ring-opacity-50
          "
          placeholder=""
        />
      </label>
      <label class="block">
        <span class="text-gray-700">Email address</span>
        <input
          type="email"
          name="email"
          v-model="email"
          class="
            mt-1
            block
            w-full
            rounded-md
            border-gray-300
            shadow-sm
            focus:border-indigo-300
            focus:ring focus:ring-indigo-200 focus:ring-opacity-50
          "
          placeholder="john@example.com"
        />
      </label>
      <label class="block">
        <span class="text-gray-700">Message</span>
        <textarea
          name="details"
          v-model="details"
          class="
            mt-1
            block
            w-full
            rounded-md
            border-gray-300
            shadow-sm
            focus:border-indigo-300
            focus:ring focus:ring-indigo-200 focus:ring-opacity-50
          "
          rows="3"
        ></textarea>
      </label>
      <label class="block">
        <vue-hcaptcha
          ref="hCaptchaElem"
          sitekey="2344238e-dd39-43be-bff7-c54b69e084b8"
          @verify="onVerify"
          @expire="onExpire"
          @error="onError"
        ></vue-hcaptcha>
      </label>
      <label class="block">
        <button
          class="bg-alabaster py-2 px-4 rounded-md font-semibold"
          :class="canSubmit ? '' : 'cursor-not-allowed opacity-40'"
          :disabled="!canSubmit"
        >
          Submit
        </button>
      </label>
      <label class="block">
        <span class="font-bold text-lg" :class="msgClasses">{{ this.msg }}</span>
      </label>
    </div>
  </form>
</template>

<script>
import VueHcaptcha from "@hcaptcha/vue-hcaptcha";
export default {
  components: { VueHcaptcha },

  data() {
    return {
      name: "",
      email: "",
      details: "",
      verified: false,
      token: null,
      ekey: null,
      expired: false,
      error: null,
      msgClasses: "",
      msg: "",
    };
  },

  computed: {
    canSubmit() {
      return (
        this.name.trim().length > 0 &&
        this.email.trim().length > 0 &&
        this.details.trim().length > 0 &&
        this.verified
      );
    },
  },

  methods: {
    onVerify(token, ekey) {
      this.verified = true;
      this.token = token;
      this.ekey = ekey;
      console.log(`Callback token: ${token}, ekey: ${ekey}`);
    },

    onExpire() {
      this.verified = false;
      this.token = null;
      this.ekey = null;
      this.expired = true;
    },

    onError(err) {
      this.verified = false;
      this.token = null;
      this.ekey = null;
      this.error = err;
      console.log(err);
    },

    onSubmit(e) {
      e.preventDefault();
      fetch(`/api/contact`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: this.name,
          email: this.email,
          details: this.details,
          token: this.token,
          ekey: this.ekey,
        }),
      })
        .then((response) => response.json())
        .then((jsonResponse) => {
          // Clears the form
          this.name = "";
          this.email = "";
          this.details = "";
          this.$refs.hCaptchaElem.reset();

          if (jsonResponse.success) {
            this.msgClasses = "text-alabaster";
          } else {
            this.msgClasses = "text-red-700";
          }

          this.msg = jsonResponse.msg;
        })
        .catch((err) => {
          this.error = err;
        });
    },
  },
};
</script>
