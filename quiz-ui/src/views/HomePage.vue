<!-- Home page of the application -->
<template>
  <div id="homeContainer">
    <h1 class="my-5"><I18nTextComponent i18n-key="homePage" /></h1>
    <div class="text-center pt-5">
      <h2 class="my-5">Bienvenue sur Quiz-App</h2>
      <article>Testez vos connaissances sur la culture informatique !</article>
      <router-link
        to="/start-new-quiz-page"
        id="title"
        class="btn btn-lg btn-outline-primary mt-5"
        ><I18nTextComponent i18n-key="startQuiz"
      /></router-link>
      <select
        @change="handleLanguageChange"
        :value="language"
        class="form-select form-select-sm mt-3 mx-auto"
        style="width: 10%"
      >
        <option value="fr">Français</option>
        <option value="en">English</option>
      </select>
    </div>
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
