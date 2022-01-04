import { HttpClientModule } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';
import { StatisticalResult } from 'src/app/Types/statistical-result';
import { StatisticsHistory } from 'src/app/Types/statistics-history';

import { StatisticsComponent } from './statistics.component';

const statisticalResultMock: StatisticalResult = {
  Mean: 15,
  StandardDeviation: 10,
  StandardError: 15,
  Variance: 30,
};

const statisticalHistoryMock: StatisticsHistory[] = [{
  statisticalField: 'Age',
  mean: 15,
  standardDeviation: 20,
  variance: 17,
  standardError: 24
}];

describe('StatisticsComponent', () => {
  let component: StatisticsComponent;
  let fixture: ComponentFixture<StatisticsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [StatisticsComponent],
      imports: [HttpClientModule],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatisticsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should get statistical result', () => {
    const spy = spyOn(
      component.statisticsService,
      'getStatisticsResults'
    ).and.returnValue(of(statisticalResultMock));

    const fieldMock = 'Age';
    component.computeStatisticalFunctions(fieldMock);
    fixture.detectChanges();

    expect(spy).toHaveBeenCalledWith([], fieldMock);
    expect(component.statistics).toEqual(statisticalResultMock);
  });

  it('should get statistical history', () => {
    const spy = spyOn(component.statisticsService, 'getStatisticsHistory').and.returnValue(of(statisticalHistoryMock));
    component.getStatisticsHistory();
    fixture.detectChanges();

    expect(spy).toHaveBeenCalled();
    expect(component.statisticsHistory).toEqual(statisticalHistoryMock);
  });
});
