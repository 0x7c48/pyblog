/* 
   Code for sending and handling requests
   for server API to get session cookie.
*/

import {API_USER_URL} from './constApi';
import request        from './requests';


export default function getUser() {
    return request(API_USER_URL);
}

export function logInUser() {
    return request(API_USER_URL);
}
