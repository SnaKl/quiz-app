<!-- A more complex component, permit to display and edit a question -->
<!-- We used the same component for edition and display since the layout of the two are similar -->

<template>
  <div id="QuestionContainer">
    <!-- EDITION MODE ONLY, POSITION OF THE QUESTION -->
    <label for="position" v-if="edit">Position</label>
    <input
      v-if="edit"
      id="position"
      type="number"
      class="form-control m-2 w-50"
      placeholder="position"
      min="1"
      :max="nbOfQuestion ? nbOfQuestion + 1 : undefined"
      v-model="editedQuestion.position"
    />

    <!-- TITLE OF THE QUESTION -->
    <h2 v-if="!edit">{{ question.title }}</h2>
    <input
      v-else
      type="text"
      class="form-control w-50"
      v-model="editedQuestion.title"
      placeholder="Titre de la question"
    />

    <!-- TEXT OF THE QUESTION -->
    <p v-if="!edit">{{ question.text }}</p>
    <input
      v-else
      type="text"
      class="form-control m-2 w-50"
      v-model="editedQuestion.text"
      placeholder="Contenu de la question"
    />

    <!-- QUESTION IMAGE -->
    <img v-if="!edit" class="display-img" :src="question.image" />
    <div v-else class="fileDeposit m-2" @click="() => $refs.file.click()">
      <p v-if="!editedQuestion.image">Déposer un fichier...</p>
      <img v-else :src="editedQuestion.image" class="preview-img" />
      <!-- Hidden input, used to handle img input -->
      <input
        ref="file"
        type="file"
        style="display: none"
        accept="image/png, image/jpeg"
        @change="handleFileInput()"
      />
    </div>

    <!-- Answers of the question -->
    <div id="AnswersContainer">
      <div
        v-for="(answer, index) in question != undefined
          ? question.possibleAnswers
          : editedQuestion.possibleAnswers"
        @click="$emit('answer-selected', index + 1)"
        v-bind:key="index"
        :class="`Answer alert alert-${possibleQuizzClasses[index]}`"
      >
        <div v-if="!edit">
          <p class="text-center">{{ answer.text }}</p>
          <!-- If we want to show the right answer, this text will be printed -->
          <hr v-if="showAnswer && answer.isCorrect" />
          <p v-if="showAnswer && answer.isCorrect" class="text-center">
            <strong>Réponse correcte</strong>
          </p>
        </div>
        <div v-else class="AnswerEdition">
          <input
            type="text"
            class="form-control m-2"
            v-model="editedQuestion.possibleAnswers[index].text"
            placeholder="Réponse"
          />
          <input
            type="checkbox"
            class="form-check-input"
            @change="handleAnswerChange(index)"
            :checked="editedQuestion.possibleAnswers[index].isCorrect"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuestionDisplay',
  props: {
    /** Question to display, or, in edit mode, the question to edit.
     * If no question is given, we will assume that we are in "creation mode" and create a new from scratch
     */
    question: {
      type: Object,
      required: false
    },
    /** If the question is in edit mode */
    edit: {
      type: Boolean,
      required: false
    },
    /** Used in edit mode for helping the user to choose a position */
    nbOfQuestion: {
      type: Number,
      required: false
    },
    /** Do we need to show the right answer */
    showAnswer: {
      type: Boolean,
      required: false
    }
  },
  emits: ['answer-selected'],
  data() {
    return {
      /** Currently edited question */
      editedQuestion: {
        image: '',
        position: 1,
        title: '',
        text: '',
        possibleAnswers: [
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false }
        ]
      },
      /** Used to set a different class (and color) to each answer (handle up to 6 answers) */
      possibleQuizzClasses: [
        'primary',
        'warning',
        'success',
        'danger',
        'secondary',
        'info'
      ]
    };
  },
  methods: {
    /** Method for handling the file upload, get the file from the input and convert it to Data URL (and set it in editedQuestion) */
    handleFileInput() {
      const file = this.$refs.file.files[0];
      const reader = new FileReader();
      reader.onload = () => (this.editedQuestion.image = reader.result);
      reader.readAsDataURL(file);
    },
    /** Method for handling change of right answer, since there is only one good answer, we switch other to false when clicked */
    handleAnswerChange(pos) {
      const currentState = this.editedQuestion.possibleAnswers[pos].isCorrect;
      for (let i = 0; i < this.editedQuestion.possibleAnswers.length; i++) {
        this.editedQuestion.possibleAnswers[i].isCorrect = false;
      }
      this.editedQuestion.possibleAnswers[pos].isCorrect = !currentState;
    }
  },
  created() {
    if (this.edit && this.question) {
      // We set the question to edit to be equal to the prop in edit mode
      this.editedQuestion = this.question;
    }
  }
};
</script>

<style scoped>
#QuestionContainer {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}

.display-img {
  border-radius: 20px;
  border: 5px solid black;
  width: auto;
  max-height: 30vh;
}

.preview-img {
  width: 100%;
  height: 100%;
}

.fileDeposit {
  border-radius: 20px;
  border: 5px dashed black;
  width: 30vw;
  height: 30vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

#AnswersContainer {
  display: flex;
  justify-content: space-evenly;
  flex-flow: row wrap;
}

.Answer {
  margin: 10px;
  width: 40%;
}

.AnswerEdition {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
