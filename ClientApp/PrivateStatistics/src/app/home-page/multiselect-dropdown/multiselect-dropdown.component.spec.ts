import { HttpClientModule } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';
import { Hospital } from 'src/app/Types/hospital';

import { MultiselectDropdownComponent } from './multiselect-dropdown.component';

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

describe('MultiselectDropdownComponent', () => {
  let component: MultiselectDropdownComponent;
  let fixture: ComponentFixture<MultiselectDropdownComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MultiselectDropdownComponent],
      imports: [HttpClientModule],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MultiselectDropdownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should get hospitals', () => {
    const spy = spyOn(component.multiSelectDropdownService, 'getHospitals').and.returnValue(of(hospitalsMock));
    component.ngOnInit();
    fixture.detectChanges();

    expect(spy).toHaveBeenCalled();
    expect(component.hospitalsList).toEqual(hospitalsMock);

  });

  it('should emit hospitals on closing panel', () => {
    const spy = spyOn(component.selectedHospitals, 'emit');
    component.isSelectionPanelClosed = false;
    component.hospitalsFormControl.setValue('Arcadia');
    component.onTogglePanel();

    expect(spy).toHaveBeenCalled();
  })

  it('should not emit hospitals on opening panel', () => {
    const spy = spyOn(component.selectedHospitals, 'emit');
    component.isSelectionPanelClosed = true;
    component.hospitalsFormControl.setValue('Arcadia');
    component.onTogglePanel();

    expect(spy).not.toHaveBeenCalled();
  });

});
