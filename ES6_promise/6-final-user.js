import uploadPhoto from './5-photo-reject.js';
import signUpUser from './4-user-promise.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([uploadPhoto(fileName), signUpUser(firstName, lastName)]).then(() => {
  }).catch(() => Error);
}
