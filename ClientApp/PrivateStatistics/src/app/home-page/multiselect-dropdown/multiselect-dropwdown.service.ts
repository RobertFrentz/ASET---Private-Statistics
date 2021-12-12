import { Injectable } from "@angular/core";
import { Observable, of } from "rxjs";
import { Hospital } from "src/app/Types/Hospital";
import HttpResponse from "../../Configurations/hospital-response-config.json";

@Injectable({
  providedIn: 'root'
})
export class MultiSelectDropdownService {

  getHospitals(): Observable<Hospital[]> {
    return of(HttpResponse);
  }

}