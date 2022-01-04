import {
  Component,
  EventEmitter,
  Input,
  OnChanges,
  OnInit,
  Output,
  SimpleChanges,
} from '@angular/core';
import { MatSelectChange } from '@angular/material/select';

@Component({
  selector: 'app-select-dropdown',
  templateUrl: './select-dropdown.component.html',
  styleUrls: ['./select-dropdown.component.scss'],
})
export class SelectDropdownComponent implements OnInit, OnChanges {
  @Input() dropdownLabel: string = 'default';
  @Input() fieldsList: string[] = [];
  @Output() selectedDrowpdownValue: EventEmitter<string> = new EventEmitter();
  constructor() {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['fieldsList']) {
      this.onSelectValue(changes['fieldsList'].currentValue[0]);
    }
  }

  ngOnInit(): void {}

  onSelectValue(matValue: any): void {
    if(this.fieldsList.length > 0){
      if(matValue.value !== undefined){
        this.selectedDrowpdownValue.emit(matValue.value);
        return;
      }
      this.selectedDrowpdownValue.emit(matValue);
    }
    
  }
}
