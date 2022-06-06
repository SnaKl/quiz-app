<!-- List of the question available on the Admin Panel (it's like the home page of the admin panel) -->
<template>
  <div class="adminHeader">
    <div>
      <h1><I18nTextComponent i18n-key="adminPage" /></h1>
      <h2><I18nTextComponent i18n-key="questionList" /></h2>
    </div>
    <button
      class="btn btn-primary addQuestionButton"
      @click="() => this.$router.push('/admin/questions/add')"
    >
      <I18nTextComponent i18n-key="addQuestion" />
    </button>
  </div>
  <table class="table" v-if="questions">
    <thead class="thead-dark">
      <tr>
        <th scope="col">#</th>
        <th scope="col"><I18nTextComponent i18n-key="title" /></th>
        <th scope="col"><I18nTextComponent i18n-key="viewQuestion" /></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="question in questions" v-bind:key="question.position">
        <th scope="row">{{ question.position }}</th>
        <td>{{ question.title }}</td>
        <td>
          <a :href="'/admin/questions/' + question.position"
            ><I18nTextComponent i18n-key="viewQuestion"
          /></a>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuizApiService from '../services/QuizApiService';
import I18nTextComponent from '../components/I18nTextComponent.vue';

export default {
  name: 'AdminPageQuestions',
  data() {
    return {
      /** Questions to display */
      questions: []
    };
  },
  methods: {
    /** Fetch questions from a backend call (added method in the backend) */
    async fetchQuestions() {
      const { data } = await QuizApiService.call('get', '/questions');
      this.questions = data;
    }
  },
  /** Check if the user is authorized to be here, and fetch the questions */
  async created() {
    const token = ParticipationStorageService.getToken();
    if (!token) this.$router.push('/questions');

    this.fetchQuestions();
  },
  components: { I18nTextComponent }
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
