import React, { PropTypes } from 'react';
import { Link } from 'react-router-dom';
import { Card, CardText, CardActions } from 'material-ui/Card';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';


const LoginForm = ({
    onSubmit,
    onChange,
    errors,
    user}) => (
        <div style={{textAlign: "center"}}>        
          <Card>
            <form action="/" onSubmit={onSubmit}>
              <br/><h2>Login</h2>

              {errors.summary && <p className="error-message">{errors.summary}</p>}

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
                <RaisedButton type="submit" label="Log in" primary />
                <br/>
              </CardActions>

              <CardText>Don't have an account? <Link to={'/signup'}>Create one</Link>.</CardText>
              <br/><br/>
            </form>
          </Card>
        </div>
);

export default LoginForm;
