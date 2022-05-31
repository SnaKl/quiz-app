<template>
  <div id="QuestionContainer">
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    <img v-if="question.image" :src="question.image" />
    <div id="AnswersContainer">
      <a
        v-for="(answer, index) in question?.possibleAnswers"
        @click="$emit('answer-selected', index + 1)"
        v-bind:key="index"
        class="Answer"
      >
        {{ answer.text }}
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuestionManager',
  props: {
    question: {
      type: Object
    }
  },
  emits: ['answer-selected']
};
</script>

<style scoped>
#QuestionContainer {
  height: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

img {
  border-radius: 20px;
  border: 5px solid black;
  width: auto;
  max-height: 30vh;
}

#AnswersContainer {
  display: flex;
  justify-content: space-evenly;
  flex-flow: row wrap;
}

.Answer {
  border: 2px solid black;
  border-radius: 5px;
  margin: 10px;
  padding: 10px;
  width: 40%;
}
</style>
