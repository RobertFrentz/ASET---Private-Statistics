import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { LoginPageFacade } from './login-page-facade.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent{

  loginResponse: boolean | undefined;

  constructor(
    private loginPageFacade: LoginPageFacade
    ) {}

  @Input() error: string | undefined;

  @Output() submitEM = new EventEmitter();

   loginForm: FormGroup = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
  });

  submit() {
    if (this.loginForm.valid) {
      this.loginPageFacade.loginPageService.getLoginValidation('Costel', 'Mirel').subscribe( response => {
          this.loginResponse = response;
      })
    }
  }

}
