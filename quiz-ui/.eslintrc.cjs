/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
  root: true,
  plugins: ['prettier'],
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/eslint-config-prettier'
  ],
  env: {
    'vue/setup-compiler-macros': true
  },
  rules: {
    'comma-dangle': ['error', 'never'],
    'no-console': ['error', { allow: ['warn'] }],
    quotes: ['error', 'single', { avoidEscape: true }]
  },
  globals: {
    bootstrap: 'readonly'
  }
};
