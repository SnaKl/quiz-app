<!-- Home page of the application -->
<template>
  <div id="homeContainer">
    <h1>Home page</h1>
    <router-link
      to="/start-new-quiz-page"
      id="title"
      class="btn btn-lg btn-outline-primary"
      >Démarrer le quiz !</router-link
    >
    <router-link to="/admin" id="bottomLink" class="btn"
      >Administration</router-link
    >
  </div>
</template>

<script>
export default {
  name: 'HomePage'
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
