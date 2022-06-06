<!-- General informations about the application -->
<template>
  <div class="about">
    <h1><I18nTextComponent i18n-key="aboutPage" /></h1>
  </div>
</template>

<script>
import I18nTextComponent from '../components/I18nTextComponent.vue';

export default {
  components: { I18nTextComponent }
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
