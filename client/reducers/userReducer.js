import {browserHistory} from 'react-router';

import * as types from '../actions/actionTypes';
import initialState from './initialState';


export default function userReducer(state = initialState.user, action) {
    switch(action.type) {
    case types.LOAD_USER_SUCCESS:
        return action.user;
    case types.LOG_IN_SUCCESS:
    	return action.user;
	case types.LOAD_USER_FAILURE:
        return {};
	case types.LOG_OUT_SUCCESS:
        return {};
	case types.LOG_OUT_FAILURE:
        return action.user;
 
    default: 
        return state;
    }
}
