<template id="app">
  <v-app>
      <v-app-bar app>
        <v-toolbar-title class="headline">
          <a href="/" class="head">
            <span>require</span>
            <span class="font-weight-light">It</span>
          </a>
        </v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>

      <v-content>
        <transition
          name="fade"
          mode="out-in"
        >
          <router-view/>
        </transition>
      </v-content>

  </v-app>
</template>

<script>

  // Simulate v-cloak removal
  window.onload = function () {
      document.getElementById('app').classList.toggle('fade-in');
  }

  export default {
      data: () => ({
      loading: true,
    }),
  }
</script>

<style>
  .head{
    color: black !important;
    text-decoration: none;

  }

  .fade-enter-active,
  .fade-leave-active {
    transition-duration: 0.3s;
    transition-property: opacity;
    transition-timing-function: ease;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0
  }

  #app{
    opacity: 0;
    transition: opacity 0.3s linear;
  }

  #app.fade-in{
    opacity: 1;
  }
</style>
