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
    <p v-else>Loading ...</p>
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
      currentQuestion: null,
      currentQuestionPosition: 1,
      totalNumberOfQuestion: null,
      selectedAnswers: []
    };
  },
  methods: {
    async loadQuestionByPosition() {
      const { data: quizInfo } = await QuizApiService.call('get', '/quiz-info');
      this.totalNumberOfQuestion = quizInfo.size;
      const { data } = await QuizApiService.call(
        'get',
        `/questions/${this.currentQuestionPosition}`
      );
      this.currentQuestion = data;
    },
    async answerClickedHandler(answerPosition) {
      this.selectedAnswers.push(answerPosition);
      this.currentQuestionPosition++;
      if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
        this.endQuiz();
      } else {
        this.loadQuestionByPosition();
      }
    },
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
