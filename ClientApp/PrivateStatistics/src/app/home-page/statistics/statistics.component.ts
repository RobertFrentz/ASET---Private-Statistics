import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-statistics',
  templateUrl: './statistics.component.html',
  styleUrls: ['./statistics.component.scss'],
})
export class StatisticsComponent implements OnInit {
  fieldsList = ['Age', 'BloodType'];
  label = 'Select statistical field';

  constructor() {}

  ngOnInit(): void {}
}
