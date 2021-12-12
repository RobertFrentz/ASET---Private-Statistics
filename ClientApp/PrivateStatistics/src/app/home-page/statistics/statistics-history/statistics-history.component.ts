import { Component, OnInit } from '@angular/core';

export interface StatisticDataRow {
  id: number;
  statisticalField: string;
  mean: number;
  standardDeviation: number;
  variance: number;
  covariance: number;
}

const ELEMENT_DATA: StatisticDataRow[] = [
  {
    id: 1,
    statisticalField: 'Age',
    mean: 1.0079,
    standardDeviation: 30,
    variance: 15,
    covariance: 2551,
  },
  {
    id: 2,
    statisticalField: 'Age',
    mean: 2.0079,
    standardDeviation: 25,
    variance: 55,
    covariance: 2553,
  },
  {
    id: 3,
    statisticalField: 'Blood Type',
    mean: 3.0079,
    standardDeviation: 35,
    variance: 35,
    covariance: 2552,
  },
  {
    id: 4,
    statisticalField: 'Age',
    mean: 4.0079,
    standardDeviation: 40,
    variance: 25,
    covariance: 2554,
  },
  {
    id: 5,
    statisticalField: 'Blood Type',
    mean: 5.0079,
    standardDeviation: 45,
    variance: 3,
    covariance: 2550,
  },
];

@Component({
  selector: 'app-statistics-history',
  templateUrl: './statistics-history.component.html',
  styleUrls: ['./statistics-history.component.scss'],
})
export class StatisticsHistoryComponent implements OnInit {
  displayedColumns: string[] = [
    'id',
    'statisticalField',
    'mean',
    'standardDeviation',
    'variance',
    'covariance',
  ];
  dataSource = ELEMENT_DATA;

  constructor() {}

  ngOnInit(): void {}
}
