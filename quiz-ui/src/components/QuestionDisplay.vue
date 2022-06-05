<template>
  <div id="QuestionContainer">
    <!-- SEULEMENT POUR L'EDITION, POSITION DE LA QUESTION -->
    <label for="position" v-if="edit">Position</label>
    <input
      v-if="edit"
      id="position"
      type="number"
      class="form-control m-2 w-25"
      placeholder="position"
      min="1"
      :max="nbOfQuestion ? nbOfQuestion + 1 : undefined"
      v-model="editedQuestion.position"
    />

    <!-- TITRE DE LA QUESTION -->
    <h2 v-if="!edit">{{ question.title }}</h2>
    <input
      v-else
      type="text"
      class="form-control w-25"
      v-model="editedQuestion.title"
      placeholder="Titre de la question"
    />

    <!-- ENONCE DE LA QUESTION -->
    <p v-if="!edit">{{ question.text }}</p>
    <input
      v-else
      type="text"
      class="form-control m-2 w-25"
      v-model="editedQuestion.text"
      placeholder="Contenu de la question"
    />

    <!-- IMAGE DE LA QUESTION -->
    <img v-if="!edit" class="display-img" :src="question.image" />
    <div v-else class="fileDeposit m-2" @click="() => $refs.file.click()">
      <p v-if="!editedQuestion.image">Déposer un fichier...</p>
      <img v-else :src="editedQuestion.image" class="preview-img" />
      <!-- Input caché, permet de gérer le fichier passé en paramètre -->
      <input
        ref="file"
        type="file"
        style="display: none"
        accept="image/png, image/jpeg"
        @change="handleFileInput()"
      />
    </div>

    <!-- REPONSES DE LA QUESTION -->
    <div id="AnswersContainer">
      <div
        v-for="(answer, index) in question != undefined
          ? question.possibleAnswers
          : editedQuestion.possibleAnswers"
        @click="$emit('answer-selected', index + 1)"
        v-bind:key="index"
        :class="`Answer alert alert-${possibleQuizzClasses[index]}`"
      >
        <p v-if="!edit" class="text-center">{{ answer.text }}</p>
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
            v-model="editedQuestion.possibleAnswers[index].isCorrect"
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
    question: {
      type: Object,
      required: false
    },
    edit: {
      type: Boolean,
      required: false
    },
    /** Utile pour aider l'utilisateur à choisir une position de question */
    nbOfQuestion: {
      type: Number,
      required: false
    }
  },
  emits: ['answer-selected'],
  data() {
    return {
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
    handleFileInput() {
      //Récuprèe le fichier de l'input et le transforme en URL base64
      const file = this.$refs.file.files[0];
      const reader = new FileReader();
      reader.onload = () => (this.editedQuestion.image = reader.result);
      reader.readAsDataURL(file);
    }
  },
  created() {
    if (this.edit && this.question) {
      this.editedQuestion = this.question;
    }
  }
};
</script>

<style scoped>
#QuestionContainer {
  height: 100%;
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
