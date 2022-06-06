<!-- Component used to display a question in Admin Panel -->
<template>
  <div class="adminHeader">
    <div>
      <h1>Admin page</h1>
      <h2>Edition de question</h2>
    </div>

    <div>
      <button
        class="btn btn-warning mx-2"
        @click="() => $router.push('/admin/questions')"
      >
        Cancel
      </button>
      <button class="btn btn-danger mx-2" @click="deleteQuestion">
        Delete
      </button>
      <button
        class="btn btn-primary"
        @click="
          () => $router.push(`/admin/questions/${$route.params.pos}/edit`)
        "
      >
        Edit question
      </button>
    </div>
  </div>

  <QuestionDisplay v-if="question" :question="question" show-answer />
</template>

<script>
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';
import ParticipationStorageService from '@/services/ParticipationStorageService';

export default {
  name: 'AdminPageQuestionView',
  methods: {
    /** Used to fecth the question from the position of the question (passed by a route parameter) */
    async fetchQuestion() {
      const { data } = await QuizApiService.call(
        'get',
        `/questions/${this.$route.params.pos}`
      );
      this.question = data;
    },
    /** Used to delete a question from the position of the question (passed by a route parameter) */
    async deleteQuestion() {
      const token = ParticipationStorageService.getToken();
      await QuizApiService.call(
        'delete',
        `/questions/${this.$route.params.pos}`,
        undefined,
        token
      );
      this.$router.push('/admin/questions');
    }
  },
  data() {
    return {
      /** Displayed Question */
      question: undefined
    };
  },
  components: {
    QuestionDisplay
  },
  /** Fetch question on mount */
  async created() {
    if (this.$route.params.pos) {
      await this.fetchQuestion();
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
