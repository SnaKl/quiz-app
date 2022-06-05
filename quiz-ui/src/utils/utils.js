export function makeAToast(content = 'test') {
  const toast = document.getElementById('toast-err-war');

  const toast_body = toast.querySelector('.toast-body');
  toast_body.innerHTML = content;

  const toast_API = new bootstrap.Toast(toast, {});
  toast_API.show();
}
