<template>
  <div class="adminHeader">
    <div>
      <h1>Admin page</h1>
      <h2>Edition de question</h2>
    </div>

    <div>
      <button
        class="btn btn-danger mx-2"
        @click="() => $router.push('/admin/questions')"
      >
        Cancel
      </button>
      <button class="btn btn-primary" @click="saveQuestion">
        Save question
      </button>
    </div>
  </div>

  <div v-if="!existingQuestion || question">
    <QuestionDisplay
      :edit="true"
      ref="question"
      :nb-of-question="nbOfQuestion"
      :question="question"
    />
  </div>
</template>

<script>
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';

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
    },
    async fetchQuizInfo() {
      const { data } = await QuizApiService.call('get', '/quiz-info');
      this.nbOfQuestion = data.size;
    }
  },
  data() {
    return {
      /** Indique si on est en mode édition ou en mode création  */
      existingQuestion: false,
      question: undefined,
      nbOfQuestion: undefined
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    if (this.$route.params.pos) {
      this.existingQuestion = true;
      await this.fetchQuestion();
      await this.fetchQuizInfo();
    }
  }
};
</script>

<style>
.adminHeader {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px;
}
</style>
