import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatisticsHistoryComponent } from './statistics-history.component';

describe('StatisticsHistoryComponent', () => {
  let component: StatisticsHistoryComponent;
  let fixture: ComponentFixture<StatisticsHistoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatisticsHistoryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatisticsHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
