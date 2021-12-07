import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-display-charts',
  templateUrl: './display-charts.component.html',
  styleUrls: ['./display-charts.component.scss'],
})
export class DisplayChartsComponent implements OnInit {
  fieldsList = ['Bar'];
  label = 'Select chart type';

  options: any;
  initOpts: any;
  constructor() {}

  ngOnInit(): void {
    this.initOpts = {
      renderer: 'svg',
      width: 800,
      height: 600,
    };

    this.options = {
      color: ['#3398DB'],
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow',
        },
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
      },
      xAxis: [
        {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisTick: {
            alignWithLabel: true,
          },
        },
      ],
      yAxis: [
        {
          type: 'value',
        },
      ],
      series: [
        {
          name: 'Counters',
          type: 'bar',
          barWidth: '60%',
          data: [10, 52, 200, 334, 390, 330, 220],
        },
      ],
    };
  }
}
