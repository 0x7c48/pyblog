import React, {Component}     from 'react';
import {Route, Switch}        from 'react-router';
import {Redirect, withRouter} from 'react-router-dom';
import {connect}              from 'react-redux';
import AuthRequired           from  './auth/requireAuth';

import {
  API_LOGIN_URL, 
  API_LOGOUT_URL,
  API_POSTS_URL,
  API_SIGNUP_URL
} from './api/constApi';

// Master is the base template for pages
import Master from './components/Master';
// All pages here
import IndexPage, {
	IndexPage2
} from './components/Pages/Index';
import SignUpPage from './components/Pages/SignUpPage';
import LoginPage  from './components/Pages/LoginPage';


// App urls
export const APP_LINKS = {
    // Frontend
    INDEX:      "/index/",
    LOGIN:      "/login/",
    SIGNUP:     "/signup/",
    LOGOUT:     "/logout/",
    // Backend urls
    LOGIN_API:  API_LOGIN_URL,
    SIGNUP_API: API_SIGNUP_URL,
    LOGOUT_API: API_LOGOUT_URL,
    POSTS:      API_POSTS_URL,
    POST:       "/api/v1/post/"
}


// Children route
const MainRoute = () => (
  <Switch>
    <Route exact path="/" component={IndexPage} />
    <Route exact path="/base" component={AuthRequired(Master)} />
    <Route exact path="/signup" component={SignUpPage} />
    <Route exact path="/login" component={LoginPage} />
    <Route exact path="/logout" component={IndexPage} />
    <Route exact path="/posts" component={IndexPage} />
    <Route exact path="/post/:slug" component={IndexPage} />
    <Route component={IndexPage}/>
  </Switch>
);


// Patents route
const routes = (
    <Route path='/' component={MainRoute} />
);


export default routes;
