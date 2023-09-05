import { Injectable } from "@angular/core";
import { LoginRequest, LoginResponse, User } from "./auth.model";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn : 'root'
})
export class AuthService {
    private _isLoggedIn : boolean = false;
    private _currentUser!: User;
    private _accessToken : string = '';

    constructor(private httpClient : HttpClient){

    }
    get IsLoggedIn() : boolean {
        return this._isLoggedIn;
    }

    get CurrentUser() : User {
        return this._currentUser;
    }

    get AccessToken() : string {
        return this._accessToken;
    }
    login(emailId: string, password: string) {
        const loginRequest : LoginRequest = {
            email : emailId,
            password : password
        }
        this.httpClient
            .post<LoginResponse>('http://localhost:3000/login', loginRequest)
            .subscribe(res => {
                this._isLoggedIn = true;
                this._currentUser = res.user;
                this._accessToken = res.accessToken;
            })
    }

    logout() {
        this._accessToken = '';
        this._isLoggedIn = false;
        
    }
}