import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LoginPageService {
  constructor(private readonly httpClient: HttpClient) {}

  getLoginValidation(username: string, password: string): Observable<any> {
    const requestHeaders = new HttpHeaders({});
    const body = {
      username: username,
      password: password,
    };
    return this.httpClient.post('http://localhost:8000/users/login/', body, {
      headers: requestHeaders,
    });
  }
}
