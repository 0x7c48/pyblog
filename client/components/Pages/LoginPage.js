import React                from 'react';
import PropTypes            from 'prop-types';
import {Redirect, withRouter} from 'react-router-dom';
import {bindActionCreators} from 'redux';
import {connect}            from 'react-redux';
import MuiThemeProvider     from 'material-ui/styles/MuiThemeProvider';

import {requestForm}        from '../../api/requests';
import {APP_LINKS}          from '../../routes';
import LoginForm            from '../Form/LoginForm';
import {login}              from '../../actions/userActions';


class LoginPage extends React.Component {
    // for history and user in props
    static propTypes = {
        history:  PropTypes.object.isRequired,
        user:     PropTypes.object.isRequired
    }

    constructor(props) {
        super(props);
        // create local component state user
        this.state = {
            errors: {},
            user: {
                email: '',
                password: ''
            }
        };

        this.processForm = this.processForm.bind(this);
        this.changeUser = this.changeUser.bind(this);
    }

    redirectToIndex(response) {
        const { history } = this.props;
        const {user} = this.props;

        // local this.state.user - data for server
        // user is the global store, dispatched by reduser
        if (user && user.is_authenticated) {
            history.push('/');
        }
    }

    setErrors(err) {
        console.log("qaz", err.response.data.errors);
        this.setState({errors: err.response.data.errors});
    }
    
    processForm(event) {
        event.preventDefault();

        this.props.login(this.state.user).then(
            (res) => this.redirectToIndex(res),
            (err) => this.setErrors(err)
        );
    }

    changeUser(event) {
        const field = event.target.name;
        const user = this.state.user;
        user[field] = event.target.value;

        this.setState({
            user
        });
    }

    render() {
        return (
            <MuiThemeProvider>
              <LoginForm
                onSubmit={this.processForm}
                onChange={this.changeUser}
                errors={this.state.errors}
                user={this.state.user}
                />
            </MuiThemeProvider>
        );
    }

}


function mapStateToProps(state, ownProps) {
    // get user from global store, and pass it into component
    return {ownProps: ownProps, user: state.user ? state.user : {}};
}

export default withRouter(connect(mapStateToProps, { login })(LoginPage));
