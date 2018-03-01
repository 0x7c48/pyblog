import {browserHistory} from 'react-router';

import * as types   from '../actions/actionTypes';
import initialState from './initialState';


export default function sessionReducer(state = initialState.session, action) {
    console.log("sessionReducer", state, action);
    switch(action.type) {
    case types.LOG_IN_SUCCESS:
        browserHistory.push('/');
        return !!sessionStorage.sessionID;
    case types.LOG_OUT:
        browserHistory.push('/');
        return !!sessionStorage.sessionID;

    default: 
        return state;
    }
}
