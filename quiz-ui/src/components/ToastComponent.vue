<!-- Utility component, used to give feedback to the user when an error ocurr -->
<script setup>
import I18nTextComponent from './I18nTextComponent.vue';
</script>

<template>
  <div class="toast-container position-absolute top-right">
    <div
      id="toast-err-war"
      class="toast"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-header bg-danger-custom-50 text-dark">
        <strong class="me-auto"><I18nTextComponent i18n-key="error" /></strong>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="toast"
          aria-label="Close"
        ></button>
      </div>
      <div class="toast-body bg-danger-custom-10"></div>
    </div>
  </div>
</template>

<style>
.top-right {
  right: 50px !important;
  top: 100px !important;
}

.bg-danger-custom-50 {
  background-color: #ed99a1;
}

.bg-danger-custom-10 {
  background-color: #fceaec;
}
</style>
