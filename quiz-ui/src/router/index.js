import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionsManager from '../views/QuestionsManager.vue';
import AdminPage from '../views/AdminPage.vue';
import AdminPageQuestions from '../views/AdminPageQuestions.vue';
import AdminPageQuestionEdition from '../views/AdminPageQuestionEdition.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page',
      name: 'NewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'QuestionManager',
      component: QuestionsManager
    },
    {
      path: '/admin',
      name: 'AdminPage',
      component: AdminPage
    },
    {
      path: '/admin/questions',
      name: 'AdminPageQuestions',
      component: AdminPageQuestions
    },
    {
      path: '/admin/questions/add',
      name: 'AdminPageQuestionEdition',
      component: AdminPageQuestionEdition
    },
    {
      path: '/admin/questions/:pos',
      name: 'AdminPageQuestionEdition',
      component: AdminPageQuestionEdition
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/score',
      name: 'score',
      component: () => import('../views/ScoreView.vue')
    }
  ]
});

export default router;
