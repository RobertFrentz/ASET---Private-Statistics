import { Component, OnInit } from '@angular/core';
import { StatisticInput } from 'src/app/Models/StatisticInput';

@Component({
  selector: 'app-display-statistics',
  templateUrl: './display-statistics.component.html',
  styleUrls: ['./display-statistics.component.scss'],
})
export class DisplayStatisticsComponent implements OnInit {
  statistics: StatisticInput[] = [
    {
      name: 'Mean',
      value: 25.4,
    },
    {
      name: 'Standard Deviation',
      value: 14,
    },
    {
      name: 'Variance',
      value: 15,
    },
    {
      name: 'Covariance',
      value: 225,
    },
  ];

  constructor() {}

  ngOnInit(): void {}
}
