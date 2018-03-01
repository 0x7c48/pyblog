import React        from 'react';
import { connect }  from 'react-redux';
import {Redirect}   from 'react-router-dom';
import {APP_LINKS}  from '../routes';


export default function AuthRequired(Component) { 
  class Authenticate extends React.Component {
    render() {
      const {user} = this.props;
      if (user && user.is_authenticated) {
            return <Component {...this.props} />;
        }
      else { 
        return <Redirect to={{
          pathname: APP_LINKS.LOGIN, 
          state: {from: this.props.location}
        }}/>
      }
    }
  }


  function mapStateToProps(state) {
      return {user: state.user ? state.user : {}};
  }

  return connect(mapStateToProps, {})(Authenticate);
}


