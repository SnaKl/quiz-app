export default {
  clear() {
    // todo : implement
  },
  /** Used to save a playerName in local storage */
  savePlayerName(playerName) {
    window.localStorage.setItem('playerName', playerName);
  },
  /** Used to get a playerName in local storage */
  getPlayerName() {
    return window.localStorage.getItem('playerName');
  },
  /** Used to save a score in local storage */
  saveScore(score) {
    window.localStorage.setItem('participationScore', score);
  },
  /** Used to get a score in local storage */
  getScore() {
    return window.localStorage.getItem('participationScore');
  },
  /** Used to save an admin token in local storage */
  saveToken(token) {
    window.localStorage.setItem('token', token);
  },
  /** Used to get an admin token in local storage */
  getToken() {
    return window.localStorage.getItem('token');
  }
};
