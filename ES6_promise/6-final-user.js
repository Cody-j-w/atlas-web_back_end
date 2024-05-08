import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(first, last, file) {
  return Promise.allSettled([uploadPhoto(file), signUpUser(first, last)]).then((results) => {
    const data = [];
    results.forEach((result) => {
      if (result.status === 'fulfilled') {
        data.push({
          status: result.status,
          value: result.value,
        });
      } else {
        data.push({
          status: result.status,
          value: `Error: ${file} cannot be processed`,
        });
      }
    });
    console.log(data);
    return data;
  });
}
