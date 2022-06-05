<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <RouterLink to="/" class="nav-link"
            ><i class="bi bi-house-fill"></i> Home</RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink to="/about" class="nav-link"
            ><i class="bi bi-info-circle-fill"></i> About</RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink to="/score" class="nav-link"
            ><i class="bi bi-bar-chart-fill"></i> Score</RouterLink
          >
        </li>
      </ul>
    </div>
  </nav>
</template>

<style></style>
