import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { LoginPageFacade } from './login-page-facade.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit{

  loginResponse: boolean = false;
  title: string = "";

  constructor(private loginPageFacade: LoginPageFacade) {}

  ngOnInit(): void {
      this.title = 'Login';
  }

  @Input() error: string | undefined;

  @Output() submitEM = new EventEmitter();

   loginForm: FormGroup = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
  });

  submit() {
    if (this.loginForm.valid) {
      this.getLoginResponse(this.loginForm.value['username'], this.loginForm.value['password']);
    }
  }


   getLoginResponse(username: string, password: string): void{
      this.loginPageFacade.loginPageService.getLoginValidation(username, password).subscribe( response => {
          this.loginResponse = response;
      });
  }

}
