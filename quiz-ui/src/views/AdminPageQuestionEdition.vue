<template>
  <h1>Admin page</h1>
  <h2>Edition de question</h2>
  <button class="btn btn-primary" @click="createQuestion">Add question</button>
  <QuestionDisplay :edit="true" ref="question" />
</template>

<script>
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuestionDisplay from '../components/QuestionDisplay.vue';
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'AdminPageQuestionEdition',
  methods: {
    async createQuestion() {
      const token = ParticipationStorageService.getToken();
      const question = this.$refs.question.editedQuestion;
      await QuizApiService.call('post', '/questions', question, token);
      this.$router.push('/admin/questions');
    }
  },
  async created() {
    const token = ParticipationStorageService.getToken();
    if (!token) this.$router.push('/questions');
  },
  components: {
    QuestionDisplay
  }
};
</script>
