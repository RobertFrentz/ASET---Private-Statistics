import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hospital } from 'src/app/Types/hospital';
import { StatisticalResult } from 'src/app/Types/statistical-result';
import statisticsHistoryConfig from 'src/app/Configurations/statistics-history-config.json';
import { StatisticsHistory } from 'src/app/Types/statistics-history';
import { HttpClient } from '@angular/common/http';

const statisticsEndpoint = 'http://localhost:8000/statistics/request';

@Injectable({
  providedIn: 'root',
})
export class StatisticsService {
  constructor(private readonly httpClient: HttpClient) {}

  getStatisticsResults(
    hospitals: Hospital[],
    field: string
  ): Observable<StatisticalResult> {
    const newArray = hospitals.map((hospital) => hospital.name);
    return this.httpClient.get<StatisticalResult>(statisticsEndpoint, {
      params: { hospitals: newArray, field: field },
    });
  }

  getStatisticsHistory(hospitals: Hospital[]): Observable<StatisticsHistory[]> {
    return of(statisticsHistoryConfig);
  }
}
