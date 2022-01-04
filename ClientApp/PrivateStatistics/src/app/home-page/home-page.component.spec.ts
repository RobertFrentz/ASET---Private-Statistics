import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Hospital } from '../Types/hospital';

import { HomePageComponent } from './home-page.component';

const hospitalsMock: Hospital[] = [
  {
    name: 'Arcadia',
    fields: ['Age', 'BloodType'],
  },
  {
    name: 'Saint Marie',
    fields: ['Age', 'BloodType'],
  },
];

describe('HomePageComponent', () => {
  let component: HomePageComponent;
  let fixture: ComponentFixture<HomePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomePageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HomePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should set current hospitals', () => {
    component.setCurrentHospitals(hospitalsMock);
    fixture.detectChanges();
    expect(component.selectedHospitalsList).toEqual(hospitalsMock);
  });

});
