import uploadPhoto from './5-photo-reject.js';
import signUpUser from './4-user-promise.js';

export default async function handleProfileSignup(first, last, file) {
  let data = [];
  try {
    const userResponse = await signUpUser(first, last);
    data.push({
        status: 'fulfilled',
        value: userResponse
    })
  } catch(error) {
    data.push({
        status: 'fulfilled',
        value: userResponse
    })
  }

  try {
    const photoResponse = await uploadPhoto(file);
    data.push({
        status: 'fulfilled',
        value: photoResponse
    })
  } catch(error) {
    data.push({
        status: 'rejected',
        value: `Error: ${file} cannot be processed`
    })
  }
  
  return data;
}
