import React from 'react';
import {Link} from 'react-router-dom';
import {connect} from 'react-redux';

import AppBar from 'material-ui/AppBar';
import Drawer from 'material-ui/Drawer';
import MenuItem from 'material-ui/MenuItem';
import {List, ListItem} from 'material-ui/List';

import SideBarAvatar from './SideBarAvatar';
import SideBarNavigation from './SideBarNavigation';
import Style from '../Style';


class SideBar extends React.Component {

    render() {
        // props from perent component
        const {
            onRequestChangeSideBar,
            open,
            user,
            ownProps,
            ...other
        } = this.props;

        return (
            <Drawer
              docked={false}
              width={Style.drawler.width}
              open={open}
              onRequestChange={onRequestChangeSideBar}
              >
              <SideBarAvatar user={user}/>
              <SideBarNavigation/>
            </Drawer>
        );
    }
}

function mapStateToProps(state, ownProps) {
    return {ownProps: ownProps, user: state.user ? state.user : {}};
}


export default connect(mapStateToProps)(SideBar);
