<script>
import participationStorageService from '@/services/ParticipationStorageService';

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
      this.$router.push('/questions'); //router déjà pré-intégré, no import
    }
  }
};
</script>

<template>
  <div id="newQuizContainer">
    <h1>Test New Quiz Page</h1>
    <form id="quiz-page-form" @submit="launchNewQuiz">
      <span style="display: inline-block">
        <label for="quiz-page-form-username">Saisissez votre nom:</label>
        <input
          type="text"
          v-model="username"
          class="form-control my-3 w-50"
          id="quiz-page-form-username"
          placeholder="Username"
        />
      </span>

      <button type="submit" class="btn btn-outline-danger">GO!</button>
    </form>
  </div>
</template>

<style>
#newQuizContainer {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
