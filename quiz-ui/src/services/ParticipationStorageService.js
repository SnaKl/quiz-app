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
  saveToken(token) {
    window.localStorage.setItem('token', token);
  },
  getToken() {
    return window.localStorage.getItem('token');
  }
};
