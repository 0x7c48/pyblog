import React, {Component} from 'react';
import {connect}          from 'react-redux';

import MuiThemeProvider   from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme        from 'material-ui/styles/getMuiTheme';
import AppBar             from 'material-ui/AppBar';

import LoginOrUserMenu    from './Menu/Login';
import HeaderMenu         from './Menu/Header';
import SideBar            from './SideBar/SideBar';
import BottomNav          from './Menu/BottomNav';


class Master extends Component {
    // Global state
    state = {
        user:        this.props.user,
        sideBarOpen: false
    };

    // Login handlers

    handleChange = (event, logged) => {
        this.setState({logged: logged});
    };


    // SideBar handlers

    handleTouchTapLeftIconButton = () => {
        this.setState({
            sideBarOpen: !this.state.sideBarOpen
        });
    };

    handleChangeRequestSideBar = (open) => {
        this.setState({
            sideBarOpen: open
        });
    };

    render() {

        return (
            <MuiThemeProvider>
              <div>

                <AppBar
                  title={<HeaderMenu/>}
                  zDepth={0}
                  onLeftIconButtonTouchTap={this.handleTouchTapLeftIconButton}
                  iconElementRight={
                      <LoginOrUserMenu />
                  }
                  />

                <SideBar
                  open={this.state.sideBarOpen}
                  onRequestChangeSideBar={this.handleChangeRequestSideBar}
                  />

                {this.props.children}
                <div>{this.props.user.is_authenticated}</div>

                <br/><br/>
                <BottomNav/>

              </div>
            </MuiThemeProvider>
        );
    }
}


function mapStateToProps(state, ownProps) {
    return {user: state.user ? state.user : {}};
}

export default connect(mapStateToProps)(Master);
