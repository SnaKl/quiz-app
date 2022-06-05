/**
 * Create a toast-alert (reused dynamically)
 * @param {string} content
 */
export function makeAToast(content = 'test') {
  const toast = document.getElementById('toast-err-war');

  const toast_body = toast.querySelector('.toast-body');
  toast_body.innerHTML = content;

  const toast_API = new bootstrap.Toast(toast, {
    delay: 2000
  });
  toast_API.show();
}
