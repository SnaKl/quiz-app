<!-- Component used to edit a question (in creation and edition mode) -->
<template>
  <h1 class="my-5"><I18nTextComponent i18n-key="adminPage" /></h1>
  <div class="d-flex justify-content-between">
    <h2><I18nTextComponent i18n-key="questionEditing" /></h2>
    <nav>
      <button
        class="btn btn-danger mx-2"
        @click="() => $router.push('/admin/questions')"
        type="button"
      >
        <i class="bi bi-arrow-left"></i> <I18nTextComponent i18n-key="cancel" />
      </button>
      <button class="btn btn-primary" @click="saveQuestion" type="button">
        <i class="bi bi-save"></i> <I18nTextComponent i18n-key="saveQuestion" />
      </button>
    </nav>
  </div>
  <!-- Only show question when we have loaded it -->
  <div v-if="!existingQuestion || question">
    <QuestionDisplay
      :edit="true"
      ref="question"
      :nb-of-question="nbOfQuestion"
      :question="question"
    />
  </div>
  <span v-else><I18nTextComponent i18n-key="loading" /></span>
</template>

<script>
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';
import I18nTextComponent from '@/components/I18nTextComponent.vue';

export default {
  name: 'AdminPageQuestionEdition',
  methods: {
    /** Permit to create or edit a question (depend if the question was existing before) */
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
    /** Used in edition mode, fetch the question to edit */
    async fetchQuestion() {
      const { data } = await QuizApiService.call(
        'get',
        `/questions/${this.$route.params.pos}`
      );
      this.question = data;
    },
    /** Fetch info about the quiz (used to get the total number of questions) */
    async fetchQuizInfo() {
      const { data } = await QuizApiService.call('get', '/quiz-info');
      this.nbOfQuestion = data.size;
    }
  },
  data() {
    return {
      /** Show if the question was existing before (if we are in edtion mode)  */
      existingQuestion: false,
      /** Question to edit (and to pass to QuestionDisplay) */
      question: undefined,
      /** Total amount of questions */
      nbOfQuestion: undefined
    };
  },
  components: {
    QuestionDisplay,
    I18nTextComponent
  },
  /** On creation, check if we are in edition mode (if we have the pos of the question to edit)
   * If true, we handle things such the fetch of this question
   */
  async created() {
    if (this.$route.params.pos) {
      this.existingQuestion = true;
      await this.fetchQuestion();
    }
    await this.fetchQuizInfo();
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
