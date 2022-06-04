<template>
  <h1>Admin page</h1>
  <h2>Edition de question</h2>
  <div v-if="!existingQuestion || question">
    <button
      v-if="!existingQuestion"
      class="btn btn-primary"
      @click="saveQuestion"
    >
      Add question
    </button>
    <button v-else class="btn btn-warning" @click="saveQuestion">
      Edit question
    </button>
    <QuestionDisplay :edit="true" ref="question" :question="question" />
  </div>
</template>

<script>
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuestionDisplay from '../components/QuestionDisplay.vue';
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'AdminPageQuestionEdition',
  methods: {
    async saveQuestion() {
      const token = ParticipationStorageService.getToken();
      const question = this.$refs.question.editedQuestion;
      if (!this.existingQuestion)
        await QuizApiService.call('post', '/questions', question, token);
      else
        await QuizApiService.call(
          'put',
          `/questions/${this.$route.params.pos}`,
          question,
          token
        );
      this.$router.push('/admin/questions');
    },
    async fetchQuestion() {
      const { data } = await QuizApiService.call(
        'get',
        `/questions/${this.$route.params.pos}`
      );
      this.question = data;
    }
  },
  data() {
    return {
      /** Indique si on est en mode édition ou en mode création  */
      existingQuestion: false,
      question: undefined
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    if (this.$route.params.pos) {
      this.existingQuestion = true;
      await this.fetchQuestion();
    }
  }
};
</script>
