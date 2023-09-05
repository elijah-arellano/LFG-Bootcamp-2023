import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { HomeComponent } from "./home.component";
import { PathNotFoundComponent } from "./path-not-found.component";
import { HTTP_INTERCEPTORS } from "@angular/common/http";
import { HttpLogInterceptor } from "./utils/httpLogInterceptor";
import { HttpAuthorizeInterceptor } from "./utils/httpAuthorizeInterceptor";
import { LoginComponent } from "./bugs/auth/login.component";
import { RegistrationComponent } from "./bugs/registration/registration.component";
import { BugsComponent } from "./bugs/bugs.component";
import { LogInGuard } from "./bugs/auth/login-guard";
import { ProjectsComponent } from "./projects/projects.component";

/* define the routes */
const routes : Routes = [
    { path: "", component: HomeComponent },
    { path : "login", component : LoginComponent},
    { path : "register", component : RegistrationComponent},
    { path: "bugs", component: BugsComponent, canActivate: [LogInGuard] },
    { path: "projects", component: ProjectsComponent, canActivate: [LogInGuard] },
    /* { path: "**", component: PathNotFoundCompnent } */
    {path : "**", redirectTo : ""}
  ]
  
  export const httpInterceptorProviders = [
    { provide: HTTP_INTERCEPTORS, useClass: HttpLogInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: HttpAuthorizeInterceptor, multi: true },
  ];

@NgModule({
    imports: [
        RouterModule.forRoot(routes)
    ],
    exports: [RouterModule]
})
export class AppRoutingModule {

}