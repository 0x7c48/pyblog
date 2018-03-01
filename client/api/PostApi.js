/* 
Get post data from server API.
*/

import {API_POSTS_URL} from './constApi';
import request         from './requests';


export default function getPosts() {
    return request(API_POSTS_URL);
}
