<template>
  <h1>Admin page</h1>
  <form id="admin-log-form">
    <label for="admin-log-form-password">Mot de passe: </label>
    <input
      id="admin-log-form-password"
      v-model="password"
      type="password"
      class="form-control w-50 my-3"
    />
    <button class="btn btn-outline-primary" type="button" @click="logAdmin">
      Connexion
    </button>
  </form>
</template>

<script>
import QuizApiService from '@/services/QuizApiService';
import participationStorageService from '@/services/ParticipationStorageService';

export default {
  name: 'AdminPage',
  data() {
    return {
      password: ''
    };
  },
  methods: {
    async logAdmin() {
      //on récupère le data sous le nom de token
      //on transmet le mdp sous format d'objet JSON
      try {
        const {
          data: { token }
        } = await QuizApiService.call(
          'post',
          '/login',
          JSON.stringify({ password: this.password })
        );

        //on stocke le token dans le cache
        participationStorageService.saveToken(token);
      } catch (e) {
        alert('Mot de passe incorrect');
      }
    }
  }
};
</script>
