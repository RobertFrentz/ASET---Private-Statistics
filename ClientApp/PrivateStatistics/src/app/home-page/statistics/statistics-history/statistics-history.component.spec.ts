import { ComponentFixture, TestBed } from '@angular/core/testing';
import { StatisticsHistory } from 'src/app/Types/statistics-history';
import { StatisticsHistoryLine } from 'src/app/Types/statistics-history-line';

import { StatisticsHistoryComponent } from './statistics-history.component';

const statisticalHistoryMock: StatisticsHistory[] = [
  {
    statisticalField: 'Age',
    mean: 15,
    standardDeviation: 20,
    variance: 17,
    standardError: 24,
  },
];

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

  it('should assign ids', () => {
    component.statisticsHistory = statisticalHistoryMock;
    const expectedDataSource: StatisticsHistoryLine[] = [
      {
      id: 0,
      ...statisticalHistoryMock[0]
      }
    ];
    component.assignIdsToLines();
    fixture.detectChanges();

    expect(component.dataSource).toEqual(expectedDataSource);
  })
});
