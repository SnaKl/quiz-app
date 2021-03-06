<!-- Leaderboard view (with a nice podium) -->

<script>
import participationStorageService from '@/services/ParticipationStorageService';
import QuizApiService from '@/services/QuizApiService';
import PodiumComponent from '@/components/PodiumComponent.vue';
import I18nTextComponent from '../components/I18nTextComponent.vue';

export default {
  data() {
    return {
      /** Name of the player */
      name: null,
      /** Score of the player */
      personalScore: 0,
      /** Position of the player score, among other scores */
      position: 0,
      /** Registered scores */
      scores: []
    };
  },
  /** On creation, fetch other scores and compute the actual position of the player */
  async created() {
    const { data } = await QuizApiService.call('get', '/quiz-info');

    //Get information of the player from localStorage
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
  },
  components: { PodiumComponent, I18nTextComponent }
};
</script>

<template>
  <div class="score">
    <div v-if="name" class="nameBox">
      <h1>{{ name }}</h1>
      <h2>Score: {{ personalScore }}</h2>
      <h2>#{{ position }}</h2>
    </div>
    <div v-else>
      <p><I18nTextComponent i18n-key="noQuizLaunched" /></p>
      <router-link to="/start-new-quiz-page">
        <button><I18nTextComponent i18n-key="startQuiz" /></button>
      </router-link>
    </div>
    <div class="scoreBox">
      <h1><I18nTextComponent i18n-key="leaderBoard" /></h1>
      <PodiumComponent
        v-if="scores.length > 2"
        :firstName="scores[0].playerName"
        :secondName="scores[1].playerName"
        :thirdName="scores[2].playerName"
      />
      <div
        v-for="(score, index) in scores.slice(0, 5)"
        :key="index"
        class="score-container"
      >
        <span style="font-weight: bold">#{{ index + 1 }}</span>
        <span>{{ score.playerName }}</span>
        <span>Score: {{ score.score }}</span>
      </div>
    </div>
  </div>
</template>

<style>
.score {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.nameBox {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin: 20px;
}

.score-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin: 20px;
  border: 2px dashed black;
}
</style>
