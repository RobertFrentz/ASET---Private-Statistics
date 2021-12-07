import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayStatisticLineComponent } from './display-statistic-line.component';

describe('DisplayStatisticLineComponent', () => {
  let component: DisplayStatisticLineComponent;
  let fixture: ComponentFixture<DisplayStatisticLineComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DisplayStatisticLineComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplayStatisticLineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
