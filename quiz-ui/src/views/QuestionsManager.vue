<!-- Component to handle the flow of the quizz -->

<template>
  <div id="QuestionManagerContainer">
    <h1
      v-if="
        currentQuestion && currentQuestion.position == currentQuestionPosition
      "
    >
      Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}
    </h1>
    <QuestionDisplay
      v-if="
        currentQuestion && currentQuestion.position == currentQuestionPosition
      "
      :question="currentQuestion"
      :edit="false"
      @answer-selected="answerClickedHandler"
    />
    <p v-else>Chargement ...</p>
  </div>
</template>

<script>
import participationStorageService from '@/services/ParticipationStorageService';
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';
export default {
  name: 'QuestionManager',
  components: {
    QuestionDisplay
  },
  async created() {
    await this.loadQuestionByPosition();
  },
  data() {
    return {
      /** Currently displayed question */
      currentQuestion: null,
      /** Currently displayed question position (start to 1) */
      currentQuestionPosition: 1,
      /** Total number of questions (used for display) */
      totalNumberOfQuestion: null,
      /** Currently selected answers by the player */
      selectedAnswers: []
    };
  },
  methods: {
    /** Get question by using his position from the back end */
    async loadQuestionByPosition() {
      const { data: quizInfo } = await QuizApiService.call('get', '/quiz-info');
      this.totalNumberOfQuestion = quizInfo.size;
      const { data } = await QuizApiService.call(
        'get',
        `/questions/${this.currentQuestionPosition}`
      );
      this.currentQuestion = data;
    },
    /** Handle the answer of the player, and finish the quizz if its the last question */
    async answerClickedHandler(answerPosition) {
      this.selectedAnswers.push(answerPosition);
      this.currentQuestionPosition++;
      if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
        this.endQuiz();
      } else {
        this.loadQuestionByPosition();
      }
    },
    /** All the process at the end of the quizz */
    async endQuiz() {
      const { data } = await QuizApiService.call('post', '/participations', {
        playerName: participationStorageService.getPlayerName(),
        answers: this.selectedAnswers
      });
      participationStorageService.saveScore(data.score);
      this.$router.push('/score');
    }
  }
};
</script>

<style scoped>
#QuestionManagerContainer {
  height: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
</style>
