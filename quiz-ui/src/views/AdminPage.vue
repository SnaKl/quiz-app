<!-- Login form for acessing the admin page ! -->
<template>
  <h1 class="my-5"><I18nTextComponent i18n-key="adminPage" /></h1>
  <h2 class="mb-5"><I18nTextComponent i18n-key="connect" /></h2>
  <div class="text-center pt-5">
    <form id="admin-log-form" class="mx-auto w-25 pt-5">
      <div class="form-floating">
        <input
          id="adminPassword"
          type="password"
          class="form-control mb-3"
          placeholder="Mot de passe"
          v-model="password"
        />
        <label for="adminPassword"
          ><I18nTextComponent i18n-key="adminPassword"
        /></label>
      </div>
      <button
        class="btn btn-outline-primary float-end"
        type="button"
        @click="logAdmin"
      >
        <I18nTextComponent i18n-key="connect" />
      </button>
    </form>
  </div>
</template>

<script>
import QuizApiService from '@/services/QuizApiService';
import participationStorageService from '@/services/ParticipationStorageService';
import I18nTextComponent from '@/components/I18nTextComponent.vue';

export default {
  name: 'AdminPage',
  data() {
    return {
      password: ''
    };
  },
  components: { I18nTextComponent },
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
