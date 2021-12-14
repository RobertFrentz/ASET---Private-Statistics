import {
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import { StatisticsHistory } from 'src/app/Types/statistics-history';
import { StatisticsHistoryLine } from 'src/app/Types/statistics-history-line';

@Component({
  selector: 'app-statistics-history',
  templateUrl: './statistics-history.component.html',
  styleUrls: ['./statistics-history.component.scss'],
})
export class StatisticsHistoryComponent implements OnInit, OnChanges {
  @Input() statisticsHistory: StatisticsHistory[] = [];

  displayedColumns: string[] = [
    'id',
    'statisticalField',
    'mean',
    'standardDeviation',
    'variance',
    'covariance',
  ];

  dataSource: StatisticsHistoryLine[] = [];

  constructor() {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['statisticsHistory']) {
      this.assignIdsToLines();
    }
  }

  ngOnInit(): void {}

  assignIdsToLines() {
    let newId = 0;
    this.dataSource = this.statisticsHistory.map((historyLine) => {
      return {
        id: newId++,
        ...historyLine,
      };
    });
  }
}
