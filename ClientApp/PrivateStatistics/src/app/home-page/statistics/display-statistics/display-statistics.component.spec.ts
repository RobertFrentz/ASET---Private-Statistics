import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayStatisticsComponent } from './display-statistics.component';

describe('DisplayStatisticsComponent', () => {
  let component: DisplayStatisticsComponent;
  let fixture: ComponentFixture<DisplayStatisticsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DisplayStatisticsComponent],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplayStatisticsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
