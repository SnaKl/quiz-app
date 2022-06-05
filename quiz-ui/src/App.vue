<script setup>
import { RouterView } from 'vue-router';
import Navbar from '@/components/NavbarComponent.vue';
import Toast from '@/components/ToastComponent.vue';
</script>

<template>
  <header>
    <Navbar />
  </header>

  <div id="mainContainer" class="container my-auto">
    <RouterView />
  </div>

  <div id="toast">
    <Toast />
  </div>
</template>

<style>
body {
  height: 100vh;
  width: 100vw;
}

/* #mainContainer {
  height: 100%;
} */
</style>
