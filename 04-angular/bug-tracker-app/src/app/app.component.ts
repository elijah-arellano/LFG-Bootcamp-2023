import { Component } from '@angular/core';
import { AuthService } from './bugs/auth/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'bug-tracker-app';

  constructor(public authService: AuthService) {
    
  }
  onBtnLogoutClick() {
    this.authService.logout()
  }
}
