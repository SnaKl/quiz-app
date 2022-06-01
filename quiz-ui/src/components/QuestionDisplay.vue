<template>
  <div id="QuestionContainer">
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    <img v-if="question.image" :src="question.image" />
    <div id="AnswersContainer">
      <div
        v-for="(answer, index) in question?.possibleAnswers"
        @click="$emit('answer-selected', index + 1)"
        v-bind:key="index"
        :class="`Answer alert alert-${possibleQuizzClasses[index]}`"
      >
        <p class="text-center">{{ answer.text }}</p>
      </div>
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
  emits: ['answer-selected'],
  data() {
    return {
      possibleQuizzClasses: [
        'primary',
        'warning',
        'success',
        'danger',
        'secondary',
        'info'
      ]
    };
  }
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
  margin: 10px;
  width: 40%;
}
</style>
