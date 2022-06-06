<!-- Home page of the application -->
<template>
  <div id="homeContainer">
    <h1><I18nTextComponent i18n-key="homePage" /></h1>
    <router-link
      to="/start-new-quiz-page"
      id="title"
      class="btn btn-lg btn-outline-primary"
      ><I18nTextComponent i18n-key="startQuiz"
    /></router-link>
    <router-link to="/admin" id="bottomLink" class="btn"
      ><I18nTextComponent i18n-key="administrationButton"
    /></router-link>
    <select @change="handleLanguageChange" :value="language">
      <option value="fr">Français</option>
      <option value="en">Anglais</option>
    </select>
  </div>
</template>

<script>
import i18nService from '../services/i18nService';
import I18nTextComponent from '../components/I18nTextComponent.vue';
export default {
  name: 'HomePage',
  components: { I18nTextComponent },
  data() {
    return {
      language: i18nService.getApplicationLanguage()
    };
  },
  methods: {
    handleLanguageChange(evt) {
      i18nService.setApplicationLanguage(evt.currentTarget.value);
      this.language = evt.currentTarget.value;
      //TODO: Trouver une méthode plus propre pour forcer le changement de la langue
      location.reload();
    }
  }
};
</script>

<style scoped>
#homeContainer {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
