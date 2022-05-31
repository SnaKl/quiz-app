<template>
  <div>
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    <img v-if="question.image" :src="question.image" />
    <div>
      <a
        v-for="(answer, index) in question?.possibleAnswers"
        @click="$emit('answer-selected', index + 1)"
        v-bind:key="index"
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
