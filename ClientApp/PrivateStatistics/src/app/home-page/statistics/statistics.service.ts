import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hospital } from 'src/app/Types/Hospital';
import { StatisticalResult } from 'src/app/Types/StatisticalResult';
import statisticalResultsConfig from 'src/app/Configurations/statistical-results-config.json';

@Injectable({
  providedIn: 'root',
})
export class StatisticsService {
  getStatisticsResults(
    hospitals: Hospital[],
    field: string
  ): Observable<StatisticalResult[]> {
    return of(statisticalResultsConfig);
  }
}
