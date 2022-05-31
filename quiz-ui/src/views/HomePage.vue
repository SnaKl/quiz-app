<template>
  <h1>Home page</h1>

  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  <router-link to="/admin">ADMIN</router-link>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      registeredScores: []
    };
  }
};
</script>
