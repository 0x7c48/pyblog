import * as types from './actionTypes';
import getPosts   from '../api/PostApi';


export function loadPostSuccess(posts) {
    return {type: types.LOAD_POSTS_SUCCESS, posts};
}

export function loadPosts() {
    return function(dispatch) {
        return getPosts().then(posts => {
            dispatch(loadPostSuccess(posts));
        }).catch(error => {
            throw(error);
        });
    };
}
