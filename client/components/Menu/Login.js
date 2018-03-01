import React, {Component}         from 'react';
import {connect}                  from 'react-redux';
import muiThemeable               from 'material-ui/styles/muiThemeable';

import Dialog                     from 'material-ui/Dialog';
import IconMenu                   from 'material-ui/IconMenu';
import MenuItem                   from 'material-ui/MenuItem';
import TextField                  from 'material-ui/TextField';

import IconButton                 from 'material-ui/IconButton';
import FlatButton                 from 'material-ui/FlatButton';
import Divider                    from 'material-ui/Divider';
import FontIcon                   from 'material-ui/FontIcon';

import SocialPerson               from 'material-ui/svg-icons/social/person';
import ActionSettingsApplications from 'material-ui/svg-icons/action/settings-applications';
import ActionHelpOutline          from 'material-ui/svg-icons/action/help-outline';
import ActionExitToApp            from 'material-ui/svg-icons/action/exit-to-app';

import Style                      from '../Style';
import {APP_LINKS}                from '../../routes';


export class Login extends Component {
    static muiName = 'FlatButton';

    constructor(props) {
        super(props);
    }

    state = {
        open: true
    };

    handleOpen = () => {
        this.setState({open: true});
    };

    handleClose = () => {
        this.setState({open: false});
    };

    render() {
        const {user, ownProps, muiTheme, ...other} = this.props;
        let flatStyle = {color: muiTheme.appBar.textColor, marginTop: (muiTheme.button.iconButtonSize - 36) / 2 + 1};
        return (
            <FlatButton
              style={flatStyle}
              label="Login"
              href={APP_LINKS.LOGIN}
              />
        );
    };
}


export class Logged extends Component {
    static muiName = 'IconMenu';

    constructor(props) {
        super(props);
        this.state = {
            valueSingle: '1'
        };
    }

    handleChangeSingle = (event, value) => {
        this.setState({
            valueSingle: value
        });
    };

    render() {
        const {user, ownProps, muiTheme, ...other} = this.props;
        let iconStyle = {fill: muiTheme.appBar.textColor, color: muiTheme.appBar.textColor};
        return (
            <IconMenu
              iconButtonElement={
                      <IconButton iconStyle={iconStyle}
                            tooltip={user.username}
                            tooltipPosition="bottom-left">
                            <SocialPerson />
                          </IconButton>
                      }
                      onChange={this.handleChangeSingle}
                      value={this.state.valueSingle}
                      targetOrigin={{horizontal: 'right', vertical: 'top'}}
                      anchorOrigin={{horizontal: 'right', vertical: 'top'}}
                      >
              <MenuItem value="1" primaryText="Settings" leftIcon={<ActionSettingsApplications/>} />
              <Divider />
              <MenuItem value="2" primaryText="Help" leftIcon={<ActionHelpOutline/>} />
              <Divider />
              <MenuItem href={APP_LINKS.LOGOUT_API} value="3" primaryText="Sign out" leftIcon={<ActionExitToApp/>} />
            </IconMenu>
        );
    };
}


class LoginOrUserMenu extends Component {
   static muiName = 'IconMenu';

    render() {
        const {user} = this.props;
        console.log("this.props", this.props);
        if (user && user.is_authenticated) {
            return <Logged {...this.props} />;
        }
        else {
            return <Login {...this.props} />;
        }
    };
};


function mapStateToProps(state, ownProps) {
    return {ownProps: ownProps, user: state.user ? state.user : {}};
}


export default connect(mapStateToProps)(muiThemeable()(LoginOrUserMenu));
