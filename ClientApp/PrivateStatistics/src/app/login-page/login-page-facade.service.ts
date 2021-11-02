import { Injectable, Injector } from "@angular/core";
import { LoginPageService } from "../services/login-page.service";
import { NumberFormatService } from "../services/number-format.service";

@Injectable({
  providedIn: 'root'
})
export class LoginPageFacade {

  private _loginPageService: LoginPageService | undefined;
  private _numberFormatService: NumberFormatService | undefined;

  constructor( private injector: Injector) {}

  get loginPageService() {
    if(!this._loginPageService){
      this._loginPageService = this.injector.get(LoginPageService);
    }
    return this._loginPageService;
  }

  get numberFormatService() {
    if(!this._numberFormatService){
      this._numberFormatService = this.injector.get(LoginPageService);
    }
    return this._numberFormatService;
  }

}
