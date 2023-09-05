import { Injectable } from '@angular/core';
import {
    HttpEvent, HttpInterceptor, HttpHandler, HttpRequest
} from '@angular/common/http';

import { Observable } from 'rxjs';
import { AuthService } from '../bugs/auth/auth.service';

/** Pass untouched request through to the next request handler. */
@Injectable()
export class HttpAuthorizeInterceptor implements HttpInterceptor {

    constructor(private authService : AuthService){

    }
    /* when configured (in the module), every http request will go through the intercept function */
    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

        // No need to add the access token for the login request
        if (req.url.includes("/login")){
            return next.handle(req);    
        }
        // process the request
        const accessToken = this.authService.AccessToken
        

        // setting the authorization header to be associated with all the http requests
        req = req.clone({
            setHeaders: {
                Authorization: "Bearer " + accessToken
            }
        });

        // hand over the request to the next interceptor in the chain for further processing
        return next.handle(req);
    }
}