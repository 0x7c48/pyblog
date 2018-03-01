import axios from 'axios';
import getItem from '../auth/cookies';

import * as types from './actionTypes';
import getUser    from '../api/UserApi';
import {APP_LINKS} from '../routes';


axios.defaults.headers.common['X-CSRFToken'] = getItem('csrftoken');
axios.defaults.headers.post['Content-Type'] = 'application/json';


export function loadUserSuccess(user) {
    return {type: types.LOAD_USER_SUCCESS, user};
}

export function loginUserSuccess(user) {
    return {type: types.LOG_IN_SUCCESS, user};
}

export function loadUser() {
    return function(dispatch) {
        return getUser().then(response => {
            dispatch(loadUserSuccess(response));
        }).catch(error => {
            throw(error);
        });
    };
}


// function do not return value,
// only dispatch and mutate global store.user
export function login(data) {
    return dispatch => {
        return axios.post(APP_LINKS.LOGIN_API, data).then(
            response => {
                const user = response.data;
                dispatch(loginUserSuccess(user));
        });
    }
}
