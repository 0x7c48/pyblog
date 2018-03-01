/*
  Const for server API
  All URL must end with trelling slash `/` in order 
  to avoid 302 redirect.
*/

const ENDPOINT = '/api',
      VER      = '/v1',
      BASE     = ENDPOINT + VER;

export const API_SIGNUP_URL = "/accounts/signup/";
export const API_LOGIN_URL  = BASE + '/login/';
export const API_LOGOUT_URL = BASE + '/logout/';
export const API_USER_URL   = BASE + '/users/';
export const API_POSTS_URL  = BASE + '/posts/';
