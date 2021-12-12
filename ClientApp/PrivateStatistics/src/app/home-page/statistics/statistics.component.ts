import {
  Component,
  Input,
  OnChanges,
  OnDestroy,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { first } from 'rxjs/operators';
import { Hospital } from 'src/app/Types/Hospital';
import { StatisticalResult } from 'src/app/Types/StatisticalResult';
import { StatisticsService } from './statistics.service';

@Component({
  selector: 'app-statistics',
  templateUrl: './statistics.component.html',
  styleUrls: ['./statistics.component.scss'],
})
export class StatisticsComponent implements OnInit, OnChanges {
  @Input() selectedHospitals: Hospital[] = [];

  fieldsList: string[] = [];
  statistics: StatisticalResult[] = [];
  label = 'Select statistical field';
  isLoading = false;

  constructor(private readonly statisticsService: StatisticsService) {}

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges): void {
    if (
      changes['selectedHospitals'] &&
      !changes['selectedHospitals'].isFirstChange()
    ) {
      this.fieldsList = changes['selectedHospitals'].currentValue[0].fields;
    }
  }

  computeStatisticalFunctions(field: string): void {
    this.isLoading = true;
    setTimeout( () => {
this.statisticsService
  .getStatisticsResults(this.selectedHospitals, field)
  .pipe(first())
  .subscribe((result) => {
    this.statistics = result;
    this.isLoading = false;
  });
    }, 1000);
    
  }
}
