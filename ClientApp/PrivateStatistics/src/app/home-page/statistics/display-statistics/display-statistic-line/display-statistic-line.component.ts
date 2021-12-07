import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-display-statistic-line',
  templateUrl: './display-statistic-line.component.html',
  styleUrls: ['./display-statistic-line.component.scss']
})
export class DisplayStatisticLineComponent implements OnInit {

  @Input() statisticName: string = "default";
  @Input() statisticValue: number = 0;

  constructor() { }

  ngOnInit(): void {
  }

}
