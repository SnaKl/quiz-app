/** Dictionary with all the string of the application */
const i18nTranslation = {
  aboutPage: {
    fr: 'Ceci est une page de renseignement',
    en: 'This is an about page'
  },
  homePage: {
    fr: "Page d'accueuil",
    en: 'Home Page'
  },
  startQuiz: {
    fr: 'Démarrer le quiz !',
    en: 'Start the quiz !'
  },
  administrationButton: {
    fr: 'Administration',
    en: 'Administration'
  },
  newQuizTitle: {
    fr: 'Nouveau quiz !',
    en: 'New Quiz !'
  },
  enterYourName: {
    fr: 'Saisissez votre nom :',
    en: 'Enter your name :'
  },
  goButton: {
    fr: "C'est parti !",
    en: 'Go !'
  },
  leaderBoard: {
    fr: 'Tableau des scores',
    en: 'Leaderboard'
  },
  noQuizLaunched: {
    fr: "Personne n'as encore lancé de quiz !",
    en: 'Nobody have lauched the quizz !'
  },
  homeLink: {
    fr: ' Accueil',
    en: ' Home'
  },
  aboutLink: {
    fr: ' A propos',
    en: ' About'
  },
  scoreLink: {
    fr: ' Score',
    en: ' Score'
  },
  adminPage: {
    fr: "Page d'administration",
    en: 'Admin Page'
  },
  adminPassword: {
    fr: 'Mot de passe admin :',
    en: 'Admin password :'
  },
  connect: {
    fr: 'Connexion',
    en: 'Connect'
  },
  error: {
    fr: 'Erreur',
    en: 'Error'
  },
  questionList: {
    fr: 'Liste des questions',
    en: 'Question List'
  },
  addQuestion: {
    fr: 'Ajouter une question',
    en: 'Add question'
  },
  title: {
    fr: 'Titre',
    en: 'Title'
  },
  viewQuestion: {
    fr: 'Voir la question',
    en: 'View Question'
  },
  questionEditing: {
    fr: 'Edition de question',
    en: 'Question Editing'
  },
  cancel: {
    fr: 'Annuler',
    en: 'Cancel'
  },
  saveQuestion: {
    fr: 'Sauvegarder la question',
    en: 'Save question'
  },
  seeQuestion: {
    fr: 'Visualisation de question',
    en: 'See question'
  },
  editQuestion: {
    fr: 'Editer la question',
    en: 'Edit question'
  },
  delete: {
    fr: 'Supprimer',
    en: 'Delete'
  }
};

/** Fallback when we do not find any stored question */
const defaultLanguage = 'fr';

export default {
  /** Used to save current language of the application */
  setApplicationLanguage(language) {
    window.localStorage.setItem('language', language);
  },
  /** Used to get current language of the application */
  getApplicationLanguage() {
    const language = window.localStorage.getItem('language');
    return language ? language : defaultLanguage;
  },
  getLocalizedString(key, language) {
    return i18nTranslation[key][language];
  }
};
