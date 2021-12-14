import { Component, Input, OnInit } from '@angular/core';
import { StatisticalResult } from 'src/app/Types/statistical-result';

@Component({
  selector: 'app-display-statistics',
  templateUrl: './display-statistics.component.html',
  styleUrls: ['./display-statistics.component.scss'],
})
export class DisplayStatisticsComponent implements OnInit {
  @Input() statistics: StatisticalResult = {
    mean: 10,
    standardDeviation: 20,
    variance: 30,
    standardError: 40,
  };

  constructor() {}

  ngOnInit(): void {}
}
