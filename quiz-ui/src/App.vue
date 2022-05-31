<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <RouterLink to="/" class="nav-link">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/about" class="nav-link">About</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/score" class="nav-link">Score</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
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
