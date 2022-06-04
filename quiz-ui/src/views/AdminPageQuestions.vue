<template>
  <h1>Admin page</h1>
  <h2>Liste des questions</h2>
  <button
    class="btn btn-primary"
    @click="() => this.$router.push('/admin/questions/add')"
  >
    Ajouter une question
  </button>
  <table class="table" v-if="questions">
    <thead class="thead-dark">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Title</th>
        <th scope="col">Edit</th>
        <th scope="col">Delete</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="question in questions" v-bind:key="question.position">
        <th scope="row">{{ question.position }}</th>
        <td>{{ question.title }}</td>
        <td>
          <a :href="'/admin/questions/' + question.position">Modifier</a>
        </td>
        <td>
          <a @click="e => deleteQuestion(question.position)" href="#">Delete</a>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'AdminPageQuestions',
  data() {
    return {
      questions: []
    };
  },
  methods: {
    async fetchQuestions() {
      const { data } = await QuizApiService.call('get', '/questions');
      this.questions = data;
    },
    async deleteQuestion(pos) {
      const token = ParticipationStorageService.getToken();
      await QuizApiService.call(
        'delete',
        `/questions/${pos}`,
        undefined,
        token
      );
      await this.fetchQuestions();
    }
  },
  async created() {
    const token = ParticipationStorageService.getToken();
    if (!token) this.$router.push('/questions');

    this.fetchQuestions();
  }
};
</script>
