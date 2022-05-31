export default {
  clear() {
    // todo : implement
  },
  savePlayerName(playerName) {
    window.localStorage.setItem('playerName', playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem('playerName');
  },
  saveScore(score) {
    window.localStorage.setItem('participationScore', score);
  },
  getScore() {
    return window.localStorage.getItem('participationScore');
  },
  saveToken(token) {
    window.localStorage.setItem('token', token);
  },
  getToken() {
    return window.localStorage.getItem('token');
  }
};
