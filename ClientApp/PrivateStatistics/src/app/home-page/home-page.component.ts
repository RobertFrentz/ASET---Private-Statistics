import { Component, OnInit } from '@angular/core';
import { Hospital } from 'src/app/Types/hospital';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss'],
})
export class HomePageComponent implements OnInit {
  selectedHospitalsList: Hospital[] = [];

  constructor() {}

  ngOnInit(): void {}

  setCurrentHospitals(hospitals: Hospital[]): void {
    this.selectedHospitalsList = hospitals;
  }
}
