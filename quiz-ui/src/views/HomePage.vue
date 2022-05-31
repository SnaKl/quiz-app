<template>
  <div id="homeContainer">
    <h1>Home page</h1>
    <router-link to="/start-new-quiz-page" id="title"
      >Démarrer le quiz !</router-link
    >
    <router-link to="/admin" id="bottomLink">Admin panel</router-link>
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

<style scoped>
#homeContainer {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
