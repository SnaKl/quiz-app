<script>
import participationStorageService from '@/services/ParticipationStorageService';
import QuizApiService from '@/services/QuizApiService';

export default {
  data() {
    return {
      name: null,
      personalScore: 0,
      position: 0,
      scores: []
    };
  },
  async created() {
    const { data } = await QuizApiService.call('get', '/quiz-info');
    const name = participationStorageService.getPlayerName();
    if (name) this.name = name;

    const score = participationStorageService.getScore();
    if (score) {
      this.personalScore = score;

      for (let i = 0; i < data.scores.length; i++) {
        if (data.scores[i].score <= this.personalScore) {
          this.position = i + 1;
          break;
        }
      }
    }

    this.scores = data.scores.slice(0, 5);
  }
};
</script>

<template>
  <div class="score">
    <h1>Score page</h1>
    <div v-if="name">
      <p>Votre nom d'utilisateur: {{ name }}</p>
      <p>Votre score: {{ personalScore }}</p>
      <p>Votre position: {{ position }}</p>
    </div>
    <div v-else>
      <p>Vous n'avez pas encore lancé de quiz</p>
      <router-link to="/start-new-quiz-page">
        <button>Démarrer le quiz !</button>
      </router-link>
    </div>
    <h1>Best scores</h1>
    <ul>
      <li v-for="(score, index) in scores" :key="index">
        Name: {{ score.playerName }}, Score: {{ score.score }}
      </li>
    </ul>
  </div>
</template>

<style></style>
