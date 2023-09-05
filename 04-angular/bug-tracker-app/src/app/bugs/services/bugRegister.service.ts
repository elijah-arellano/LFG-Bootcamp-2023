import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class RegistrationService{
    private registrationEndpoint = 'http://localhost:3000/register';

    constructor(private httpClient: HttpClient){

    }

    registerUser(userData: any): Observable<any>{
        return this.httpClient.post(this.registrationEndpoint, userData)
    }
 }