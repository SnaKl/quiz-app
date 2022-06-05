import axios from 'axios';
import { makeAToast } from '../utils/utils';

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      'Content-Type': 'application/json'
    };
    if (token != null) {
      headers.authorization = 'Bearer ' + token;
    }

    const onError = function (error) {
      //TODO : ajouter le makeAToast()
      makeAToast(error.response.data.error);
      return Promise.reject(error.response || error.message);
    };

    return (
      instance({
        method,
        headers: headers,
        url: resource,
        data
      })
        .then(response => {
          return { status: response.status, data: response.data };
        })
        //on modifie la fonction de catch afin de pouvoir transmettre le status de l'erreur
        .catch(onError)
    );
  },
  getQuizInfo() {
    return this.call('get', 'quiz-info');
  }
};
