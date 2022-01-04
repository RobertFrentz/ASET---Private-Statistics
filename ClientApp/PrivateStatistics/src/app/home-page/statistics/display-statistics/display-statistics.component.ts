import { Component, Input, OnInit } from '@angular/core';
import { StatisticalResult } from 'src/app/Types/statistical-result';

@Component({
  selector: 'app-display-statistics',
  templateUrl: './display-statistics.component.html',
  styleUrls: ['./display-statistics.component.scss'],
})
export class DisplayStatisticsComponent implements OnInit {
  @Input() statistics: StatisticalResult = {
      Mean: 0,
      StandardDeviation: 0,
      Variance: 0,
      StandardError: 0
    };

  constructor() {}

  ngOnInit(): void {
  }
}
