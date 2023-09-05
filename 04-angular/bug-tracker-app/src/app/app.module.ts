import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { BugsModule } from './bugs/bugs.module';
import { ProjectsModule } from './projects/projects.module';
import { AppRoutingModule } from './app-router.module';

import { AppComponent } from './app.component';
import { PathNotFoundComponent } from './path-not-found.component';
import { HomeComponent } from './home.component';
import { LoginComponent } from './bugs/auth/login.component';
import { RegistrationComponent } from './bugs/registration/registration.component';

import { RouterModule, Routes } from '@angular/router';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';






@NgModule({
  declarations: [
    AppComponent,
    PathNotFoundComponent,
    HomeComponent,
    LoginComponent,
    RegistrationComponent
  ],
  imports: [
    BrowserModule,
    BugsModule,
    ProjectsModule,
    AppRoutingModule,
    RouterModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule
    
    

  ],
  providers: [
    
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
