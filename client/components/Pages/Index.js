import React, {Component} from 'react';
import {GridTile} from 'material-ui/GridList';
import {connect} from 'react-redux';

import Master from '../Master';
import PostCard from '../Post/PostCard';
import PostGridList from '../Post/PostGridList';

import {store} from '../../store/configureStore';
import {loadPosts}  from '../../actions/postActions';


store.dispatch(loadPosts());


class IndexPage extends Component {
    render() {
        const {
            user,
            posts,
            ownProps,
            ...other
        } = this.props;
        return (
            <Master>
                <PostGridList>
                {posts.map((post) =>
                  <PostCard post={post} key={post.id} />
                 )}
              </PostGridList>
            </Master>
        );
    }
}


function mapStateToProps(state, ownProps) {
    return {
        ownProps: ownProps,
        user: state.user ? state.user : {},
        posts: state.posts ? state.posts : []
    };
}


export default connect(mapStateToProps)(IndexPage);
