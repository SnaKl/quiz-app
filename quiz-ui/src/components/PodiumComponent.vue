<!-- Simple component who display a podium for 3 names -->
<script>
export default {
  name: 'PodiumComponent',
  props: {
    /** First Person in the leaderboard */
    firstName: String,
    /** Second Person in the leaderboard */
    secondName: String,
    /** Third Person in the leaderboard */
    thirdName: String
  }
};
</script>

<template>
  <div class="podium">
    <div class="stepContainer">
      <div class="name">{{ secondName }}</div>
      <div class="step2">2</div>
    </div>
    <div class="stepContainer">
      <div class="name">{{ firstName }}</div>
      <div class="step1">1</div>
    </div>
    <div class="stepContainer">
      <div class="name">{{ thirdName }}</div>
      <div class="step3">3</div>
    </div>
  </div>
</template>

<style>
.podium {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 15vh;
  width: 20vw;
}
.stepContainer {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  height: 100%;
}
.name {
  width: 100%;
  text-align: center;
  margin-top: auto;
}
.step1 {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 1000;
  font-size: 2em;
  height: 90%;
  background-color: green;
  margin-top: 0;
}
.step2 {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 1000;
  font-size: 1.5em;
  height: 60%;
  background-color: yellow;
  margin-top: 0;
}
.step3 {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 1000;
  font-size: 1.25em;
  height: 30%;
  background-color: red;
  margin-top: 0;
}
</style>
