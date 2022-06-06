<!-- Simple component used to create a new quizz and take the player name -->
<script>
import participationStorageService from '@/services/ParticipationStorageService';
import I18nTextComponent from '@/components/I18nTextComponent.vue';

export default {
  name: 'NewQuizPage',
  data() {
    return {
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions'); //Router is already integrated, no need to import it
    }
  },
  components: { I18nTextComponent }
};
</script>

<template>
  <h1 class="my-5"><I18nTextComponent i18n-key="newQuizTitle" /></h1>
  <div class="text-center pt-5">
    <h2 class="my-5">Nouveau quiz</h2>
    <form id="quiz-page-form" @submit="launchNewQuiz">
      <label for="quiz-page-form-username"
        ><label for="quiz-page-form-username">Saisissez votre nom</label></label
      >
      <div class="input-group w-25 mx-auto mt-3">
        <input
          type="text"
          v-model="username"
          class="form-control"
          id="quiz-page-form-username"
          placeholder="Pseudonyme"
        />
        <button type="submit" class="btn btn-outline-danger">
          <label for="quiz-page-form-username">Saisissez votre nom</label>
        </button>
      </div>
    </form>
  </div>
</template>
