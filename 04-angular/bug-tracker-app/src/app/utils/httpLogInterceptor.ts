import { Injectable } from '@angular/core';
import {
    HttpEvent, HttpInterceptor, HttpHandler, HttpRequest
} from '@angular/common/http';

import { Observable } from 'rxjs';

/** Pass untouched request through to the next request handler. */
@Injectable()
export class HttpLogInterceptor implements HttpInterceptor {
    /* when configured (in the module), every http request will go through the intercept function */
    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

            
            // process the request
            console.log(req.url)

            // hand over the request to the next interceptor in the chain for further processing
            return next.handle(req);
    }
}