/*
  Requests headers wraper for server API.
  All requests with session id.
*/

import getItem, {setItem} from '../auth/cookies';


const GET         = 'GET';
const POST        = 'POST';
const ContentType = 'Content-Type';
const AppJSON     = 'application/json';
const XCSRFToken  =  'csrftoken';


function formatApi(response){
    // Server API response: {"results": data}
    return response.json();
}


export default function request (url, method='GET', headers={}, data={}) {
    console.log("API call ", method, url, getItem("sessionid"));

    headers[ContentType] = AppJSON;
    headers['Cookie'] = "sessionid=" + getItem("sessionid");

    let apiReq = {
        method: method,
        headers: new Headers(headers),
        credentials: "same-origin"
        // same-origin: Send cookies if the URL is on the same origin as the calling script.
        // https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials
    };

    if (method == POST && Object.keys(data).length > 0) {
        apiReq['body'] = JSON.stringify(data);
    };

    const request = new Request(url, apiReq);
    return fetch(request).then(
        response => {
            let resJson = formatApi(response);
            console.log("API resp", resJson);
            return resJson;
        })
        .catch(error => {
            console.log("API error: ", error);
            return error;
        });
}


export function requestForm (data) {
    /* Send JSON POST to Django backend with X-CSRFToken.*/
    let apiReq = {
        body:        JSON.stringify(data),
        method:      'POST',
        headers:     {
            "Content-Type":     AppJSON,
            // "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken":      getItem(XCSRFToken)
        },
        credentials: "same-origin"
        // same-origin: Send cookies if the URL is on the same origin as the calling script.
        // https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials
    };
    
    return apiReq;
};
