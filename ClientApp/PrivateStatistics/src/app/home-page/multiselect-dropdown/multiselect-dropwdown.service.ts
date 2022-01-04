import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Hospital } from 'src/app/Types/hospital';

const hospitalEndpoint = 'http://localhost:8000/hospitals';

@Injectable({
  providedIn: 'root',
})
export class MultiSelectDropdownService {

  constructor(private readonly httpClient: HttpClient) {}

  getHospitals(): Observable<Hospital[]> {
    return this.httpClient.get<Hospital[]>(hospitalEndpoint);
  }
}
