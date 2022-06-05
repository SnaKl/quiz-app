<template>
  <h1 class="m-2">Admin page</h1>
  <form id="admin-log-form" class="m-2">
    <div class="form-floating">
      <input
        id="adminPassword"
        type="password"
        class="form-control mb-3"
        placeholder="Mot de passe"
        v-model="password"
      />
      <label for="adminPassword">Mot de passe admin :</label>
    </div>
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
        this.$router.push('/admin/questions');
      } catch (e) {
        //exception gérée dans QuizApiService
      }
    }
  }
};
</script>
