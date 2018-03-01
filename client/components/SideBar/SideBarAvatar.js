import React from 'react';
import {GridList, GridTile} from 'material-ui/GridList';

import Style from '../Style';


const SideBarAvatar = (props) => (
    <div style={Style.sideBarAvatar.root}>

      <GridList
        cols={1}
        cellHeight={200}
        padding={0}
        style={Style.sideBarAvatar.gridList}
      >

        <GridTile
          titlePosition="bottom"
          titleBackground="linear-gradient(to bottom, rgba(0,0,0,0.7) 0%,rgba(0,0,0,0.3) 70%,rgba(0,0,0,0) 100%)"
          title={props.user.username}
        >
          <img src={props.user.image} />
        </GridTile>

      </GridList>

    </div>
);

export default SideBarAvatar;
