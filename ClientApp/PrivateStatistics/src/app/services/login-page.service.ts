import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginPageService {

  constructor() { }

  getLoginValidation(username: string, password: string) : Observable<boolean>{
      return of(true);
  }
}
