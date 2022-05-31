<template>
  <h1>Test New Quiz Page</h1>
  <form id="quiz-page-form">
    <label for="quiz-page-form-username">Saisissez votre nom:</label>
    <input type="text" v-model="username" class="form-control my-3 w-50" id="quiz-page-form-username" placeholder="Username"/>
    <button @click="launchNewQuiz" type="button" class="btn btn-outline-danger">GO!</button> <!--v-on:click=""-->
  </form>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username : ''
    };
  },
  methods:{
    launchNewQuiz(){
      participationStorageService.savePlayerName(this.username);
      //console.log("Launch new quiz with", participationStorageService.getPlayerName());
      this.$router.push('/questions'); //router déjà pré-intégré, no import
    },
  },
  async created() {
    console.log("Composant Quiz Page 'created'");
  },
};
</script>