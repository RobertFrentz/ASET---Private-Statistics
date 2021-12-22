import {
  Component,
  EventEmitter,
  OnDestroy,
  OnInit,
  Output,
} from '@angular/core';
import { FormControl } from '@angular/forms';
import { Hospital } from 'src/app/Types/hospital';
import { MultiSelectDropdownService } from './multiselect-dropwdown.service';

@Component({
  selector: 'app-multiselect-dropdown',
  templateUrl: './multiselect-dropdown.component.html',
  styleUrls: ['./multiselect-dropdown.component.scss'],
})
export class MultiselectDropdownComponent implements OnInit, OnDestroy {
  @Output() selectedHospitals: EventEmitter<Hospital[]> = new EventEmitter<
    Hospital[]
  >();

  hospitalsList: Hospital[] = [];
  hospitalsFormControl = new FormControl();
  hospitalSubscription: any;
  isSelectionPanelClosed = true;

  constructor(
    readonly multiSelectDropdownService: MultiSelectDropdownService
  ) {}

  ngOnInit(): void {
    this.hospitalSubscription = this.multiSelectDropdownService
      .getHospitals()
      .subscribe((hospitalResponse) => {
        this.hospitalsList = hospitalResponse;
      });
  }

  ngOnDestroy(): void {
    this.hospitalSubscription.unsubscribe();
  }

  onTogglePanel(): void {
    this.isSelectionPanelClosed = !this.isSelectionPanelClosed;
    this.isSelectionPanelClosed && this.hospitalsFormControl.value
      ? this.selectedHospitals.emit(this.hospitalsFormControl.value)
      : null;
  }
}
