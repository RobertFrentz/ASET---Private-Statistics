import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hospital } from 'src/app/Types/hospital';
import { StatisticalResult } from 'src/app/Types/statistical-result';
import statisticalResultsConfig from 'src/app/Configurations/statistical-results-config.json';
import statisticsHistoryConfig from 'src/app/Configurations/statistics-history-config.json';
import { StatisticsHistory } from 'src/app/Types/statistics-history';
import { HttpClient, HttpParams } from '@angular/common/http';

const statisticsEndpoint = 'http://127.0.0.1:8000/statistics/request';

@Injectable({
  providedIn: 'root',
})
export class StatisticsService {

  constructor(private readonly httpClient: HttpClient) {}

  getStatisticsResults(
    hospitals: Hospital[],
    field: string
  ): Observable<StatisticalResult[]> {
    // let queryParams: HttpParams = new HttpParams();
    // hospitals.forEach(hospital => {
    //     queryParams.append('hospitals', hospital.name);
    // });
    // queryParams.append('field', field);
    // console.log(queryParams);
    const newArray = hospitals.map(hospital => hospital.name);
    return this.httpClient.get<StatisticalResult[]>(statisticsEndpoint, {
      params: { hospitals: newArray, field: field },
    });
    //return of(statisticalResultsConfig);
  }

  getStatisticsHistory(
    hospitals: Hospital[]
  ): Observable<StatisticsHistory[]> {
    return of(statisticsHistoryConfig);
  }
}
