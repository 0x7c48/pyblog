/* Reducers - how the application's state changes in response. */

import {combineReducers} from 'redux';

// App reducers
import user    from './userReducer';
import posts   from './postReducer';


const rootReducer = combineReducers({
    user,
    posts
});

export default rootReducer;
