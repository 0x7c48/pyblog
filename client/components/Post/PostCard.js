import React, {Component} from 'react';

import {
    Card, CardActions, CardHeader,
    CardMedia, CardTitle, CardText
} from 'material-ui/Card';

import FlatButton from 'material-ui/FlatButton';


const PostCard = (props) => (
    <Card>
      <CardHeader
        title={props.post.title}
        subtitle={props.post.user.username}
        avatar="/static/images/avatar.png"
        />
      <CardMedia
        overlay={<CardTitle title="Python Dzen" subtitle="Python" />}
        >
        <img height="300" src="/static/images/avatar.png" alt="" />
      </CardMedia>
      <CardTitle title="Card title" subtitle="04.07.2017" />
      <CardText>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
        Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
        Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.      
      </CardText>

      <CardText>
        Keyword: Python, pip
      </CardText>

      <CardActions>
        <FlatButton style={{textAlign: 'center'}} label="Read more" />
      </CardActions>
      
      <p style={{textAlign: 'center'}}>~~~~~~~~~~~~</p>
      <br/>
    </Card>
);


export default PostCard;
