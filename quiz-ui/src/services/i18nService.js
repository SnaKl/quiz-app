/** Dictionary with all the string of the application */
const i18nTranslation = {
  aboutPage: {
    fr: 'À propos',
    en: 'About'
  },
  aboutContent: {
    fr: "Quiz-App est une application développée par une équipe de trois étudiants jeunes et dynamiques. Passionés par l'informatique et plus particulièrement le développement web. En effet, ces trois têtes brûlées sont très friandes du PHP natif.",
    en: 'Quiz-App is an application developed by a team of three young and dynamic students. Passionated about IT et more specifically web development. Indeed, these three hotheaded students are fond of native PHP.'
  },
  aboutTeamTitle: {
    fr: "L'équipe",
    en: 'The team'
  },
  aboutContactTitle: {
    fr: 'Demande de contact',
    en: 'Contact request'
  },
  aboutContact: {
    fr: "Nous n'acceptons malheureusement aucune demande de contact, merci de votre compréhension.",
    en: 'We sadly do not accept contact requests, thank you for your comprehension.'
  },
  welcome: {
    fr: 'Bienvenue sur Quiz-App',
    en: 'Welcome on Quiz-App'
  },
  welcomeMsg: {
    fr: 'Testez vos connaissances sur la culture informatique !',
    en: 'Have a go on your IT knowledge !'
  },
  homePage: {
    fr: 'Accueil',
    en: 'Homepage'
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
    fr: 'Nouveau quiz',
    en: 'New quiz'
  },
  enterYourName: {
    fr: 'Saisissez votre nom',
    en: 'Enter your name'
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
    fr: ' À propos',
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
    fr: 'Mot de passe admin',
    en: 'Admin password'
  },
  connect: {
    fr: 'Connexion',
    en: 'Login'
  },
  error: {
    fr: 'Erreur',
    en: 'Error'
  },
  questionList: {
    fr: 'Liste des questions',
    en: 'Question list'
  },
  addQuestion: {
    fr: ' Ajouter une question',
    en: ' Add question'
  },
  title: {
    fr: 'Titre',
    en: 'Title'
  },
  viewQuestion: {
    fr: 'Voir la question',
    en: 'View question'
  },
  questionEditing: {
    fr: 'Edition de question',
    en: 'Question editing'
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
    fr: 'Vue de question',
    en: 'Question display'
  },
  editQuestion: {
    fr: ' Éditer la question',
    en: ' Edit question'
  },
  delete: {
    fr: ' Supprimer',
    en: ' Delete'
  },
  loading: {
    fr: 'Chargement ...',
    en: 'Loading ...'
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
