<!-- Utility Component printing the i18n text string associated to a key -->
<script>
import i18nService from '../services/i18nService';

export default {
  name: 'I18nTextComponent',
  props: {
    i18nKey: {
      type: String
    }
  },
  data() {
    return {
      // We pass with a getter to keep track of localStorage
      get language() {
        return i18nService.getApplicationLanguage();
      }
    };
  },
  methods: {
    getString() {
      return i18nService.getLocalizedString(this.i18nKey, this.language);
    }
  }
};
</script>

<template>{{ getString() }}</template>

<style></style>
