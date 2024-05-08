import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(first, last, file) {
  const signupData = [];
  return Promise.allSettled([uploadPhoto(file), signUpUser(first, last)]).then((results) => {
    results.forEach((result) => {
      let data = {};
      if (result.status === 'fulfilled') {
        data = {
          status: result.status,
          value: result.value,
        };
      } else {
        data = {
          status: result.status,
          value: result.reason,
        };
      }
      signupData.push(data);
    });
  }).catch(() => Error);
}
