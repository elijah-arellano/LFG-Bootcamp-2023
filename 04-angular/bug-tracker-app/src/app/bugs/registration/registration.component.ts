import { Component } from "@angular/core";
import { FormControl, FormGroup, Validators } from "@angular/forms";
import { RegistrationService } from "../services/bugRegister.service";

@Component({
    selector: 'app-registration',
    templateUrl: 'registration.component.html',
    styleUrls: ['registration.component.css']
})

export class RegistrationComponent{

    constructor(private registrationService: RegistrationService){}


    registrationForm= new FormGroup({
        emailId: new FormControl('', [
            Validators.required, 
            Validators.email
        ]),
        firstName: new FormControl('', [
            Validators.required
        ]),
        lastName: new FormControl('', [
            Validators.required
        ]),
        phone: new FormControl('', [
            Validators.required
        ]),
        password: new FormControl('', [
            Validators.required
        ]),
        confirmPassword: new FormControl('', [
            Validators.required
        ]),
    })

    get emailId(){
        return this.registrationForm.get('emailId')
    }

    get firstName(){
        return this.registrationForm.get('firstName')
    }

    get lastName(){
        return this.registrationForm.get('lastName')
    }

    get phone(){
        return this.registrationForm.get('phone')
    }

    get password(){
        return this.registrationForm.get('password')
    }

    get confirmPassword(){
        return this.registrationForm.get('confirmPassword')
    }

    onBtnRegisterClick(){
        if(this.registrationForm.valid){
            const registrationData = {
                emailId: this.registrationForm.value.emailId,
                firstName: this.registrationForm.value.firstName,
                lastName: this.registrationForm.value.lastName,
                phone: this.registrationForm.value.phone,
                password: this.registrationForm.value.password,
            }

            this.registrationService.registerUser(registrationData).subscribe(
                () => {}
            )
            
        }
    }

    }


