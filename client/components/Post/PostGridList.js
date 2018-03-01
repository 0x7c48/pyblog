import React from 'react';

import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import Subheader from 'material-ui/Subheader';
import StarBorder from 'material-ui/svg-icons/toggle/star-border';


const styles = {
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  }
};


const PostGridList = (props) => (
  <div style={styles.root}>
    <GridList cellHeight='auto'>
      <Subheader>All posts</Subheader>
      {props.children}
    </GridList>
  </div>
);


export default PostGridList;
