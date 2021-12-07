import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayChartsComponent } from './display-charts.component';

describe('DisplayChartsComponent', () => {
  let component: DisplayChartsComponent;
  let fixture: ComponentFixture<DisplayChartsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DisplayChartsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplayChartsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
