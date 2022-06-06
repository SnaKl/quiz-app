import axios from 'axios';
import { makeAToast } from '../utils/utils';

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  /** Principal method of the Service, call the back end with the selected parameters */
  async call(method, resource, data = null, token = null) {
    var headers = {
      'Content-Type': 'application/json'
    };
    if (token != null) {
      headers.authorization = 'Bearer ' + token;
    }

    const onError = function (error) {
      /** Since in the backend, on each error, we got a message in the "error" field, we print it using a toast in the app for the feedback */
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
        //Modified error function to get error status
        .catch(onError)
    );
  },
  getQuizInfo() {
    return this.call('get', 'quiz-info');
  }
};
