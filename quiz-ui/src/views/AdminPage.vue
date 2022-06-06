<!-- Login form for acessing the admin page ! -->
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
      //We directly get token from the data
      try {
        const {
          data: { token }
        } = await QuizApiService.call(
          'post',
          '/login',
          //We transmit Object to JSON DATA
          JSON.stringify({ password: this.password })
        );

        //We store the token in localStorage
        participationStorageService.saveToken(token);
        this.$router.push('/admin/questions');
      } catch (e) {
        //Exception handled in a higher level (QuizApiService who will print an error toast)
      }
    }
  }
};
</script>
