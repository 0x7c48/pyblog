import React, { PropTypes } from 'react';
import { Link } from 'react-router-dom';
import { Card, CardHeader, CardActions, CardText } from 'material-ui/Card';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';

import FlatButton from 'material-ui/FlatButton';


const SignUpForm = ({
    onSubmit,
    onChange,
    errors,
    user}) => (
        <div style={{textAlign: "center"}}>
          <Card>
            <form action="/" onSubmit={onSubmit}>
              <br/><h2>Sign Up</h2>
              
              {errors.summary && <p className="error-message">{errors.summary}</p>}

              <div className="field-line">
                <TextField
                  floatingLabelText="Name"
                  name="name"
                  errorText={errors.name}
                  onChange={onChange}
                  value={user.name}
                  />
              </div>

              <div className="field-line">
                <TextField
                  floatingLabelText="Email"
                  name="email"
                  errorText={errors.email}
                  onChange={onChange}
                  value={user.email}
                  />
              </div>

              <div className="field-line">
                <TextField
                  floatingLabelText="Password"
                  type="password"
                  name="password"
                  onChange={onChange}
                  errorText={errors.password}
                  value={user.password}
                  />
              </div>

              <CardActions>
                <br/>
                  <RaisedButton type="submit" label="SignUp for free" primary />
                <br/>
              </CardActions>

              <CardText>Already have an account? <Link to={'/login'}>Log in</Link></CardText>
              <br/><br/>
            </form>
          </Card>
        </div>
);

export default SignUpForm;
