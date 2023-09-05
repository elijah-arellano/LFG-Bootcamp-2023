
import { Injectable } from "@angular/core";
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from "@angular/router";
import { Observable } from "rxjs";
import { AuthService } from "./auth.service";


@Injectable({
    providedIn: 'root'
})
export class LogInGuard implements CanActivate {
    constructor(private router: Router, private authService : AuthService) {

    }
    /* check the conditions to decide whether the route can be activated */
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {

        // check if the user is logged in
        const loggedIn = this.authService.IsLoggedIn;

        if (!loggedIn) {
            
            // redirect the user to the login route
            this.router.navigate(['/login'])
        }
        return loggedIn;
    }

}