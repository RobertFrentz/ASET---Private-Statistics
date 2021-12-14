import {
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { first } from 'rxjs/operators';
import { Hospital } from 'src/app/Types/hospital';
import { StatisticalResult } from 'src/app/Types/statistical-result';
import { StatisticsHistory } from 'src/app/Types/statistics-history';
import { StatisticsService } from './statistics.service';

@Component({
  selector: 'app-statistics',
  templateUrl: './statistics.component.html',
  styleUrls: ['./statistics.component.scss'],
})
export class StatisticsComponent implements OnInit, OnChanges {
  @Input() selectedHospitals: Hospital[] = [];

  fieldsList: string[] = [];
  statistics: StatisticalResult = {
    mean: 10,
    standardDeviation: 20,
    variance: 30,
    standardError: 40,
  };
  statisticsHistory: StatisticsHistory[] = [];
  label = 'Select statistical field';
  isLoadingStatistics = false;
  isLoadingHistory = false;

  constructor(private readonly statisticsService: StatisticsService) {}

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges): void {
    if (
      changes['selectedHospitals'] &&
      !changes['selectedHospitals'].isFirstChange()
    ) {
      this.fieldsList = changes['selectedHospitals'].currentValue[0].fields;
      this.getStatisticsHistory();
    }
  }

  computeStatisticalFunctions(field: string): void {
    this.isLoadingStatistics = true;
    this.statisticsService
      .getStatisticsResults(this.selectedHospitals, field)
      .pipe(first())
      .subscribe((statistics) => {
        this.statistics = statistics;
        this.isLoadingStatistics = false;
      });
  }

  getStatisticsHistory(): void {
    this.isLoadingHistory = true;
    setTimeout(() => {
      this.statisticsService
        .getStatisticsHistory(this.selectedHospitals)
        .pipe(first())
        .subscribe((history) => {
          this.statisticsHistory = history;
          this.isLoadingHistory = false;
        });
    }, 2000);
  }
}
