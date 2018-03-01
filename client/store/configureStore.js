/* Store for different state */

import {createStore, applyMiddleware, compose} from 'redux';
import rootReducer from '../reducers'
import thunk from 'redux-thunk';

// https://github.com/zalmoxisus/redux-devtools-extension#12-advanced-store-setup
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export default function configureStore() {
  return createStore(
    rootReducer,
      composeEnhancers(applyMiddleware(thunk))
  );
}

export const store = configureStore();
