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
  <h1>Test New Quiz Page</h1>
  <form id="quiz-page-form" @submit="launchNewQuiz">
    <label for="quiz-page-form-username">Saisissez votre nom:</label>
    <input
      type="text"
      v-model="username"
      class="form-control my-3 w-50"
      id="quiz-page-form-username"
      placeholder="Username"
    />
    <button type="submit" class="btn btn-outline-danger">GO!</button>
    <!--v-on:click=""-->
  </form>
</template>

<style></style>
