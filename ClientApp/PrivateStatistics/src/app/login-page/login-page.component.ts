import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginPageFacade } from './login-page-facade.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss'],
})
export class LoginPageComponent implements OnInit {
  loginResponse: boolean = false;
  maxInputSize = 25;
  readOnlyUsername = false;
  readOnlyPassword = false;
  title: string = '';

  constructor(
    private readonly loginPageFacade: LoginPageFacade,
    private readonly router: Router
  ) {}

  ngOnInit(): void {
    this.title = 'Login';
    this.onChangingState();
  }

  @Input() error: string | undefined;

  @Output() submitEM = new EventEmitter();

  loginForm: FormGroup = new FormGroup({
    username: new FormControl('', [
      Validators.required,
      Validators.maxLength(this.maxInputSize - 1),
    ]),
    password: new FormControl('', [
      Validators.required,
      Validators.maxLength(this.maxInputSize - 1),
    ]),
  });

  submit() {
    if (this.loginForm.valid) {
      this.getLoginResponse(
        this.loginForm.value['username'],
        this.loginForm.value['password']
      );
    }
  }

  getLoginResponse(username: string, password: string): void {
    this.loginPageFacade.loginPageService
      .getLoginValidation(username, password)
      .subscribe((response) => {
        if (Object.keys(response).length === 0) {
          this.router.navigate(['/home']);
        }
      });
  }

  get username() {
    return this.loginForm.controls.username;
  }

  get password() {
    return this.loginForm.controls.password;
  }
  private onChangingState(): void {
    this.loginForm.controls.username.valueChanges.subscribe((val) => {
      if (val.length >= this.maxInputSize) {
        console.log('Maxim username size reached');
      }
    });
    this.loginForm.controls.password.valueChanges.subscribe((val) => {
      if (val.length >= this.maxInputSize) {
        console.log('Maxim password size reached');
      }
    });
  }
}
