import merge from 'lodash.merge';

import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

import muiThemeable from 'material-ui/styles/muiThemeable';

import Style from '../Style';


const Link = (to, title, props) => (
    <NavLink exact
             activeStyle={Style.header.activeLink}
             style={merge(props.muiTheme.tabs, Style.header.link)}
             to={to}>
      {title}
    </NavLink>
);


const HeaderMenu = (props) => (
    <div>
      <span style={Style.header.span}>{Link("/", "Blog", props)}</span>
      <span style={Style.header.span}>{Link("/base", "Base", props)}</span>
    </div>
);

export default muiThemeable()(HeaderMenu);
