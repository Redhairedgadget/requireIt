<template>
  <v-content
    id="background"
  >
    <v-layout
      align-center
      column
      justify-center
      class="h-80"
    >
        <h1 class="font-weight-thin mb-4 home">requireIt</h1>
        <h4 class="subheading">Click <router-link to="/questionnaire">here</router-link> to get your requirements now!</h4>
        <v-overlay z-index="0"></v-overlay>
    </v-layout>
  </v-content>
</template>

<script>

</script>

<style>

    #background{
        background: url('../assets/background.jpg') no-repeat;
        height: 100vh;
        color: white;
        background-size: cover;
    }

    .h-80{
        height: 70vh;
    }

    .home{
        font-size: 60pt;
        z-index: 20;
    }

    h4{
        font-size: 18pt;
        z-index: 20;
    }

</style>