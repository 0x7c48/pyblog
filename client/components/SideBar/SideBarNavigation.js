import merge from 'lodash.merge';

import React from 'react';
import {NavLink} from 'react-router-dom';

import MenuItem from 'material-ui/MenuItem';
import {List, ListItem, makeSelectable} from 'material-ui/List';

import muiThemeable from 'material-ui/styles/muiThemeable';

import Style from '../Style';


const Link = (to, title, props) => (
    <NavLink exact
             activeStyle={Style.header.activeLink}
             style={merge(props.muiTheme.menuItem, Style.nemuItem)}
             to={to}>
      {title}
    </NavLink>
);


const Link_ = (to, title, props) => {
    return (<a
             href={to}
             target="_blank"
             style={merge(props.muiTheme.menuItem, Style.nemuItem)}>
            {title}
            </a>)
}


const SelectableList = makeSelectable(List);

const SideBarNavigation = (props) => (
    <SelectableList value={location.pathname}>
      <ListItem primaryText={Link("/", "Blog", props)} />
      <ListItem primaryText={Link("/base", "Base", props)} />
      <ListItem primaryText={Link_("https://github.com", "Github", props)} />
        <ListItem primaryText={Link("/cv", "CV", props)} />
        <ListItem primaryText={Link_("/blogadmin/", "Blog admin", props)} />
      <ListItem
        primaryText="Nested items"
        primaryTogglesNestedList={true}
        nestedItems={[
          <ListItem primaryText={Link("/user/posts", "My Posts", props)} />
        ]}
       />
    </SelectableList>
);

export default muiThemeable()(SideBarNavigation);
