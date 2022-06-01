<script setup>
import { RouterView } from 'vue-router';
import Navbar from '@/components/NavbarComponent.vue';
</script>

<template>
  <header>
    <Navbar />
  </header>

  <div id="mainContainer">
    <RouterView />
  </div>
</template>

<style>
body {
  height: 100vh;
  width: 100vw;
}

#mainContainer {
  height: 100%;
}
</style>
