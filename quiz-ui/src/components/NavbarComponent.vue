<!-- Utility Component containing the main navBar of the application -->
<script setup>
import { RouterLink } from 'vue-router';
import I18nTextComponent from './I18nTextComponent.vue';
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <button
      class="navbar-toggler mr-5"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarSupportedContent"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <RouterLink to="/" class="nav-link"
            ><i class="bi bi-house-fill"></i>
            <I18nTextComponent i18n-key="homeLink"
          /></RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/about" class="nav-link"
            ><i class="bi bi-info-circle-fill"></i>
            <I18nTextComponent i18n-key="aboutLink"
          /></RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/score" class="nav-link"
            ><i class="bi bi-bar-chart-fill"></i>
            <I18nTextComponent i18n-key="scoreLink"
          /></RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/admin" class="nav-link"
            ><i class="bi bi-tools"></i> Administration</RouterLink
          >
        </li>
      </ul>
    </div>
  </nav>
</template>

<style></style>
