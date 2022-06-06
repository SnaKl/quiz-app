<!-- Component used to display a question in Admin Panel -->
<template>
  <h1 class="my-5"><I18nTextComponent i18n-key="adminPage" /></h1>
  <div class="d-flex justify-content-between">
    <h2><I18nTextComponent i18n-key="seeQuestion" /></h2>
    <nav>
      <button
        class="btn btn-warning"
        @click="() => $router.push(`/admin/questions/`)"
        type="button"
      >
        <i class="bi bi-arrow-left"></i> <I18nTextComponent i18n-key="cancel" />
      </button>
      <button class="btn btn-danger mx-2" @click="deleteQuestion" type="button">
        <i class="bi bi-trash-fill"></i> <I18nTextComponent i18n-key="delete" />
      </button>
      <button
        class="btn btn-primary"
        @click="
          () => $router.push(`/admin/questions/${$route.params.pos}/edit`)
        "
        type="button"
      >
        <i class="bi bi-pencil-fill"></i>
        <I18nTextComponent i18n-key="editQuestion" />
      </button>
    </nav>
  </div>
  <QuestionDisplay v-if="question" :question="question" show-answer />
</template>

<script>
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';
import ParticipationStorageService from '@/services/ParticipationStorageService';
import I18nTextComponent from '@/components/I18nTextComponent.vue';

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
    QuestionDisplay,
    I18nTextComponent
  },
  /** Fetch question on mount */
  async created() {
    if (this.$route.params.pos) {
      await this.fetchQuestion();
    }
  }
};
</script>
