"use strict";

console.log("main.js");

import {Provider, connect}  from 'react-redux';
import { createStore }      from 'redux';
import createBrowserHistory from 'history/createBrowserHistory';

import React                from 'react';
import {render}             from 'react-dom';
import injectTapEventPlugin from 'react-tap-event-plugin';
import {Router}             from 'react-router';

import configureStore, {store} from './store/configureStore';
import routes                  from './routes';

import {loadUser}           from './actions/userActions';


// Helpers for debugging
window.React = React;
window.Perf = require('react-addons-perf');


// Needed for onTouchTap http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();

// history
const history = createBrowserHistory();


// load data from API
store.dispatch(loadUser());


render(
  <Provider store={store}>
    <Router history={history}>
      {routes}
    </Router>
  </Provider>,
  document.getElementById('app'));
