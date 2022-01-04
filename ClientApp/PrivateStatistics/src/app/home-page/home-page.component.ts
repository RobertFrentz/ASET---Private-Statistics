import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Hospital } from 'src/app/Types/hospital';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss'],
})
export class HomePageComponent implements OnInit {
  selectedHospitalsList: Hospital[] = [];
  username: String | null = 'user';

  constructor(private readonly activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
    this.username = this.activatedRoute.snapshot.queryParamMap.get('username');
    this.username = this.username;
  }

  setCurrentHospitals(hospitals: Hospital[]): void {
    this.selectedHospitalsList = hospitals;
  }
}
